"""Helpers for tests."""

import random
import re


def is_good_markdown(text: str) -> bool:
    """
    Make some checks of Markdown text.

    These are meant to catch mistakes in templates producing Markdown.

    Returns:
        True.  Will raise an exception with a failure message if something
        is wrong.
    """
    if text.startswith((" ", "\n", "\t")):
        raise ValueError(f"Markdown shouldn't start with whitespace: {text!r}")

    # HTML comments must be on a line by themselves or the Markdown won't
    # render properly.
    if re.search(".<!--", text):
        raise ValueError(f"Markdown shouldn't have an HTML comment in the middle of a line: {text!r}")
    if re.search("-->.", text):
        raise ValueError(f"Markdown shouldn't have an HTML comment with following text: {text!r}")

    return True


def random_text() -> str:
    """
    Generate a random text string.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words = []
    for _ in range(random.randint(4, 10)):
        words.append("".join(random.choice(alphabet) for _ in range(random.randrange(1, 6))))
    return " ".join(words)
