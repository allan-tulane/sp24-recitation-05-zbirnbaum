import random
import time
import tabulate


def ssort(L):
  ### selection sort
  if (len(L) == 1):
    return (L)
  else:
    m = L.index(min(L))
    print('selecting minimum %s' % L[m])
    L[0], L[m] = L[m], L[0]
    print('recursively sorting L=%s\n' % L[1:])
    return [L[0]] + ssort(L[1:])


# includes code from module 05 lecture:
def qsort(a, pivot_fn):
  if len(a) <= 1:
    return a
  else:
    pivot = pivot_fn(a)
    left = list(filter(lambda x: x < pivot, a))
    right = list(filter(lambda x: x > pivot, a))
    return qsort(left, pivot_fn) + [pivot] + qsort(right, pivot_fn)


def time_search(sort_fn, mylist):
  """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
  start = time.time()
  sort_fn(mylist)
  return (time.time() - start) * 1000
  ###


def compare_sort(sizes=[10, 20, 50, 100, 200, 500]):
  ## had to modify sizes list because of system memory issues
  """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

  ### TODO - sorting algorithms for comparison
  def qsort_fixed_pivot(a):
    return qsort(a, lambda x: x[0])

  def qsort_random_pivot(a):
    return qsort(a, random.choice)

  tim_sort = sorted
  result = []
  for size in sizes:
    # create list in ascending order
    mylist = list(range(size))
    # shuffles list if needed
    #random.shuffle(mylist)
    result.append([
        len(mylist),
        time_search(qsort_fixed_pivot, mylist),
        time_search(qsort_random_pivot, mylist),
        time_search(ssort, mylist)
    ])
  return result
  ###


def print_results(results):
  """ change as needed for comparisons """
  print(
      tabulate.tabulate(
          results,
          headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'ssort'],
          floatfmt=".3f",
          tablefmt="github"))


def test_print():
  print_results(compare_sort())


random.seed()
test_print()
