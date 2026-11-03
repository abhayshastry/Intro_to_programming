"""Read integer score files and write mean-score reports."""


def load_scores(filename):
    """Return integer scores, skipping blank lines."""
    scores = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            text = line.strip()
            if text:
                scores.append(int(text))
    return scores


def write_report(filename, average):
    """Replace the file with a mean-score report."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Average score: {average:.1f}\n")
