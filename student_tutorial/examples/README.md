# Tutorial: Python modules and text files

Use the Python 3 installation you use for class. There are no packages to
install for these examples, and you do not need LaTeX.

## Start on Windows in VS Code

1. Right-click `student_tutorial.zip` in File Explorer and choose **Extract All**.
   Work in the extracted files. Keep the entire `examples` folder together.
2. In VS Code, choose **File > Open Folder** and select that `examples` folder.
   You should see `scores.py`, `scores.txt`, and `self_check.py` in Explorer.
3. Open a `.py` file. Press **Ctrl+Shift+P**, choose **Python: Select Interpreter**,
   and select the Python 3 interpreter you use for class.
4. Choose **Terminal > New Terminal**. Its current folder should be `examples`.
   PowerShell is fine. Run `python --version` and check that it reports Python 3.

Run the commands below in this terminal and save your edits before checking.
If `python` is unavailable but `py --version` reports Python 3, replace `python`
with `py` in every command. On macOS/Linux, use `python3` if necessary.

If **Python: Select Interpreter** is missing, install Microsoft's **Python**
extension in VS Code. The extension uses your existing Python installation.
If neither `python` nor `py` runs Python 3, fix the Python installation before
starting; VS Code itself does not include the Python interpreter.
See the [official VS Code setup guide](https://code.visualstudio.com/docs/python/python-tutorial)
if needed. All commands here are terminal commands, not input for the `>>>` prompt.

## 1. Reuse a function from another file

Open `scores.py` and `compare_scores.py` side by side. Predict the output:

```text
python compare_scores.py
```

Expect `Class A: 78.0` and `Class B: 80.0`. Find the import and the two calls
to `scores.average_score`. The calculation is defined once in `scores.py`.

Run `python scores.py`: expect `Example mean: 84.5`.
Then run `python -c "import scores"`: expect no output. Explain why the
`if __name__ == "__main__":` guard gives these different results.

**Exercise 1:** edit only `modules_exercise.py`. Import `scores`, complete the
function using that module, and guard the supplied demonstration. Save, then run:

```text
python self_check.py modules
```

Each failed check gives a hint. Fix the first problem and rerun until you get
`Results: 5 PASS, 0 FAIL, 0 ERROR`. Also run `python modules_exercise.py`:
it should display `Example comparison: (78.0, 80.0)`.

## 2. Read text, then turn it into numbers

Open `scores.txt`. It contains five integer scores, one per line.

```text
python read_text.py
python read_position.py
```

The first script displays the same scores using `read()` and file iteration.
The second displays `'78\n'`, `'91\n'`, and `''`: successive reads move
forward, and reading at the end returns an empty string.
Reading digits from a text file gives strings; `int()` creates the numbers
needed for arithmetic. In `textfiles.py`, follow `strip()`, the blank-line
check, `int()`, and `append()`. Why is `return` after the loop?

## 3. Write a report; append a history

```text
python make_report.py
python append_history.py
python append_history.py
```

Open the newly created `mean.txt`: expect `Average score: 78.0` and a newline.
Run `make_report.py` again: it still has one line because `"w"` replaces it.
Open `history.txt`: each run of `append_history.py` adds one line using `"a"`.
Source files and saved results remain after Python exits; variables do not.

## 4. Implement the file operations yourself

**Exercise 2:** edit only `scores_exercise.py`. Complete `load_scores`,
`write_report`, and `append_history`. The mean function is supplied.

- Reader: return integers in order, ignoring blank lines; keep zero and duplicates.
- Report: replace existing text with `Average score: 78.0\n` for a mean of 78.0.
- History: append `Processed scores.txt: mean 78.0\n` for that same mean.
- Both output formats use one decimal place and a final newline.

```text
python self_check.py files
```

The target is `Results: 12 PASS, 0 FAIL, 0 ERROR`. `FAIL` means the result
differs from the expectation; `ERROR` means an exception occurred. Both include
a hint. Failures are expected before you finish the TODOs. The checker continues
through the cases so you can see which parts already work. You do not need to
understand or edit the checker. It makes its own temporary test files and leaves
the supplied datasets and your reports alone.

Once those checks pass, run `python scores_exercise.py` and inspect
`practice_mean.txt` and `practice_history.txt`. Run it again: the report should
stay one line, while the history grows. If you get stuck, compare the worked
reader and writer in `textfiles.py` and the append example in `append_history.py`.

Finally run `python self_check.py` for both exercises: the target is
**17 PASS, 0 FAIL, 0 ERROR**.

## Try new data and explain your choices

Change the exercise demo's input to `edge_scores.txt`: expect `[78, 0, 91]`
and a report mean of `56.3`. Use `second_scores.txt` next: expect a mean of
`80.0`. Import your completed exercise into another script to save a second
report. Importing it should not run its demonstration.

Explain: What does importing a module make available? Why convert strings?
Why test for blank text before conversion? What do `"r"`, `"w"`, and `"a"`
do? What does `with` close? Where does a relative filename point?

If a demo cannot find `scores.txt`, check that your terminal is in this folder
and that you extracted all files. Relative data paths start from the terminal's
working directory. Keep input and output filenames different: `"w"` erases
the output file's old contents. These exercises assume existing input files,
valid integer text, and nonempty score lists; exception handling comes later.
