import math
import statistics
import logging
import datetime

logging.basicConfig(filename='example.log', level=logging.INFO)
logging.info(datetime.datetime.now())

def quick_sort(to_sort: list, left: int, right: int, method: str) -> list:
    if left >= right:
        logging.debug(f"left:{left}, right:{right}")
        return

    p = choose_pivot(to_sort, left, right, method)

    logging.debug(f"p: {p}, left: {left}, right:{right}")

    to_sort[p], to_sort[left] = to_sort[left], to_sort[p]
    new_piv = bucket(to_sort, left, right)  #mutates to_sort
    quick_sort(to_sort, left, new_piv, method)
    quick_sort(to_sort, new_piv + 1, right, method)
    return to_sort


def choose_pivot(to_sort, left, right, method):
    if method.lower() == 'first':
        return left
    elif method.lower() == 'last':
        return right - 1
    elif method.lower() == 'median':
        first = left
        mid = math.floor((len(to_sort) - 0.5) // 2)
        last = right - 1

        return statistics.median((first, mid, last))


def bucket(l: list, left: int, right: int) -> None:
    """
  partitions a list l around a pivot index.
  Mutates the original list and does not return anything.
  A subroutine, not a function.

  left <= right. The left and right endpoints of the partition.
  """
    pivot = left
    i = left + 1
    bucket.comp += (right - left - 1 if right > left else 0)
    for j in range(left + 1, right):
        if l[j] < l[pivot]:
            l[j], l[i] = l[i], l[j]
            i += 1

    l[pivot], l[i - 1] = l[i - 1], l[pivot]
    return i - 1


def main(list_length: int, pivot_choice: str):
    """
    long_boi = []
    with open("QuickSort.txt") as f:
        for line in f.readlines():
            long_boi.append(int(line[:-1]))
    """
    with open("QuickSort.txt") as f:
        long_boi = [int(next(f)[:-1]) for x in range(list_length)]

    bucket.comp = 0
    quick_sort(long_boi, 0, len(long_boi), pivot_choice)
    logging.info(f"There were {bucket.comp} comparisons")
    return bucket.comp


if __name__ == "__main__":
    main(10, 'first')
