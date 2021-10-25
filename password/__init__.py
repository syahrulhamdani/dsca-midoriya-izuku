from random import choice

from .generator import *


class PasswordGenerator:
    """Password Generator."""

    POSSIBLE_PATTERN = []

    def __init__(self):
        """Init password generator."""
        with open("words.txt", "r") as f:
            self.word_list = f.read().split("\n")
        self.POSSIBLE_PATTERN.extend(self.word_list)

    def generate_password(self, n: int = 3):
        """Generate password from available word list.

        Args:
            n (int): number of word to choose from word list.
                Default is 3.

        Returns:
            str: password as string.
        """
        chosen = [choice(self.word_list).lower() for _ in range(n)]
        return "".join(chosen)
