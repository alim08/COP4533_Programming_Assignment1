import random

def generate_test_case(n, filename):
    # generate valid input file for stable matching algorithms
    with open(filename, 'w') as f:
        f.write(f"{n}\n") # write N first

        for _ in range(n): # hospital preferences
            prefs = list(range(1, n + 1))
            random.shuffle(prefs) # randomize test data
            f.write(" ".join(map(str, prefs)) + "\n")

        for _ in range(n): # student preferences
            prefs = list(range(1, n + 1))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

