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

def main():
    data = read_data('input')
    count = 0
    for row in data:
        if is_ordered(row):
            count += 1
    print(count)

if __name__ == '__main__':
    main()