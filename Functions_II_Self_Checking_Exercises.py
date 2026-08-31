"""
FUNCTIONS II: COMPOSITION, SIDE EFFECTS, FUNCTIONS AS OBJECTS, AND MODULES
Self-checking exercises

Instructions
------------
1. Work from top to bottom.
2. Replace only the `pass` statements (and, where stated, complete the return expression).
3. Do NOT change the tests at the bottom.
4. Run this file frequently.
5. "OK" means the test passed. "X" means something needs fixing.
6. Unless an exercise explicitly says to mutate a list, prefer returning a result.
7. Do not use input() inside these functions.

The exercises are grouped by concept:
  Part A  Function composition
  Part B  Function contracts and arguments
  Part C  Pure functions, mutation, and side effects
  Part D  Functions as objects
  Part E  Passing functions to functions
  Part F  Decomposition with helper functions
  Part G  Modules and reusable programs

Core target for class: Exercises 1-10.
Exercises 11-14 are extensions if you finish early.
"""

import inspect
import math


# ============================================================
# PART A — FUNCTION COMPOSITION
# ============================================================

def add_one(x):
    """Return x + 1."""
    pass


def square(x):
    """Return x squared."""
    pass


def square_after_adding_one(x):
    """
    Return square(add_one(x)).

    REQUIREMENT:
    Use BOTH helper functions add_one() and square().
    Do not repeat their arithmetic directly in this function.
    """
    pass


def add_one_after_squaring(x):
    """
    Return add_one(square(x)).

    REQUIREMENT:
    Use BOTH helper functions square() and add_one().
    """
    pass


# ============================================================
# PART B — FUNCTION CONTRACTS, DEFAULTS, KEYWORD ARGUMENTS
# ============================================================

def greet(name, greeting="Hello"):
    """
    Return '<greeting>, <name>!'

    Examples:
        greet("Asha")                 -> "Hello, Asha!"
        greet("Asha", "Good morning") -> "Good morning, Asha!"

    Keep greeting="Hello" as the default parameter.
    """
    pass


def power(base, exponent=2):
    """
    Return base raised to exponent.
    Keep exponent=2 as the default.
    """
    pass


# ============================================================
# PART C — PURE FUNCTIONS, MUTATION, AND SIDE EFFECTS
# ============================================================

def append_zero_in_place(numbers):
    """
    MUTATE numbers by appending one 0.

    Return None.

    Example:
        x = [1, 2]
        append_zero_in_place(x)
        # x is now [1, 2, 0]
    """
    pass


def with_zero(numbers):
    """
    Return a NEW list containing all elements of numbers followed by 0.

    REQUIREMENTS:
    - Do NOT modify numbers.
    - Return a different list object.

    Example:
        x = [1, 2]
        y = with_zero(x)
        # x == [1, 2]
        # y == [1, 2, 0]
    """
    pass


def replace_first_locally(numbers):
    """
    This exercise is about rebinding versus mutation.

    Return a NEW list [99] + the elements after the first element.
    Do NOT modify the original list.

    Examples:
        [1, 2, 3] -> [99, 2, 3]
        [5]       -> [99]

    Assume numbers is non-empty.
    """
    pass


# ============================================================
# PART D — FUNCTIONS AS OBJECTS
# ============================================================

def double(x):
    """Return 2*x."""
    pass


def choose_operation(name):
    """
    Return a FUNCTION OBJECT based on name.

    If name == "square", return the function square.
    If name == "double", return the function double.
    Otherwise return None.

    IMPORTANT:
    Return the function itself, NOT the result of calling it.
    """
    pass


# ============================================================
# PART E — PASSING FUNCTIONS TO FUNCTIONS
# ============================================================

def apply_twice(function, x):
    """
    Apply function to x, then apply the SAME function to that result.

    Example:
        apply_twice(add_one, 5) -> 7
        apply_twice(square, 2)  -> 16
    """
    pass


def transform(items, function):
    """
    Return a NEW list obtained by applying function to every item.

    Do NOT use map().
    Do NOT modify items.

    Example:
        transform([1, 2, 3], square) -> [1, 4, 9]
    """
    pass


def select(items, predicate):
    """
    Return a NEW list containing only items for which predicate(item)
    returns True.

    Do NOT use filter().
    Do NOT modify items.
    """
    pass


# ============================================================
# PART F — DECOMPOSITION WITH REQUIRED HELPER FUNCTIONS
# ============================================================

def is_valid_mark(mark):
    """Return True exactly when mark is between 0 and 100 inclusive."""
    pass


def count_valid_marks(marks):
    """
    Return the number of valid marks in marks.

    REQUIREMENT:
    Use is_valid_mark() inside this function.
    """
    pass


def clean_and_transform(items, predicate, function):
    """
    First keep only items satisfying predicate, then apply function
    to each surviving item.

    REQUIREMENT:
    Use BOTH select() and transform().

    Example:
        clean_and_transform([-2, 3, -4, 5], is_positive, square)
        -> [9, 25]
    """
    pass


# ============================================================
# PART G — MODULES AND REUSABLE PROGRAMS
# ============================================================

def hypotenuse(a, b):
    """
    Return sqrt(a*a + b*b).

    REQUIREMENT:
    Use math.sqrt(...), not exponentiation by 0.5 and not
    `from math import sqrt`.

    This exercise reinforces the module namespace idea:
        math.sqrt(...)
    """
    pass


# ============================================================
# TEST HARNESS — DO NOT MODIFY BELOW THIS LINE
# ============================================================

passed = 0
total = 0


def heading(text):
    print("\n" + "=" * 72)
    print(text)
    print("=" * 72)


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


def check_true(name, condition, detail="condition was False"):
    global passed, total
    total += 1
    if condition:
        passed += 1
        print("OK   ", name)
    else:
        print("X    ", name)
        print("      ", detail)


def safe_call(name, function, args, expected):
    global total
    try:
        got = function(*args)
    except Exception as exc:
        total += 1
        print("X    ", name)
        print("      raised:", type(exc).__name__ + ":", str(exc))
        return
    check(name, got, expected)


def run_tests():
    global passed, total

    # --------------------------------------------------------
    heading("PART A — FUNCTION COMPOSITION")

    safe_call("1a add_one(4)", add_one, (4,), 5)
    safe_call("1b add_one(-1)", add_one, (-1,), 0)
    safe_call("2a square(5)", square, (5,), 25)
    safe_call("2b square(-3)", square, (-3,), 9)

    safe_call("3a square_after_adding_one(4)", square_after_adding_one, (4,), 25)
    safe_call("3b square_after_adding_one(-2)", square_after_adding_one, (-2,), 1)
    safe_call("4a add_one_after_squaring(4)", add_one_after_squaring, (4,), 17)
    safe_call("4b add_one_after_squaring(-2)", add_one_after_squaring, (-2,), 5)

    # Verify that the composition functions really call the helpers.
    original_add_one = globals()["add_one"]
    original_square = globals()["square"]
    calls = {"add_one": 0, "square": 0}

    def watched_add_one(x):
        calls["add_one"] += 1
        return original_add_one(x)

    def watched_square(x):
        calls["square"] += 1
        return original_square(x)

    try:
        globals()["add_one"] = watched_add_one
        globals()["square"] = watched_square
        square_after_adding_one(3)
    except Exception:
        pass
    finally:
        globals()["add_one"] = original_add_one
        globals()["square"] = original_square

    check_true(
        "3c square_after_adding_one uses both helper functions",
        calls["add_one"] > 0 and calls["square"] > 0,
        "Use add_one(...) and square(...) rather than repeating their arithmetic."
    )

    calls = {"add_one": 0, "square": 0}
    try:
        globals()["add_one"] = watched_add_one
        globals()["square"] = watched_square
        add_one_after_squaring(3)
    except Exception:
        pass
    finally:
        globals()["add_one"] = original_add_one
        globals()["square"] = original_square

    check_true(
        "4c add_one_after_squaring uses both helper functions",
        calls["add_one"] > 0 and calls["square"] > 0,
        "Use square(...) and add_one(...) rather than repeating their arithmetic."
    )

    # --------------------------------------------------------
    heading("PART B — FUNCTION CONTRACTS AND ARGUMENTS")

    safe_call("5a greet uses default", greet, ("Asha",), "Hello, Asha!")
    safe_call("5b greet custom greeting", greet, ("Asha", "Good morning"), "Good morning, Asha!")
    safe_call("5c greet another name", greet, ("Ravi",), "Hello, Ravi!")

    sig = inspect.signature(greet)
    check(
        "5d greeting has default value 'Hello'",
        sig.parameters["greeting"].default,
        "Hello"
    )

    safe_call("6a power(5)", power, (5,), 25)
    safe_call("6b power(5, 3)", power, (5, 3), 125)
    safe_call("6c power(2, 0)", power, (2, 0), 1)

    sig = inspect.signature(power)
    check("6d exponent default is 2", sig.parameters["exponent"].default, 2)

    try:
        got = power(exponent=3, base=2)
        check("6e keyword arguments work", got, 8)
    except Exception as exc:
        total += 1
        print("X     6e keyword arguments work")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    # --------------------------------------------------------
    heading("PART C — PURE FUNCTIONS, MUTATION, AND SIDE EFFECTS")

    try:
        x = [1, 2, 3]
        result = append_zero_in_place(x)
        check("7a input list is mutated", x, [1, 2, 3, 0])
        check("7b mutating function returns None", result, None)
    except Exception as exc:
        total += 2
        print("X     7a/7b append_zero_in_place")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    try:
        x = [1, 2, 3]
        before = x.copy()
        y = with_zero(x)
        check("8a returned values are correct", y, [1, 2, 3, 0])
        check("8b original list is unchanged", x, before)
        check_true(
            "8c returned object is a new list",
            y is not x,
            "Return a new list rather than the original list."
        )
    except Exception as exc:
        total += 3
        print("X     8a/8b/8c with_zero")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    try:
        x = [1, 2, 3]
        before = x.copy()
        y = replace_first_locally(x)
        check("9a replacement result", y, [99, 2, 3])
        check("9b original remains unchanged", x, before)
        check_true("9c result is a new object", y is not x, "Return a new list.")
    except Exception as exc:
        total += 3
        print("X     9a/9b/9c replace_first_locally")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    # --------------------------------------------------------
    heading("PART D — FUNCTIONS AS OBJECTS")

    safe_call("10a double(7)", double, (7,), 14)
    safe_call("10b double(-3)", double, (-3,), -6)

    try:
        op = choose_operation("square")
        check_true(
            "11a choose_operation returns square function object",
            op is square,
            "Return square, not square(...)."
        )
        check("11b returned square function can be called", op(6) if callable(op) else None, 36)
    except Exception as exc:
        total += 2
        print("X     11a/11b choose_operation('square')")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    try:
        op = choose_operation("double")
        check_true(
            "11c choose_operation returns double function object",
            op is double,
            "Return double, not double(...)."
        )
        check("11d returned double function can be called", op(6) if callable(op) else None, 12)
    except Exception as exc:
        total += 2
        print("X     11c/11d choose_operation('double')")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    safe_call("11e unknown operation returns None", choose_operation, ("cube",), None)

    # --------------------------------------------------------
    heading("PART E — PASSING FUNCTIONS TO FUNCTIONS")

    safe_call("12a apply_twice(add_one, 5)", apply_twice, (add_one, 5), 7)
    safe_call("12b apply_twice(square, 2)", apply_twice, (square, 2), 16)
    safe_call("12c apply_twice(double, 3)", apply_twice, (double, 3), 12)

    try:
        x = [1, 2, 3]
        before = x.copy()
        y = transform(x, square)
        check("13a transform with square", y, [1, 4, 9])
        check("13b transform leaves input unchanged", x, before)
        check_true("13c transform returns new list", y is not x, "Return a new list.")
        check("13d transform with double", transform([1, 2, 3], double), [2, 4, 6])
        check("13e transform empty list", transform([], square), [])
    except Exception as exc:
        total += 5
        print("X     13a-13e transform")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    def is_positive(x):
        return x > 0

    def is_even_local(x):
        return x % 2 == 0

    try:
        x = [3, -2, 0, 7, -4]
        before = x.copy()
        y = select(x, is_positive)
        check("14a select positive values", y, [3, 7])
        check("14b select leaves input unchanged", x, before)
        check_true("14c select returns new list", y is not x, "Return a new list.")
        check("14d select even values", select([1, 2, 4, 5, 8], is_even_local), [2, 4, 8])
        check("14e select empty list", select([], is_positive), [])
    except Exception as exc:
        total += 5
        print("X     14a-14e select")
        print("      raised:", type(exc).__name__ + ":", str(exc))

    # --------------------------------------------------------
    heading("PART F — DECOMPOSITION WITH HELPER FUNCTIONS")

    safe_call("15a valid mark 0", is_valid_mark, (0,), True)
    safe_call("15b valid mark 100", is_valid_mark, (100,), True)
    safe_call("15c invalid mark -1", is_valid_mark, (-1,), False)
    safe_call("15d invalid mark 101", is_valid_mark, (101,), False)

    safe_call("16a count valid marks", count_valid_marks, ([90, -1, 50, 101, 0],), 3)
    safe_call("16b all valid", count_valid_marks, ([0, 25, 100],), 3)
    safe_call("16c none valid", count_valid_marks, ([-5, 200],), 0)

    original_validator = globals()["is_valid_mark"]
    helper_calls = 0

    def watched_validator(mark):
        nonlocal_box[0] += 1
        return original_validator(mark)

    # Python does not have nonlocal at module scope; a list is a simple mutable box.
    nonlocal_box = [0]
    try:
        globals()["is_valid_mark"] = watched_validator
        count_valid_marks([10, 20, 200])
    except Exception:
        pass
    finally:
        globals()["is_valid_mark"] = original_validator

    helper_calls = nonlocal_box[0]
    check_true(
        "16d count_valid_marks actually uses is_valid_mark",
        helper_calls > 0,
        "Call is_valid_mark(mark) inside count_valid_marks."
    )

    # Require clean_and_transform to call both select and transform.
    original_select = globals()["select"]
    original_transform = globals()["transform"]
    calls = {"select": 0, "transform": 0}

    def watched_select(items, predicate):
        calls["select"] += 1
        return original_select(items, predicate)

    def watched_transform(items, function):
        calls["transform"] += 1
        return original_transform(items, function)

    try:
        globals()["select"] = watched_select
        globals()["transform"] = watched_transform
        got = clean_and_transform([-2, 3, -4, 5], is_positive, square)
        check("17a clean_and_transform result", got, [9, 25])
    except Exception as exc:
        total += 1
        print("X     17a clean_and_transform result")
        print("      raised:", type(exc).__name__ + ":", str(exc))
    finally:
        globals()["select"] = original_select
        globals()["transform"] = original_transform

    check_true(
        "17b clean_and_transform uses select and transform",
        calls["select"] > 0 and calls["transform"] > 0,
        "Use both helper functions rather than rewriting their loops."
    )

    # --------------------------------------------------------
    heading("PART G — MODULES AND REUSABLE PROGRAMS")

    safe_call("18a hypotenuse(3,4)", hypotenuse, (3, 4), 5.0)
    safe_call("18b hypotenuse(5,12)", hypotenuse, (5, 12), 13.0)

    original_sqrt = math.sqrt
    sqrt_calls = [0]

    def watched_sqrt(x):
        sqrt_calls[0] += 1
        return original_sqrt(x)

    try:
        math.sqrt = watched_sqrt
        hypotenuse(8, 15)
    except Exception:
        pass
    finally:
        math.sqrt = original_sqrt

    check_true(
        "18c hypotenuse uses math.sqrt",
        sqrt_calls[0] > 0,
        "Call math.sqrt(...) so the module namespace is explicit."
    )

    # --------------------------------------------------------
    heading("SUMMARY")
    print(f"Passed {passed} out of {total} tests.")

    if passed == total:
        print("Excellent: every supplied test passed.")
    elif passed >= 0.85 * total:
        print("Very good. Fix the remaining X results and rerun the file.")
    elif passed >= 0.60 * total:
        print("Good progress. Revisit the sections containing X results.")
    else:
        print("Work from the top. Make the earlier sections pass before the later ones.")

    print("""
Concept checklist
-----------------
- A function call produces a value.
- The result of one function can become the input to another.
- Defaults make common calls convenient; keyword arguments can make calls clearer.
- Mutation changes an existing object; a pure-style function can return a new result instead.
- `square` is a function object; `square(5)` is a function call.
- Functions can be passed into functions.
- Helper functions let us decompose larger problems.
- Modules group related reusable definitions; `math.sqrt` shows the module namespace explicitly.
""")


# This is a first look at a useful reusable-program pattern:
# importing this file will define the functions, while running this file
# directly will also execute the tests.
if __name__ == "__main__":
    run_tests()
