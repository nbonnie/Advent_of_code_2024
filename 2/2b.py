import numpy as np

def read_data(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    data = np.array(data, dtype=object)
    return data

def is_ordered(array):
    if all(array[i] < array[i+1] for i in range(len(array)-1)) or all(array[i] > array[i+1] for i in range(len(array)-1)):
       if all(abs(array[i] - array[i+1]) <= 3 for i in range(len(array)-1)):
           return True
    return False
       
# function that makes a list of all possible combinations of dropping one element from the list
# [1, 2, 3] -> [[2, 3], [1, 3], [1, 2]]
def drop_element_combinations(array):
    return [array[:i] + array[i+1:] for i in range(len(array))]

def main():
    data = read_data('input')
    test_array = [8,6,4,4,1]
    # print(drop_element_combinations(test_array))
    # print(any([is_ordered(item) for item in drop_element_combinations(test_array)]))
    count = 0
    for row in data:
        if is_ordered(row):
            count += 1
        elif any( [is_ordered(item) for item in drop_element_combinations(row)] ):
            count += 1
    print(count)

if __name__ == '__main__':
    main()