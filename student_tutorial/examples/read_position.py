"""Each read starts where the previous read stopped."""
with open("two_lines.txt", "r", encoding="utf-8") as file:
    first = file.readline()
    rest = file.read()
    again = file.read()

print(repr(first))  # '78\n'
print(repr(rest))   # '91\n'
print(repr(again))  # ''
