import time
from aocs.aoc1 import aoc1_easy, aoc1_hard


def run_it(f):
    print(f"Running {f.__name__}")
    start = time.time()
    f()
    print(f"{time.time() - start} seconds")


if __name__ == "__main__":
    run_it(aoc1_hard)
