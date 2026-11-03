"""Run twice and inspect history.txt: each run adds one line."""
with open("history.txt", "a", encoding="utf-8") as file:
    file.write("Processed scores.txt: mean 78.0\n")
print("Added one line to history.txt")
