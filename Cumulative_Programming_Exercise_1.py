"""
SELF-CHECKING EXERCISE 1
Cumulative Programming Exercise

This is a guided, cumulative exercise designed
to make you combine the Python ideas covered so far.

Topics used:
- variables and expressions
- strings and string methods
- lists and indexing
- membership with `in`
- conditionals and Boolean expressions
- for loops and while loops
- range()
- counters and accumulators
- functions, parameters, return values
- default arguments
- mutability and aliasing
- helper functions and composition
- functions as objects / functions passed as arguments
- importing and using the math module

Rules:
1. Replace only the `pass` statements.
2. Do not change the supplied tests.
3. Run this file often.
4. Do not hard-code answers for the visible examples.
5. Unless a function explicitly says "mutate", return the answer and leave
   the input object unchanged.
"""

import math


# ============================================================
# PART A — STRINGS -> LISTS
# ============================================================

def clean_text(text):
    """
    Return a cleaned version of text:
      - remove spaces at the beginning/end
      - convert to lowercase
      - replace each of . , ! ? ; : and apostrophe with a space
      - collapse repeated whitespace by splitting and joining with one space

    Example:
        clean_text("  Hello,   PYTHON!  ") -> "hello python"
    """
    pass


def words(text):
    """
    Return a list of cleaned words from text.

    REQUIREMENT:
    use clean_text(text).

    Example:
        words(" Hello, Python! ") -> ["hello", "python"]
    """
    pass


def count_word(text, target):
    """
    Return how many times target appears as a whole word in text.
    Comparison is case-insensitive and punctuation should not matter.

    REQUIREMENT:
    use words(text).

    Example:
        count_word("Python, python! Java.", "PYTHON") -> 2
    """
    pass


def first_long_word(text, minimum_length=6):
    """
    Return the FIRST word whose length is at least minimum_length.
    Return "" if no such word exists.

    REQUIREMENT:
    use words(text).

    Example:
        first_long_word("we study programming today", 8) -> "programming"
    """
    pass


# ============================================================
# PART B — LOOPS, RANGE, WHILE
# ============================================================

def positions_of(text, letter):
    """
    Return a list of indices at which letter occurs in text.

    Treat uppercase/lowercase as the same.
    Use range() and indexing.

    Example:
        positions_of("Banana", "a") -> [1, 3, 5]
    """
    pass


def cumulative_totals(numbers):
    """
    Return a NEW list of running totals.

    Example:
        cumulative_totals([3, 5, -2, 4]) -> [3, 8, 6, 10]

    Do NOT use sum().
    """
    pass


def take_until(items, stop_value):
    """
    Use a WHILE loop.

    Return a NEW list containing items from the beginning up to, but not
    including, the first occurrence of stop_value.

    If stop_value is absent, return a copy of the whole list.

    Examples:
        take_until([4, 7, 2, 9], 2) -> [4, 7]
        take_until([4, 7], 99)      -> [4, 7]
    """
    pass


# ============================================================
# PART C — MUTABILITY AND ALIASING
# ============================================================

def clamp_in_place(numbers, low=0, high=100):
    """
    MUTATE numbers so every value lies in [low, high].

    Values below low become low.
    Values above high become high.

    Return None.

    Example:
        x = [-5, 20, 120]
        clamp_in_place(x)
        # x is now [0, 20, 100]
    """
    pass


def clamped_copy(numbers, low=0, high=100):
    """
    Return a NEW clamped list, leaving numbers unchanged.

    REQUIREMENT:
    do not call clamp_in_place() on the original input object.
    You may make a copy and then use clamp_in_place() on the copy.
    """
    pass


def rotate_left_in_place(items):
    """
    MUTATE a non-empty list by moving its first element to the end.

    Example:
        x = [1, 2, 3, 4]
        rotate_left_in_place(x)
        # x is now [2, 3, 4, 1]

    Return None.
    """
    pass


# ============================================================
# PART D — DECOMPOSITION AND FUNCTION COMPOSITION
# ============================================================

def is_palindrome(text):
    """
    Return True if text is a palindrome after cleaning.

    Ignore spaces, punctuation, and case.

    REQUIREMENT:
    use clean_text(text), then remove spaces from the cleaned result.

    Examples:
        is_palindrome("Never odd or even") -> True
        is_palindrome("Python") -> False
    """
    pass


def word_lengths(text):
    """
    Return a list containing the length of every word.

    REQUIREMENT:
    use words(text).

    Example:
        word_lengths("I love Python") -> [1, 4, 6]
    """
    pass


def average_word_length(text):
    """
    Return the average word length as a float.
    Return 0.0 for text with no words.

    REQUIREMENTS:
    use word_lengths(text)
    do NOT use sum()
    """
    pass


def text_score(text, multiplier=1):
    """
    Return:
        number_of_words * average_word_length * multiplier

    REQUIREMENTS:
    use words(text)
    use average_word_length(text)

    Example:
        "one two three" has 3 words and average length 3.666...
    """
    pass


# ============================================================
# PART E — FUNCTIONS AS OBJECTS
# ============================================================

def square(x):
    return x * x


def absolute_value(x):
    if x < 0:
        return -x
    return x


def is_even(x):
    return x % 2 == 0


def apply_to_each(values, function):
    """
    Return a NEW list containing function(x) for every x in values.

    Do not mutate values.
    """
    pass


def keep_if(values, predicate):
    """
    Return a NEW list containing only values for which predicate(value)
    returns True.

    Do not mutate values.
    """
    pass


def compose(f, g, x):
    """
    Return f(g(x)).
    """
    pass


# ============================================================
# PART F — MODULE USE + FINAL CUMULATIVE FUNCTIONS
# ============================================================

def euclidean_length(numbers):
    """
    Return sqrt(x1^2 + x2^2 + ...).

    REQUIREMENTS:
    - use math.sqrt(...)
    - do NOT use sum()
    - work for an empty list: return 0.0

    Example:
        euclidean_length([3, 4]) -> 5.0
    """
    pass


def analyze_text(text):
    """
    Return a list with EXACTLY these four values:

        [number_of_words,
         average_word_length,
         first_word_of_length_at_least_6,
         palindrome_boolean]

    REQUIREMENTS:
    use words(text)
    use average_word_length(text)
    use first_long_word(text, 6)
    use is_palindrome(text)

    Example:
        analyze_text("Never odd or even")
        -> [4, 3.5, "", True]
    """
    pass


# ============================================================
# TEST HARNESS — DO NOT MODIFY BELOW
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


heading("PART A — STRINGS -> LISTS")
check_call("clean punctuation/case", clean_text, ("  Hello,   PYTHON!  ",), "hello python")
check_call("clean multiple punctuation", clean_text, ("A...B,, C!",), "a b c")
check_call("words normal", words, ("One, TWO three!",), ["one", "two", "three"])
check_call("words empty", words, ("   !!! ",), [])
check_call("count word", count_word, ("Python, python! Java.", "PYTHON"), 2)
check_call("count missing", count_word, ("one two", "three"), 0)
check_call("first long", first_long_word, ("we study programming today", 8), "programming")
check_call("first long absent", first_long_word, ("one two", 5), "")

heading("PART B — LOOPS / RANGE / WHILE")
check_call("positions normal", positions_of, ("Banana", "a"), [1, 3, 5])
check_call("positions upper", positions_of, ("BaNaNa", "N"), [2, 4])
check_call("positions absent", positions_of, ("abc", "z"), [])
check_call("running totals", cumulative_totals, ([3, 5, -2, 4],), [3, 8, 6, 10])
check_call("running totals empty", cumulative_totals, ([],), [])
check_call("take until found", take_until, ([4, 7, 2, 9], 2), [4, 7])
check_call("take until absent", take_until, ([4, 7], 99), [4, 7])
check_call("take until first", take_until, ([5, 6, 7], 5), [])

heading("PART C — MUTABILITY")
try:
    x = [-5, 20, 120]
    result = clamp_in_place(x)
    check("clamp mutates", x, [0, 20, 100])
    check("clamp returns None", result, None)
except Exception as exc:
    total_tests += 2
    print("X     clamp_in_place raised", type(exc).__name__, str(exc))

try:
    x = [-5, 20, 120]
    before = x.copy()
    y = clamped_copy(x)
    check("clamped copy result", y, [0, 20, 100])
    check("clamped copy original unchanged", x, before)
    total_tests += 1
    if y is not x:
        passed_tests += 1
        print("OK    clamped_copy returned a new list")
    else:
        print("X     clamped_copy returned the original list object")
except Exception as exc:
    total_tests += 3
    print("X     clamped_copy raised", type(exc).__name__, str(exc))

try:
    x = [1, 2, 3, 4]
    result = rotate_left_in_place(x)
    check("rotate mutates", x, [2, 3, 4, 1])
    check("rotate returns None", result, None)
except Exception as exc:
    total_tests += 2
    print("X     rotate_left_in_place raised", type(exc).__name__, str(exc))

heading("PART D — DECOMPOSITION / COMPOSITION")
check_call("palindrome phrase", is_palindrome, ("Never odd or even",), True)
check_call("palindrome punctuation", is_palindrome, ("Madam, I'm Adam!",), True)
check_call("not palindrome", is_palindrome, ("Python",), False)
check_call("word lengths", word_lengths, ("I love Python",), [1, 4, 6])
check_close("average word length", average_word_length("I love Python"), 11/3)
check_close("average empty", average_word_length("!!!"), 0.0)
check_close("text score", text_score("one two three"), 11.0)
check_close("text score multiplier", text_score("one two three", 2), 22.0)

heading("PART E — FUNCTIONS AS OBJECTS")
check_call("apply square", apply_to_each, ([1, 2, 3], square), [1, 4, 9])
check_call("apply abs", apply_to_each, ([-2, 3, -4], absolute_value), [2, 3, 4])
check_call("keep even", keep_if, ([1, 2, 3, 4, 5], is_even), [2, 4])
check_call("keep none", keep_if, ([1, 3, 5], is_even), [])
check_call("compose", compose, (square, absolute_value, -3), 9)

heading("PART F — MODULE USE / CUMULATIVE")
check_close("euclidean 3-4", euclidean_length([3, 4]), 5.0)
check_close("euclidean three dims", euclidean_length([1, 2, 2]), 3.0)
check_close("euclidean empty", euclidean_length([]), 0.0)

# Verify math.sqrt is actually used
try:
    original_sqrt = math.sqrt
    sqrt_calls = 0
    def spy_sqrt(x):
        global sqrt_calls
        sqrt_calls += 1
        return original_sqrt(x)
    math.sqrt = spy_sqrt
    euclidean_length([3, 4])
    math.sqrt = original_sqrt
    total_tests += 1
    if sqrt_calls > 0:
        passed_tests += 1
        print("OK    euclidean_length uses math.sqrt")
    else:
        print("X     euclidean_length must use math.sqrt")
except Exception as exc:
    math.sqrt = original_sqrt
    total_tests += 1
    print("X     math.sqrt structural test raised", type(exc).__name__, str(exc))

analysis = analyze_text("Never odd or even")
check("analyze text word count", analysis[0] if isinstance(analysis, list) and len(analysis) == 4 else None, 4)
check_close("analyze text average", analysis[1] if isinstance(analysis, list) and len(analysis) == 4 else -999, 3.5)
check("analyze text first long word", analysis[2] if isinstance(analysis, list) and len(analysis) == 4 else None, "")
check("analyze text palindrome", analysis[3] if isinstance(analysis, list) and len(analysis) == 4 else None, True)

heading("FINAL RESULT")
print(f"Passed {passed_tests} out of {total_tests} tests.")
if passed_tests == total_tests:
    print("Excellent — every supplied test passed.")
elif passed_tests >= 0.8 * total_tests:
    print("Very good. Fix the remaining X results.")
elif passed_tests >= 0.5 * total_tests:
    print("Good progress. Revisit the sections with several X results.")
else:
    print("Work from the earlier sections first, then rerun.")

print("""
The important question is not just whether the tests pass.
Can you explain:
- why each loop is needed?
- which variables are counters/accumulators?
- when an input list is mutated?
- why helper functions are useful?
- the difference between square and square(5)?
""")
