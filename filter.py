import sys
import os
import math
from operator import itemgetter

# time complexity:
# in simple words: sort and output the ids of largest numbers, unless it is faster to loop
# O(n log n ) -> average quasilinear time for sorting the list
# O(n * number of requested ids) while n < log (length of data) or (length of data) - N < log (length of data)
# memory complexity:
# O(n) -> worst case of sorting


def read_file(file):
    with open(file) as f:
        return f.read().splitlines()


# for easier evaluation, split each data set into a separate list of 2 elements
# cast the 2nd element of each list to int, in prepration of sorting
def format_dataset(data):
    separated_list = []
    for i in range(len(data)):
        split_data = data[i].split()
        split_data_int = (split_data[0], int(split_data[1]))
        separated_list.append(split_data_int)
    return separated_list


# N < log (length of data) => loop through dataset and get highest numbers
# return ids of highest numbers
def max_loop(formatted_data, n_values):
    largest_values_list = []
    i = 0
    while i < n_values:
        i += 1
        max_value = 0
        for j in range(len(formatted_data)):
            if formatted_data[j][1] > max_value:
                max_id, max_value = formatted_data[j]
                max_j = j
        largest_values_list.append(formatted_data[max_j][0])
        formatted_data.remove((max_id, max_value))
    return largest_values_list


# (length of data) - N < log (length of data) => loop through dataset and get lowest numbers
# remove lowest numbers and return ids of remaining numbers
def min_loop(formatted_data, n_values, dataset_length):
    i = 0
    while i < dataset_length - n_values:
        i += 1
        max_value = float("inf")
        for j in range(len(formatted_data)):
            if formatted_data[j][1] < max_value:
                max_id, max_value = formatted_data[j]
        formatted_data.remove((max_id, max_value))
    return [element[0] for element in formatted_data]


def main(largest_values):
    # set default file input, but if valid file path is given, use the specified file
    filepath = "data.txt"
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        filepath = sys.argv[1]
    data_original = read_file(filepath)

    datasets_list = format_dataset(data_original)
    datasets_list_length = len(datasets_list)
    input_larger_log_list_length = largest_values > math.log(datasets_list_length)
    input_smaller_log_list_length = largest_values < math.log(datasets_list_length)
    difference_smaller_log_list_length = (
        datasets_list_length - largest_values
    ) < math.log(datasets_list_length)
    difference_larger_equal_log_list_length = (
        datasets_list_length - largest_values
    ) >= math.log(datasets_list_length)

    if (input_larger_log_list_length) and (difference_larger_equal_log_list_length):
        # N > log (length of data) => sort the datasets in descending order of the 2nd value of each dataset
        data_sorted_by_value = sorted(datasets_list, key=itemgetter(1), reverse=True)
        # print("sort")
        # output the N-largest valid ids separately
        for unique_id in data_sorted_by_value[:largest_values]:
            print(unique_id[0])

        # Alternatively output the N-largest valid ids as a list
        # first_dataset_elements = [a_tuple[0] for a_tuple in data_sorted_by_value]
        #   print(first_dataset_elements[:largest_values])

    if input_smaller_log_list_length:
        result = max_loop(datasets_list, largest_values)
        # print("max loop")
        for id in result:
            print(id)

    if difference_smaller_log_list_length:
        result = min_loop(datasets_list, largest_values, datasets_list_length)
        # print("min loop")
        for id in result:
            print(id)


if __name__ == "__main__":
    main(5)
