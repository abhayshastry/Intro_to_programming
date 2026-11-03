"""Supplied feedback tool. Edit the exercises, not this file.

python self_check.py modules   -- exercise 1
python self_check.py files     -- exercise 2
python self_check.py           -- both exercises

Only Python's standard library is used. Test files are created in a disposable
system temporary directory, never in the supplied datasets or student reports.
"""
import argparse
from contextlib import redirect_stdout
import importlib
import io
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("section", nargs="?", choices=("modules", "files"))
    args = parser.parse_args()
    results = {"PASS": 0, "FAIL": 0, "ERROR": 0}

    def check(name, action, expected, hint):
        try:
            actual = action()
            status = "PASS" if actual == expected else "FAIL"
            detail = "" if status == "PASS" else f"expected {expected!r}; got {actual!r}"
        except Exception as error:
            status = "ERROR"
            detail = f"{type(error).__name__}: {error}"
        results[status] += 1
        print(f"{status}: {name}")
        if detail:
            print(f"  {detail}\n  Hint: {hint}")

    def load(name):
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                module = importlib.import_module(name)
            return module, captured.getvalue()
        except Exception as error:
            # Continue to the other exercise even if this file has a syntax error.
            check(f"import {name}", lambda: (_ for _ in ()).throw(error), None,
                  f"Fix the error in {name}.py, save, and rerun this command.")
            return None, captured.getvalue()

    if args.section in (None, "modules"):
        print("\nExercise 1: modules")
        student, output = load("modules_exercise")
        if student is not None:
            check("import displays nothing", lambda: output, "",
                  'Put the demo print inside if __name__ == "__main__":.')
            check("compare two classes", lambda: student.compare_classes(
                [78, 91, 65, 84, 72], [70, 80, 90]), (78.0, 80.0),
                "Import scores, call scores.average_score for each argument, and return a tuple.")
            check("different inputs and fractional means",
                  lambda: student.compare_classes([0, 1], [90]), (0.5, 90.0),
                  "Use the two supplied lists rather than hard-coding the example results.")

            def shared_helper():
                import scores
                original = scores.average_score
                calls = []

                def replacement(values):
                    calls.append(values)
                    return 10.0 * len(calls)

                scores.average_score = replacement
                try:
                    answer = student.compare_classes([1, 2], [3, 4])
                    return answer, calls
                finally:
                    scores.average_score = original

            check("reuse the function from scores.py", shared_helper,
                  ((10.0, 20.0), [[1, 2], [3, 4]]),
                  "Use import scores and scores.average_score(...); the check temporarily changes that shared function.")

            def demonstration():
                result = subprocess.run(
                    [sys.executable, "-B", str(HERE / "modules_exercise.py")],
                    cwd=HERE, capture_output=True, text=True, timeout=5)
                if result.returncode:
                    raise RuntimeError(result.stderr.strip())
                return result.stdout

            check("running the file displays its demo", demonstration,
                  "Example comparison: (78.0, 80.0)\n",
                  "Keep the supplied demo print inside the script guard. It should still run when you execute the file.")

    if args.section in (None, "files"):
        print("\nExercise 2: files")
        student, _ = load("scores_exercise")
        if student is not None:
            with tempfile.TemporaryDirectory(prefix="python-file-practice-") as directory:
                root = Path(directory)

                def read_case(text):
                    path = root / "input.txt"
                    path.write_text(text, encoding="utf-8")
                    value = student.load_scores(str(path))
                    if not isinstance(value, list) or any(type(item) is not int for item in value):
                        raise TypeError(f"load_scores must return a list of integers; got {value!r}")
                    return value

                check("read five scores", lambda: read_case("78\n91\n65\n84\n72\n"),
                      [78, 91, 65, 84, 72],
                      "Build a list, append int(text) for each score, and return after the loop.")
                check("read a final line without a newline", lambda: read_case("91"), [91],
                      "Iterate over the file; do not drop the last line or its last character.")
                check("ignore blank lines and surrounding whitespace",
                      lambda: read_case("\n 78 \n\t\n91\n"), [78, 91],
                      "Use text = line.strip(), then if text: before calling int(text).")
                check("preserve zero, order, and repeated scores",
                      lambda: read_case("91\n0\n91\n65\n"), [91, 0, 91, 65],
                      "Check whether the string is empty before conversion; zero is a valid score.")

                def fresh_lists():
                    first = read_case("78\n91\n")
                    second = read_case("78\n91\n")
                    return first == second == [78, 91] and first is not second

                check("return a fresh list on each call", fresh_lists, True,
                      "Create scores = [] inside load_scores, before opening the file.")

                def report_case(average, prior=None):
                    path = root / "report.txt"
                    if path.exists():
                        path.unlink()
                    if prior is not None:
                        path.write_text(prior, encoding="utf-8")
                    student.write_report(str(path), average)
                    return path.read_text(encoding="utf-8")

                check("create the exact report line", lambda: report_case(78.0),
                      "Average score: 78.0\n",
                      'Open filename in "w" mode and write f"Average score: {average:.1f}\\n".')
                check("format a fractional mean to one decimal place", lambda: report_case(2 / 3),
                      "Average score: 0.7\n", "Use :.1f and include the final newline.")
                check("replace an existing report", lambda: report_case(91, "OLD\nExtra line\n"),
                      "Average score: 91.0\n", 'Use "w" for the report; "a" would retain old lines.')

                def pipeline():
                    values = read_case("78\n91\n65\n84\n72\n")
                    return report_case(student.average_score(values))

                check("read -> calculate -> write", pipeline, "Average score: 78.0\n",
                      "Return integer scores, calculate their mean, and write that number as formatted text.")

                def history_case(values, prior=None):
                    path = root / "history.txt"
                    if path.exists():
                        path.unlink()
                    if prior is not None:
                        path.write_text(prior, encoding="utf-8")
                    for value in values:
                        student.append_history(str(path), value)
                    return path.read_text(encoding="utf-8")

                check("create a history record", lambda: history_case([78.0]),
                      "Processed scores.txt: mean 78.0\n",
                      'Open filename in "a" mode and write the required formatted line.')
                check("append two different means", lambda: history_case([78.0, 2 / 3]),
                      "Processed scores.txt: mean 78.0\nProcessed scores.txt: mean 0.7\n",
                      'Use "a", retain the first record, and format the supplied average each time.')
                check("preserve earlier history", lambda: history_case([91], "Earlier record\n"),
                      "Earlier record\nProcessed scores.txt: mean 91.0\n",
                      'Use append mode so existing text remains unchanged.')

    print(f"\nResults: {results['PASS']} PASS, {results['FAIL']} FAIL, {results['ERROR']} ERROR")
    if results["FAIL"] or results["ERROR"]:
        print("Fix the first failure using its hint, save the exercise, and rerun.")
        return 1
    print("All checks passed. Explain the imports and file modes to a classmate.")
    return 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    sys.exit(main())
