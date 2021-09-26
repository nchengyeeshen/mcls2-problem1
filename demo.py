from random import randint

from binary_search import binary_search

if __name__ == "__main__":
    print("-" * 72)
    print("Binary search demo")
    print("-" * 72)

    # Generate a random sorted list with integers in the interval [-10, 20]
    lst = list(range(randint(-10, 10), randint(10, 20), randint(1, 10)))

    # Generate a random target integer
    target = randint(-10, 20)

    print(f"Input integer list: {lst}")
    print(f"Target integer: {target}")
    print(f"Target found at index (-1 if not found): {binary_search(lst, target)}")
