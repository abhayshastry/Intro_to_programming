"""Exercise 1: reuse another module, then control code that runs on import.

Slides 4-7: study the completed scores.py and compare_scores.py first.
Use compare_scores.py's import/calls and scores.py's script guard as patterns.
Your exercise is another caller of the SAME supplied scores.py module.

1. Import the scores module (scores.py is beside this file).
2. Complete compare_classes using scores.average_score twice.
3. Put the final demonstration under an if __name__ == "__main__": guard.

Check your work: python self_check.py modules
Run in the VS Code terminal; save your edits before checking.
See README.md if your Python command is py or python3.
"""

# TODO: import the scores module here.


def compare_classes(first, second):
    """Return (first_mean, second_mean), using the shared module's function."""
    # TODO: call scores.average_score for each list and return both results.
    pass


# TODO: guard this demonstration so importing the module displays nothing.
print("Example comparison:", compare_classes([78, 91, 65, 84, 72], [70, 80, 90]))
