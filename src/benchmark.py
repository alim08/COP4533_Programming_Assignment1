import sys
from main import StableMatcher
from gen import generate_test_case
import time
import matplotlib.pyplot as plt
import os

sizes = [1, 2, 4, 8, 16, 64, 128, 256, 512]
times = []

for n in sizes:
    # generate temp file
    generate_test_case(n, "temp.in")

    # load solver
    solver = StableMatcher()
    # here we redirect stdin for the solver to read the file
    sys.stdin = open("temp.in", "r")
    solver.parse_input()

    # time the matcher
    start = time.perf_counter()
    solver.solve_match()
    end = time.perf_counter()

    times.append(end - start)
    print(f"n={n}: {end - start:.6f}s")

# plotting
plt.plot(sizes, times, marker = 'o')
plt.title("Gale-Shapley Runtime vs N")
plt.xlabel("N (Number of pairs)")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.savefig("scalability_graph.png")

