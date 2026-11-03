"""Read the sample file as text, then one line at a time."""
with open("scores.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print("Whole file:")
print(contents, end="")

print("One line at a time:")
with open("scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
