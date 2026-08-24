"""
FUNCTIONS AND MODULAR PROGRAMMING
Self-checking exercises

How to use this file
--------------------
1. Work from top to bottom.
2. Replace ONLY the `pass` statements with your code.
3. Do not change the tests at the bottom.
4. Run this file frequently.
5. "OK" means your function passed that test.
6. "X" means your result did not match what was expected.
7. If your function crashes, the test runner will show the exception and continue.

Important:
- Unless an exercise explicitly says otherwise, RETURN the answer.
- Do not use input() inside these functions.
- Do not modify the supplied tests.
- For Exercises 8, 13, and 14, do not use the built-ins named in the instructions.

Recommended use:
- Exercises 1-10: core in-class practice.
- Exercises 11-12: modular-programming practice.
- Exercises 13-15: algorithmic extension / homework if needed.
"""


# ============================================================
# PART A — FUNCTION MECHANICS
# ============================================================

# Exercise 1
def square(x):
    """
    Return the square of x.

    Examples:
        square(5)  -> 25
        square(-3) -> 9
    """
    pass


# Exercise 2
def add(a, b):
    """
    Return a + b.

    This exercise is mainly about functions with two parameters.
    """
    pass


# Exercise 3
def make_greeting(name):
    """
    Return the string: Hello, <name>!

    Example:
        make_greeting("Asha") -> "Hello, Asha!"

    Do NOT print the greeting. Return it.
    """
    pass


# Exercise 4
def is_even(n):
    """
    Return True if n is even, and False otherwise.
    """
    pass


# Exercise 5
def sign_label(x):
    """
    Return:
        "positive" if x > 0
        "negative" if x < 0
        "zero"     if x == 0
    """
    pass


# ============================================================
# PART B — FUNCTIONS WITH LOOPS AND CONDITIONALS
# ============================================================

# Exercise 6
def count_positive(numbers):
    """
    Return the number of strictly positive values in numbers.

    Zero is NOT positive.
    """
    pass


# Exercise 7
def count_vowels(word):
    """
    Return the number of vowels in word.

    Count both lowercase and uppercase vowels.
    The vowels are: a, e, i, o, u.
    """
    pass


# Exercise 8
def average(numbers):
    """
    Return the arithmetic mean of a NON-EMPTY list of numbers.

    Do NOT use sum().
    Use a loop and an accumulator.
    """
    pass


# ============================================================
# PART C — MUTABILITY AND SIDE EFFECTS
# ============================================================

# Exercise 9
def add_one_in_place(numbers):
    """
    MUTATE the given list so that every element increases by 1.

    Example:
        x = [4, 7, -1]
        add_one_in_place(x)
        # x is now [5, 8, 0]

    Do not create and return a replacement list.
    This function should return None.
    """
    pass


# Exercise 10
def squared_copy(numbers):
    """
    Return a NEW list containing the square of every number.

    IMPORTANT:
    - Do NOT modify the original list.
    - The returned list must be a different list object.

    Example:
        x = [2, 3, 4]
        y = squared_copy(x)

        x -> [2, 3, 4]
        y -> [4, 9, 16]
    """
    pass


# ============================================================
# PART D — DECOMPOSITION / HELPER FUNCTIONS
# ============================================================

# Exercise 11
def is_vowel(c):
    """
    Return True if c is a vowel and False otherwise.

    Treat uppercase and lowercase letters the same.

    Examples:
        is_vowel("a") -> True
        is_vowel("E") -> True
        is_vowel("y") -> False
    """
    pass


# Exercise 12
def count_vowels_modular(word):
    """
    Return the number of vowels in word.

    REQUIREMENT:
    Use the helper function is_vowel(c) inside this function.

    This exercise is about decomposition:
        count_vowels_modular
              |
              +----> is_vowel
    """
    pass


# ============================================================
# PART E — FIRST ALGORITHMS
# ============================================================

# Exercise 13
def largest(numbers):
    """
    Return the largest value in a NON-EMPTY list.

    Do NOT use max().

    Your solution must also work when every number is negative.
    """
    pass


# Exercise 14
def find_first(items, target):
    """
    Return the index of the FIRST occurrence of target.

    Return -1 if target is not present.

    Do NOT use list.index().

    Example:
        find_first([4, 8, 2, 8, 7], 8) -> 1
    """
    pass


# Exercise 15
def is_sorted(numbers):
    """
    Return True if numbers are in non-decreasing order.

    Equal neighbouring values are allowed.

    Examples:
        [1, 2, 2, 5] -> True
        [1, 4, 3, 7] -> False
        []            -> True
        [10]          -> True
    """
    pass


# ============================================================
# TESTS — DO NOT MODIFY ANYTHING BELOW THIS LINE
# ============================================================

passed = 0
total = 0


def check(name, got, expected):
    global passed, total
    total += 1

    if got == expected:
        passed += 1
        print("OK   ", name)
    else:
        print("X    ", name)
        print("      got:     ", repr(got))
        print("      expected:", repr(expected))


def check_call(name, func, args, expected):
    """Call a student function without allowing one exception to stop all tests."""
    try:
        got = func(*args)
        check(name, got, expected)
    except Exception as exc:
        global total
        total += 1
        print("X    ", name)
        print("      function raised:", type(exc).__name__ + ":", str(exc))


def heading(text):
    print("\n" + "=" * 64)
    print(text)
    print("=" * 64)


# ------------------------------------------------------------
heading("PART A — FUNCTION MECHANICS")

check_call("1a square(5)", square, (5,), 25)
check_call("1b square(-3)", square, (-3,), 9)
check_call("1c square(0)", square, (0,), 0)

check_call("2a add(3, 7)", add, (3, 7), 10)
check_call("2b add(-5, 2)", add, (-5, 2), -3)
check_call("2c add(1.5, 2.5)", add, (1.5, 2.5), 4.0)

check_call("3a greeting", make_greeting, ("Asha",), "Hello, Asha!")
check_call("3b greeting", make_greeting, ("Python",), "Hello, Python!")

check_call("4a is_even(8)", is_even, (8,), True)
check_call("4b is_even(7)", is_even, (7,), False)
check_call("4c is_even(0)", is_even, (0,), True)
check_call("4d is_even(-4)", is_even, (-4,), True)

check_call("5a positive", sign_label, (3,), "positive")
check_call("5b negative", sign_label, (-2,), "negative")
check_call("5c zero", sign_label, (0,), "zero")


# ------------------------------------------------------------
heading("PART B — LOOPS AND CONDITIONALS")

check_call(
    "6a mixed values",
    count_positive,
    ([4, -2, 0, 7, -3, 9],),
    3,
)
check_call(
    "6b no positive values",
    count_positive,
    ([-5, -1, 0],),
    0,
)
check_call(
    "6c all positive",
    count_positive,
    ([1, 2, 3, 4],),
    4,
)
check_call(
    "6d empty list",
    count_positive,
    ([],),
    0,
)

check_call("7a banana", count_vowels, ("banana",), 3)
check_call("7b Python", count_vowels, ("Python",), 1)
check_call("7c uppercase vowels", count_vowels, ("AEIOU",), 5)
check_call("7d rhythm", count_vowels, ("rhythm",), 0)
check_call("7e empty string", count_vowels, ("",), 0)

check_call("8a [2, 4, 6]", average, ([2, 4, 6],), 4.0)
check_call("8b [1, 2, 3, 4]", average, ([1, 2, 3, 4],), 2.5)
check_call("8c [10]", average, ([10],), 10.0)
check_call("8d negatives", average, ([-4, 0, 4],), 0.0)


# ------------------------------------------------------------
heading("PART C — MUTABILITY AND SIDE EFFECTS")

try:
    x = [4, 7, -1]
    result = add_one_in_place(x)
    check("9a list is mutated", x, [5, 8, 0])
    check("9b function returns None", result, None)
except Exception as exc:
    total += 2
    print("X     9a/9b add_one_in_place")
    print("      function raised:", type(exc).__name__ + ":", str(exc))

try:
    x = []
    result = add_one_in_place(x)
    check("9c empty list remains empty", x, [])
    check("9d still returns None", result, None)
except Exception as exc:
    total += 2
    print("X     9c/9d add_one_in_place")
    print("      function raised:", type(exc).__name__ + ":", str(exc))

try:
    original = [2, 3, 4]
    before = original.copy()
    result = squared_copy(original)

    check("10a correct squared values", result, [4, 9, 16])
    check("10b original list unchanged", original, before)

    total += 1
    if result is not original:
        passed += 1
        print("OK    10c returned a new list object")
    else:
        print("X     10c returned a new list object")
        print("      the returned list is the same object as the input list")
except Exception as exc:
    total += 3
    print("X     10a/10b/10c squared_copy")
    print("      function raised:", type(exc).__name__ + ":", str(exc))


# ------------------------------------------------------------
heading("PART D — DECOMPOSITION / HELPER FUNCTIONS")

check_call("11a is_vowel('a')", is_vowel, ("a",), True)
check_call("11b is_vowel('E')", is_vowel, ("E",), True)
check_call("11c is_vowel('y')", is_vowel, ("y",), False)
check_call("11d is_vowel('B')", is_vowel, ("B",), False)

check_call("12a modular banana", count_vowels_modular, ("banana",), 3)
check_call("12b modular AEIOU", count_vowels_modular, ("AEIOU",), 5)
check_call("12c modular rhythm", count_vowels_modular, ("rhythm",), 0)

# Special decomposition test: verify that count_vowels_modular actually
# calls the helper function is_vowel.
try:
    original_is_vowel = is_vowel
    helper_calls = 0

    def counting_is_vowel(c):
        global helper_calls
        helper_calls += 1
        return original_is_vowel(c)

    globals()["is_vowel"] = counting_is_vowel
    _ = count_vowels_modular("hello")
    globals()["is_vowel"] = original_is_vowel

    total += 1
    if helper_calls > 0:
        passed += 1
        print("OK    12d count_vowels_modular uses is_vowel()")
    else:
        print("X     12d count_vowels_modular uses is_vowel()")
        print("      your result may be right, but this exercise requires decomposition")
except Exception as exc:
    globals()["is_vowel"] = original_is_vowel
    total += 1
    print("X     12d helper-function test")
    print("      function raised:", type(exc).__name__ + ":", str(exc))


# ------------------------------------------------------------
heading("PART E — FIRST ALGORITHMS")

check_call(
    "13a ordinary maximum",
    largest,
    ([7, 2, 11, 4, 8],),
    11,
)
check_call(
    "13b all negative",
    largest,
    ([-5, -2, -9, -1],),
    -1,
)
check_call(
    "13c one element",
    largest,
    ([42],),
    42,
)
check_call(
    "13d repeated maximum",
    largest,
    ([4, 9, 2, 9, 1],),
    9,
)

check_call(
    "14a first repeated target",
    find_first,
    ([4, 8, 2, 8, 7], 8),
    1,
)
check_call(
    "14b target at first position",
    find_first,
    ([5, 2, 3], 5),
    0,
)
check_call(
    "14c target at last position",
    find_first,
    ([5, 2, 3], 3),
    2,
)
check_call(
    "14d target absent",
    find_first,
    ([4, 8, 2], 5),
    -1,
)
check_call(
    "14e empty list",
    find_first,
    ([], 5),
    -1,
)

check_call("15a increasing", is_sorted, ([1, 2, 3, 4],), True)
check_call("15b repeated values", is_sorted, ([1, 2, 2, 5],), True)
check_call("15c not sorted", is_sorted, ([1, 4, 3, 7],), False)
check_call("15d decreasing", is_sorted, ([5, 4, 3],), False)
check_call("15e one item", is_sorted, ([10],), True)
check_call("15f empty list", is_sorted, ([],), True)


# ------------------------------------------------------------
heading("SUMMARY")
print(f"Passed {passed} out of {total} tests.")

if passed == total:
    print("Excellent: every supplied test passed.")
elif passed >= 0.8 * total:
    print("Very good. Fix the remaining X results and rerun the file.")
elif passed >= 0.5 * total:
    print("Good progress. Revisit the sections with X results before moving on.")
else:
    print("Keep working from the top. Make the early functions pass before the later ones.")

print("""
Remember:
- A function should have a clear job.
- Parameters receive the objects supplied as arguments.
- print() displays; return sends a value back to the caller.
- A function can contain conditionals and loops.
- Mutable objects can be changed inside a function.
- Helper functions let us decompose a larger problem.
- Algorithms are precise procedures, not Python built-ins.
""")
