import time


def sort_a(word_list):

    """
    Recursive implementation of quick- or mergesort.
    Parameter
    ---------
    word_list : list of str
    list to be sorted
    Returns
    -------
    int
    sum of all swaps and comparisons
    float
    time used in ms

    """

    # return mergesort_or_quicksort(word_list)

    start = time.time()
    sorted_list = quicksort(word_list + [0])

    ende = time.time()
    comparisons = sorted_list.pop()
    time_ms = (ende-start)*1000

    return [comparisons] + [time_ms] + sorted_list



def quicksort(word_list):
    length = len(word_list)
    if length <=1:
        return word_list
    comparisons = word_list.pop()
    pivot = word_list.pop()

    lower = []
    higher = []

    for item in word_list:
        comparisons += 1
        if item < pivot:
            lower.append(item)
        else:
            higher.append(item)

    sorted_lower = quicksort(lower+ [comparisons])
   # print(sorted_lower)
    comp_lower = sorted_lower.pop()
    sorted_higher = quicksort(higher+ [0])
    comp_higher = sorted_higher.pop()

    return sorted_lower + [pivot] + sorted_higher + [comp_lower+comp_higher]