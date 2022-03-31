from insertion import insertion_sort

def test_given_sample():
  arr = [8,4,23,42,16,15]
  actual = insertion_sort(arr)
  expected = [4, 8, 15, 16, 23, 42]
  assert actual == expected

def test_reverse_sorted():
  arr = [20,18,12,8,5,-2]
  actual = insertion_sort(arr)
  expected = [-2, 5, 8, 12, 18, 20]
  assert actual == expected
