# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random


def simulate(n_numbers, n_replications):
    """Simulates generating n random numbers and returns the probability that the first number generated is the
    highest."""
    count = 0
    if n_replications == 0:
        print(f"Invalid n_replications. Program stopping ...")
        exit(1)
    for i in range(n_replications):
        numbers = [random.random() for _ in range(n_numbers)]

        # Find the highest number.
        highest = max(numbers)

        # Count the number of times the first number is the highest.

        if numbers[0] == highest:
            count += 1
    # Return the probability that the first number is the highest.
    return count / n_replications


def prompt_user():
    n = int(input("Enter the number of n random numbers or enter 0 to stop\n"))
    if n == 0:
        print("Program stopping ...")
        exit(1)
    replications = int(input("Enter the number of replications you want\n"))
    average_probability = simulate(n, replications)
    print(f"Average probability for {n} random numbers in  {replications} replications:", average_probability)
    while True:
        if average_probability == 1 / n:
            return f"Average probability for {n} random numbers:{average_probability}"
        prompt_user()


if __name__ == '__main__':
    prompt_user()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
