import math #used for math.floor
import statistics #used to calculate median.
import utils #I created a helper function to check if list sorted.

def quick_sort(to_sort: list, left: int, right: int, pivot_choice: str) -> list:
  """
  Input:
  to_sort - the list to be sorted. like sorted(), quick_sort sorts in place.

  left, right - these are list indices, when we make recursive calls to this function, we don't pass in slices of to_sort, we pass in left and right indices.

  pivot_choice - 'first', 'median', 'last' which pivot would you like? see choose pivot for further information.

  returns to_sort - the sorted list.
  """
    if left >= right:
        return

    p = choose_pivot(to_sort, left, right, pivot_choice)
    #pre-process for bucket subroutine by swapping pivot and first element.
    to_sort[p], to_sort[left] = to_sort[left], to_sort[p] 
    #bucket() partitions the list into [ <p, p, >p ].
    #Note that <p is not sorted. >p is also not sorted.
    new_piv = bucket(to_sort, left, right)  
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
  """
  Median of three pivot rule takes the first, middle and last elements of the list.

  For an odd length list, middle is defined as expected.
  For an even length list, middle picks the left of the two middle elements.

  Then chooses the median of those first, middle, last.
  """
  
  first = left
  mid = math.floor((left + right - 0.5) // 2)
  last = right - 1

  #We need first, middle and last to be distinct.
  if right == left + 2 or right == left + 1:
    return left

  d = {
    to_sort[first]: first,
    to_sort[mid]: mid,
    to_sort[last]: last
  }

  med_val = int(statistics.median(d.keys()))
  median_idx = d[med_val]
  return median_idx


def bucket(l: list, left: int, right: int) -> None:
  """
  partitions a list l around a pivot index.
  Mutates the original list and does not return anything.
  A subroutine, not a function.

  left <= right. The left and right endpoints of the partition.
  e.g. bucket([0, 1, 2, 5, 3, 4], 3, 5) would only partition 
  [5, 3, 4]

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
  """
  Open QuickSort.txt and extract the first list_length integers.

  If list_length < 0, get the whole txt file of 10,000 ints.
  """
  if list_length < 0:
    long_boi = []
    with open("QuickSort.txt") as f:
        for line in f.readlines():
            long_boi.append(int(line[:-1]))
    return long_boi

  with open("QuickSort.txt") as f:
      long_boi = [int(next(f)[:-1]) for x in range(list_length)]
  return long_boi

def main(to_sort: list, pivot_choice: str):

    bucket.comp = 0
    quick_sort(to_sort, 0, len(to_sort), pivot_choice)
    did_it_work = utils.is_sorted(to_sort)

    print(f"For input size {len(to_sort)}, we made {bucket.comp} comparisons. \nWe used the {pivot_choice} element as our pivot. \nIs our list sorted?: {did_it_work}")

    return bucket.comp, to_sort


if __name__ == "__main__":
    out = main(qs_file(-1), 'median')