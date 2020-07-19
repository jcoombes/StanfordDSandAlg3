import math
import statistics
import logging
import datetime
import utils

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
    """
    Returns the list index of the pivot rather than the value of the pivot itself.
    """
    if method.lower() == 'first':
        return left
    elif method.lower() == 'last':
        return right - 1
    elif method.lower() == 'median':
        return median_pivot(to_sort, left, right)

def median_pivot(to_sort, left, right):
  first = left
  mid = math.floor((left + right - 0.5) // 2)
  last = right - 1

  if right == left + 2 or right == left + 1:
    logging.debug(f"f:{first}, m:{mid}, l:{last}, median:{left}")
    return left

  d = {
    to_sort[first]: first,
    to_sort[mid]: mid,
    to_sort[last]: last
  }

  med_val = int(statistics.median(d.keys()))
  try:
    median_idx = d[med_val]
  except KeyError:
    logging.warning(f"f:{first}, m:{mid}, l:{last}, median:{left}")
    logging.warning(f"d:{d}, med_val: {med_val}")
    logging.warning(to_sort[left:right])
    raise KeyError(med_val) 
  logging.debug(f"f:{first}, m:{mid}, l:{last}, median:{median_idx}")
  return median_idx


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


def qs_file(list_length: int):
  
  if list_length < 0:
    long_boi = []
    with open("QuickSort.txt") as f:
        for line in f.readlines():
            long_boi.append(int(line[:-1]))
        logging.info(f"longboi is {len(long_boi)} long")
    return long_boi

  with open("QuickSort.txt") as f:
      long_boi = [int(next(f)[:-1]) for x in range(list_length)]
  return long_boi

def main(to_sort: list, pivot_choice: str):

    bucket.comp = 0
    quick_sort(to_sort, 0, len(to_sort), pivot_choice)
    logging.info(f"sported longboi is {len(to_sort)} long")
    logging.info(f"There were {bucket.comp} comparisons")

    did_it_work = utils.is_sorted(to_sort)

    print(f"For input size {len(to_sort)}, we made {bucket.comp} comparisons. \nWe used the {pivot_choice} element as our pivot. \nIs our list sorted?: {did_it_work}")


    return bucket.comp, to_sort


if __name__ == "__main__":
    out = main(qs_file(-1), 'median')
