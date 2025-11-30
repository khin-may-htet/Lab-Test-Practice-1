import bubble_sort as bs
def test_bubble_sort():
    # result = []
    numbers = [8,9,7,5,6,3,4,2]
    sorting_order = bs.SORT_ASCENDING
    result = bs.bubble_sort(numbers,sorting_order)
    assert result == [2,3,4,5,6,7,8,9]

def test_bubble_sort_descending():
    numbers = [8,9,7,5,6,3,4,2]
    sorting_order = bs.SORT_DESCENDING
    result = bs.bubble_sort(numbers,sorting_order)
    assert result == [9,8,7,6,5,4,3,2]

def test_bubble_sort_more_than_10():
    numbers = [8,9,7,5,6,3,4,2,1,0,11]
    sorting_order = None
    result = bs.bubble_sort(numbers,sorting_order)
    assert result == 1

def test_bubble_sort_empty():
    numbers = []
    sorting_order = None
    result = bs.bubble_sort(numbers, sorting_order)
    assert result == 0 

def test_bubble_sort_not_integers():
    numbers = [8,9,7,'a',6,3,4,2]
    sorting_order = bs.SORT_ASCENDING
    result = bs.bubble_sort(numbers, sorting_order)
    assert result == 2