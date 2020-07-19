to_sort = [1, 3, 5, 7, 2, 4, 6, 8]
rev = [8, 7, 6, 5, 4, 3, 2, 1]

class Counter(object) :
    def __init__(self, fun) :
        self._fun = fun
        self.counter=0
    def __call__(self, to_sort, left, right, comp) :
        self.counter = count_compares(left, right, comp)
        return self._fun(to_sort, left, right, comp)

def quick_sort(to_sort: list, left:int, right:int, comp: int) -> None:
  # base case
  comp = count_compares(left, right, comp)

  if left>=right:
    print(f"left:{left}, right:{right}, comp:{comp}")
    return


  p = choose_pivot(to_sort, left, right)
  
  print(f"p: {p}, left: {left}, right:{right}, l: {to_sort}, c: {comp}")

  to_sort[p], to_sort[left] = to_sort[left], to_sort[p]
  new_piv = bucket(to_sort, left, right) #mutates to_sort
  quick_sort(to_sort, left, new_piv, comp)
  quick_sort(to_sort, new_piv+1, right, comp)
  
  print(f"compr:{comp}")
  return



def choose_pivot(to_sort, left, right):
  #First approach, always choose first element index.
  return left

def bucket(l: list, left:int, right: int) -> None:
  """
  partitions a list l around a pivot index.
  Mutates the original list and does not return anything.
  A subroutine, not a function.

  left <= right. The left and right endpoints of the partition.
  """
  #Pre-process by swapping the pivot and the first element.
  pivot = left
  i = left + 1
  for j in range(left+1, right):
    if l[j] < l[pivot]:
      l[j], l[i] = l[i], l[j]
      i += 1
  
  l[pivot], l[i-1] = l[i-1], l[pivot]
  return i-1

def count_compares(left: int, right: int, comp:int):
  if left >= right:
    return comp + 0
  else:
    return comp + (right - left - 1)

if __name__ == "__main__":
  quick_sort = Counter(quick_sort)
  comparisons = quick_sort(to_sort, 0, len(to_sort), 0)
  print(f"count is {quick_sort.counter}")