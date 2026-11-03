import scores
import textfiles

values = textfiles.load_scores("scores.txt")
average = scores.average_score(values)
textfiles.write_report("mean.txt", average)
print("Saved mean.txt")
