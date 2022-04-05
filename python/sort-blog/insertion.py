def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    temp = arr[i]
    print(j)
    while j>=0 and temp < arr[j]:
      arr[j+1] = arr[j]
      j = j - 1

    arr[j+1] = temp
  return arr

test_list = [8,4,23,42,16,15]
insertion_sort(test_list)
print(f'test_list: {test_list}')

test_list2 = [20,18,12,8,5,-2]
insertion_sort(test_list2)
print(f'test_list2: {test_list2}')
