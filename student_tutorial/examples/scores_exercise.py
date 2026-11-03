"""Exercise 2: read scores, replace a report, and append a history record.

Work from the examples folder. Input has one integer per nonblank line.
Skip blank lines and retain zero scores. The mean function is supplied.
Write one line with one decimal place and a final newline, replacing old text.
append_history must add a line without erasing earlier records.
Input files exist, contain valid integer text, and have at least one score.
The output folder exists. Keep input and output filenames different.

Check your work: python self_check.py files
Run in the VS Code terminal; save your edits before checking.
See README.md if your Python command is py or python3.
Compare your functions with textfiles.py after attempting the exercise.
"""


def load_scores(filename):
    """Return a list of integers in file order, skipping blank lines."""
    # TODO: use with open(...), a loop, strip(), int(), and append().
    # Return the completed list after the loop.
    pass


def average_score(values):
    """Return the mean of a nonempty numeric sequence."""
    return sum(values) / len(values)


def write_report(filename, average):
    """Replace the file with a line such as 'Average score: 78.0\n'."""
    # TODO: open in "w" mode and write a formatted string.
    pass


def append_history(filename, average):
    """Add 'Processed scores.txt: mean 78.0\n' for an average of 78.0.

    Use one decimal place, a final newline, and preserve previous records.
    """
    # TODO: open in "a" mode and write a formatted string.
    pass


if __name__ == "__main__":
    values = load_scores("scores.txt")
    print(values)                       # [78, 91, 65, 84, 72]
    average = average_score(values)
    print(average)                      # 78.0
    write_report("practice_mean.txt", average)
    append_history("practice_history.txt", average)
    # Open practice_mean.txt to check the saved line.
    # Then try edge_scores.txt: expect [78, 0, 91] and a report mean of 56.3.
