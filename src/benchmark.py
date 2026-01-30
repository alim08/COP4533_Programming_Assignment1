import sys
from main import StableMatcher
from gen import generate_test_case
import time
import matplotlib.pyplot as plt
import os

sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
matcher_times = []
verifier_times = []

for n in sizes:
    #generate temp file
    generate_test_case(n, "temp.in")

    #load solver
    solver = StableMatcher()
    #here we redirect stdin for the solver to read the file
    sys.stdin = open("temp.in", "r")
    solver.parse_input()
    sys.stdin.close()

    #time the matcher
    start = time.perf_counter()
    result = solver.solve_match()
    end = time.perf_counter()
    matcher_time = end - start
    matcher_times.append(matcher_time)
    
    #time the verifier
    start = time.perf_counter()
    verification = solver.verify_matching(result)
    end = time.perf_counter()
    verifier_time = end - start
    verifier_times.append(verifier_time)
    
    print(f"n={n}: matcher={matcher_time:.6f}s, verifier={verifier_time:.6f}s")

#clean up temp file
if os.path.exists("temp.in"):
    os.remove("temp.in")

#plotting - two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

#matcher plot
ax1.plot(sizes, matcher_times, marker='o', color='blue')
ax1.set_title("Matcher Runtime vs N")
ax1.set_xlabel("N (Number of pairs)")
ax1.set_ylabel("Time (seconds)")
ax1.grid(True)

#verifier plot
ax2.plot(sizes, verifier_times, marker='s', color='red')
ax2.set_title("Verifier Runtime vs N")
ax2.set_xlabel("N (Number of pairs)")
ax2.set_ylabel("Time (seconds)")
ax2.grid(True)

plt.tight_layout()
plt.savefig("scalability_graph.png", dpi=150)
print("\nGraph saved as scalability_graph.png")

