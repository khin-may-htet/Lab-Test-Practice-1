
def display_main_menu():
    print("Please Enter Three Numbers")

def user_input():
    user_values = input().split(",")
    # print(user_input)
    
    input_list = []
    for x in user_values:
        input_list.append(float(x))
        # print(input_list)
    return input_list

def calc_average(input_list):
    average = sum(input_list)/len(input_list)
    print ("The average value is ", average)
    return average

def sort_temperature(input_list):
    sorted_tem = sorted(input_list)
    print("The sorted values are ", sorted_tem)
    return sorted_tem

def find_min_max(input_list):
    min_value = min(input_list)
    print("The minimum value is ", min_value)

    max_value = max(input_list)
    print("The maximum value is ", max_value)

def calc_median_tem(input_list):
    input_list.sort()
    n = len(input_list)

    if n%2 == 1:
        median = input_list[n//2]
    else:
        a = input_list[n//2 -1]
        b = input_list[n//2]
        median = (a + b)/2
    print("The median value is ", median)
    return median
    
    

display_main_menu()
input_list = user_input()
calc_average(input_list)
sort_temperature(input_list)
find_min_max(input_list)
calc_median_tem(input_list)


