#!/usr/bin/env python3

import sys
from math import floor, log10
from concurrent.futures import ProcessPoolExecutor, as_completed


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        help()
        sys.exit(1)
    n = float(sys.argv[1])
    if len(sys.argv) == 3:
        threads = int(sys.argv[2])
    else:
        threads = 1
    burn(n, threads)


def help():
    print("Single core burner computing fib(n) recursively.")
    print("  Usage: {} <hours> [number of threads]".format(sys.argv[0]))


def burn(hours, threads):
    """
    Solve:
        time(fib(36)) = 10s
        time(fib(n)) = c * 1.618**n

        10 = c ** 1.618**n
        log10(10)/log10(1.618) = log10(c)/log10(1.618) + n
        log10(10) - n*log10(1.618) = log10(c)
        10**(1 - n*log10(1.618)) = c

    """
    # c is the characteristic speed of this cpu
    # and I measured time(fib(36)) = 10s
    c = 10**(1 - 36*log10(1.618))
    n = log10(hours*3600/c)/log10(1.618)
    n = int(floor(n))
    print("Burning {} hours by stupidly calculating fib({}).".format(hours, n))
    with ProcessPoolExecutor(max_workers=threads) as pool:
        futures = {pool.submit(fib, n) for i in range(threads)}
        for index, future in enumerate(as_completed(futures)):
            print("(thread {}) fib({}) = "
                  "{} , congrats.".format(index, n, future.result()))


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    main()
