def is_sorted(lst) -> bool:
  for i in range(len(lst) - 1):
    if lst[i] > lst[i+1]:
      return False
  return True