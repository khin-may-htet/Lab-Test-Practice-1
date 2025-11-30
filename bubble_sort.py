SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(numbers, sorting_order):
    num_list = numbers.copy()
    n = len(num_list)

    for item in num_list:
        if type(item) != int:
            return 2
    
    if n == 0:
        return 0

    if n < 10:
        for i in range(n-1):
            for j in range(0, n-i-1):
                if sorting_order== SORT_ASCENDING:
                    if num_list[j] > num_list[j+1]:
                        num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

                elif sorting_order == SORT_DESCENDING:
                    if num_list[j] < num_list[j+1]:
                        num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

                else:
                    arr_result = []
    else: 
        return 1
    return num_list
    

def main():
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Ascending:", bubble_sort(numbers, SORT_ASCENDING))
    print("Descending:", bubble_sort(numbers, SORT_DESCENDING))

if __name__ == "__main__":
    main()
    
  


 