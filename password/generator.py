from random import choice


def generate_password(n=3):
    with open("words.txt", "r") as f:
        word_list = f.read().split("\n")

    chosen = [choice(word_list).lower() for _ in range(n)]
    return "".join(chosen)
