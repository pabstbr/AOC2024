#!/usr/bin/python3

inputFile = open('Day1Input')


def read_file():
    left_col = []
    right_col = []

    for line in inputFile:
        line_vals = [int(e) for e in line.split()]
        left_col.append(line_vals[0])
        right_col.append(line_vals[1])

    left_col.sort()
    right_col.sort()

    return left_col, right_col


def find_difference(col1, col2):
    total_difference = 0

    for i in range(len(col1)):
        total_difference += abs(col1[i] - col2[i])

    print("Difference: {}".format(total_difference))


def find_similarity(col1, col2):
    total_similarity = 0
    frequency_dict = {i:col2.count(i) for i in set(col2)}

    for val in col1:
        total_similarity += val * frequency_dict.get(val, 0)

    print("Similarity: {}".format(total_similarity))


if __name__ == "__main__":
    column1, column2 = read_file()
    find_difference(column1, column2)
    find_similarity(column1, column2)
