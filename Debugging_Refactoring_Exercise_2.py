"""
SELF-CHECKING EXERCISE 2
Debugging, Refactoring, and Program Design

This file is deliberately DIFFERENT from a normal fill-the-pass worksheet.

Most functions below already contain code — but the code is wrong, fragile,
or badly designed. Your job is to:

  1. READ the specification.
  2. READ the existing code.
  3. PREDICT what is wrong.
  4. FIX or REFACTOR the function.
  5. Run the tests.

Topics covered:
- strings and string methods
- lists and indexing
- conditionals
- for / while loops and range
- mutability and aliasing
- return vs print
- local rebinding vs mutation
- function composition
- helper functions
- functions as objects
- default arguments
- module use

Rules:
- You MAY edit the bodies of the functions in the STUDENT CODE section.
- Do not edit the tests.
- Prefer clear code over clever code.
"""

import math


# ============================================================
# STUDENT CODE — FIX THESE FUNCTIONS
# ============================================================

def initials(full_name):
    """
    Return uppercase initials separated by periods.

    Example:
        initials("  asha rao  ") -> "A.R."
        initials("john")         -> "J."
    """
    parts = full_name.split(" ")
    result = ""
    for part in parts:
        result = result + part[0].upper() + "."
    return result


def count_above(numbers, threshold=0):
    """
    Return how many values are STRICTLY greater than threshold.
    """
    count = 0
    for x in numbers:
        if x >= threshold:
            count += 1
        return count


def first_index(items, target):
    """
    Return the index of the FIRST occurrence of target.
    Return -1 if target is absent.
    Do NOT use list.index().
    """
    for x in items:
        if x == target:
            return x
    return -1


def reverse_copy(items):
    """
    Return a NEW list containing the elements in reverse order.
    Leave items unchanged.

    Requirement:
    use a WHILE loop.
    """
    result = items
    i = len(items) - 1
    while i >= 0:
        result.append(items[i])
        i -= 1
    return result


def add_marker_in_place(items, marker="END"):
    """
    MUTATE items by appending marker.
    Return None.
    """
    items = items + [marker]
    return items


def normalized_copy(words):
    """
    Return a NEW list in which each string has been stripped and lowercased.
    Leave the original list unchanged.
    """
    result = words
    for i in range(len(result)):
        result[i] = result[i].strip().lower()
    return result


def average(numbers):
    """
    Return the arithmetic mean of a non-empty list.
    Do not use sum().
    """
    total = 0
    for x in numbers:
        total += x
    print(total / len(numbers))


def largest(numbers):
    """
    Return the largest number in a non-empty list.
    Do not use max().
    Must work on an all-negative list.
    """
    best = 0
    for x in numbers:
        if x > best:
            best = x
    return best


def is_vowel(c):
    """
    Return True for a/e/i/o/u, ignoring case.
    """
    return c in "aeiou"


def count_vowels(text):
    """
    Return the number of vowels in text.

    Requirement:
    use is_vowel().
    """
    count = 0
    for c in text:
        if c in "aeiou":
            count += 1
    return count


def square(x):
    return x * x


def add_one(x):
    return x + 1


def apply_twice(function, x):
    """
    Return function(function(x)).
    """
    return function(x) * 2


def transform(values, function):
    """
    Return a NEW list containing function(x) for every x in values.
    """
    result = []
    for x in values:
        result.append(function)
    return result


def keep_if(values, predicate):
    """
    Return a NEW list containing values for which predicate(value) is True.
    """
    result = []
    for x in values:
        if predicate:
            result.append(x)
    return result


def compose(f, g, x):
    """
    Return f(g(x)).
    """
    return g(f(x))


def safe_divide(a, b, default=0):
    """
    Return a / b when b != 0.
    Otherwise return default.
    """
    if b == 0:
        print(default)
    else:
        return a / b


def hypotenuse(a, b):
    """
    Return sqrt(a^2 + b^2).
    Requirement: use math.sqrt.
    """
    return math.sqrt(a * a) + b * b


def clean_words(text):
    """
    Return a list of lowercase words.

    Remove these punctuation marks by replacing them with spaces:
        . , ! ? ; :

    Example:
        clean_words(" Hi, PYTHON! ") -> ["hi", "python"]
    """
    text = text.lower()
    return text.split(" ")


def word_frequencies(text):
    """
    Return a list of [word, count] pairs in order of FIRST appearance.

    Do NOT use dictionaries or sets.

    Requirement:
    use clean_words(text).

    Example:
        word_frequencies("red blue red")
        -> [["red", 2], ["blue", 1]]
    """
    words = clean_words(text)
    result = []
    for word in words:
        result.append([word, words.count(word)])
    return result


# ============================================================
# TESTS — DO NOT MODIFY BELOW
# ============================================================

passed_tests = 0
total_tests = 0

def check(name, got, expected):
    global passed_tests, total_tests
    total_tests += 1
    if got == expected:
        passed_tests += 1
        print("OK   ", name)
    else:
        print("X    ", name)
        print("      got:     ", repr(got))
        print("      expected:", repr(expected))


def check_close(name, got, expected, tolerance=1e-9):
    global passed_tests, total_tests
    total_tests += 1
    try:
        ok = abs(got - expected) <= tolerance
    except Exception:
        ok = False
    if ok:
        passed_tests += 1
        print("OK   ", name)
    else:
        print("X    ", name)
        print("      got:     ", repr(got))
        print("      expected:", repr(expected))


def check_call(name, function, args, expected):
    global total_tests
    try:
        got = function(*args)
        check(name, got, expected)
    except Exception as exc:
        total_tests += 1
        print("X    ", name)
        print("      raised:", type(exc).__name__ + ":", str(exc))


def heading(text):
    print("\n" + "=" * 72)
    print(text)
    print("=" * 72)


heading("STRINGS")
check_call("initials two names", initials, ("  asha rao  ",), "A.R.")
check_call("initials one name", initials, ("john",), "J.")
check_call("clean words", clean_words, (" Hi, PYTHON!  Yes? ",), ["hi", "python", "yes"])
check_call("clean words empty", clean_words, ("  !!! ",), [])

heading("LOOPS / RANGE / WHILE")
check_call("count above", count_above, ([1, 5, 2, 8], 3), 2)
check_call("strictly above", count_above, ([3, 3, 4], 3), 1)
check_call("first index repeated", first_index, ([4, 8, 2, 8], 8), 1)
check_call("first index absent", first_index, ([4, 8], 9), -1)

try:
    x = [1, 2, 3]
    before = x.copy()
    y = reverse_copy(x)
    check("reverse result", y, [3, 2, 1])
    check("reverse original unchanged", x, before)
except Exception as exc:
    total_tests += 2
    print("X     reverse_copy raised", type(exc).__name__, str(exc))

heading("MUTABILITY / RETURN")
try:
    x = [1, 2]
    result = add_marker_in_place(x)
    check("marker mutates original", x, [1, 2, "END"])
    check("marker returns None", result, None)
except Exception as exc:
    total_tests += 2
    print("X     add_marker_in_place raised", type(exc).__name__, str(exc))

try:
    x = [" A ", "B  "]
    before = x.copy()
    y = normalized_copy(x)
    check("normalized result", y, ["a", "b"])
    check("normalized original unchanged", x, before)
    total_tests += 1
    if y is not x:
        passed_tests += 1
        print("OK    normalized_copy returned new list")
    else:
        print("X     normalized_copy returned same list object")
except Exception as exc:
    total_tests += 3
    print("X     normalized_copy raised", type(exc).__name__, str(exc))

check_close("average", average([2, 4, 6]), 4.0)
check_call("largest negative", largest, ([-5, -2, -9],), -2)

heading("HELPER FUNCTIONS / COMPOSITION")
check_call("vowel lowercase", is_vowel, ("a",), True)
check_call("vowel uppercase", is_vowel, ("E",), True)
check_call("not vowel", is_vowel, ("y",), False)
check_call("count vowels uppercase", count_vowels, ("AEIOU",), 5)

# Structural check: count_vowels must actually call is_vowel
try:
    original = is_vowel
    calls = 0
    def spy(c):
        global calls
        calls += 1
        return original(c)
    globals()["is_vowel"] = spy
    count_vowels("hello")
    globals()["is_vowel"] = original
    total_tests += 1
    if calls > 0:
        passed_tests += 1
        print("OK    count_vowels uses is_vowel")
    else:
        print("X     count_vowels must use is_vowel")
except Exception as exc:
    globals()["is_vowel"] = original
    total_tests += 1
    print("X     helper-use test raised", type(exc).__name__, str(exc))

check_call("apply twice square", apply_twice, (square, 2), 16)
check_call("apply twice add one", apply_twice, (add_one, 5), 7)
check_call("transform", transform, ([1, 2, 3], square), [1, 4, 9])
check_call("keep if", keep_if, ([-2, -1, 0, 1, 2], lambda x: x > 0), [1, 2])
check_call("compose order", compose, (square, add_one, 3), 16)

heading("DEFAULT ARGUMENTS / MODULES")
check_close("safe divide normal", safe_divide(10, 4), 2.5)
check_call("safe divide default", safe_divide, (10, 0), 0)
check_call("safe divide custom default", safe_divide, (10, 0, -1), -1)
check_close("hypotenuse", hypotenuse(3, 4), 5.0)

# Structural check: hypotenuse must use math.sqrt
try:
    original_sqrt = math.sqrt
    sqrt_calls = 0
    def spy_sqrt(x):
        global sqrt_calls
        sqrt_calls += 1
        return original_sqrt(x)
    math.sqrt = spy_sqrt
    hypotenuse(5, 12)
    math.sqrt = original_sqrt
    total_tests += 1
    if sqrt_calls > 0:
        passed_tests += 1
        print("OK    hypotenuse uses math.sqrt")
    else:
        print("X     hypotenuse must use math.sqrt")
except Exception as exc:
    math.sqrt = original_sqrt
    total_tests += 1
    print("X     sqrt structural test raised", type(exc).__name__, str(exc))

heading("PROGRAM DESIGN")
check_call(
    "word frequencies",
    word_frequencies,
    ("Red, blue red! GREEN blue red.",),
    [["red", 3], ["blue", 2], ["green", 1]],
)
check_call(
    "word frequencies order",
    word_frequencies,
    ("b a b c a",),
    [["b", 2], ["a", 2], ["c", 1]],
)
check_call("word frequencies empty", word_frequencies, ("!!!",), [])

heading("FINAL RESULT")
print(f"Passed {passed_tests} out of {total_tests} tests.")

if passed_tests == total_tests:
    print("Excellent — every supplied test passed.")
else:
    print("Do not just chase the X marks. For each bug, explain WHY the original code was wrong.")

print("""
Before you finish, make sure you can explain these bugs in words:
- return placed inside a loop
- >= used when > was required
- returning an element instead of its index
- aliasing a list instead of copying it
- rebinding a parameter instead of mutating a list
- printing instead of returning
- bad initialization for an all-negative maximum
- passing a function vs calling a function
- composing functions in the wrong order
""")
