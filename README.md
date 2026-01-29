# COP4533_Programming_Assignment1

**Team Members:**
* **Justin Oh** (78478358)
* **Adam Lim** (UFID)

---

## Project Overview
This project implements the **Gale-Shapley Algorithm** (Hospital-Proposing Deferred Acceptance) to solve the Stable Matching problem. It includes:
1.  **Matching Engine (Task A):** Finds a stable matching for $N$ hospitals and $N$ students.
2.  **Verifier (Task B):** Validates that the output is a perfect bijection and contains no blocking pairs.
3.  **Scalability Analysis (Task C):** A benchmark script to measure runtime performance as $N$ increases.

---

## Directory Structure
* `main.py`: The core program containing the `StableMatcher` class, input parser, and verifier.
* `gen.py`: A utility script to generate random input files for testing.
* `benchmark.py`: A script to automate performance testing and plot the time complexity graph.
* `scalability_graph.png`: The output graph from the benchmark script.

---

## Setup & Dependencies
The project is written in **Python 3**.
* No compilation is required.
* **Standard Libraries used:** `sys`, `random`, `collections`, `time`, `os`.
* **External Library (Task C only):** `matplotlib` is required to generate the graph.
    ```bash
    pip install matplotlib
    ```

---

## Usage Instructions

### 1. Generating Test Data
To create a random input file with $N$ pairs:
```bash
# Usage: python gen.py <N> <filename>
python gen.py 5 data/test_5.in
