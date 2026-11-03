"""Shared score calculations; used by both lecture callers."""


def average_score(values):
    """Return the mean of a nonempty numeric sequence."""
    return sum(values) / len(values)


if __name__ == "__main__":
    print("Example mean:", average_score([78, 91]))
