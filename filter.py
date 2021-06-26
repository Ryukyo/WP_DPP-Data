import sys
import os
from operator import itemgetter

# time complexity: O(n log n ) -> average quasilinear time for sorting the list
# memory complexity: O(n) -> worst case of sorting


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


def main(largest_values):
    # set default file input, but if valid file path is given, use the specified file
    filepath = "data.txt"
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        filepath = sys.argv[1]
    data_original = read_file(filepath)

    datasets_list = format_dataset(data_original)

    #  sort the datasets in descending order of the 2nd value of each dataset
    data_sorted_by_value = sorted(datasets_list, key=itemgetter(1), reverse=True)

    # output the N-largest valid ids separately
    for unique_id in data_sorted_by_value[:largest_values]:
        print(unique_id[0])

    #  Alternatively output the N-largest valid ids as a list
    # first_dataset_elements = [a_tuple[0] for a_tuple in data_sorted_by_value]
    # print(first_dataset_elements[:largest_values])


if __name__ == "__main__":
    main(3)
