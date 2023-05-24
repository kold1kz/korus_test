'''task 2'''
import csv

def max_positive_sequence_length(arr):
    max_len = 0
    curr_len = 0

    for num in arr:
        if num > 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0

    return max_len


q=[]
with open('./file2/numbers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    q = [int(row[0]) for row in reader if row[0].lstrip("-").isdigit()]


print(max_positive_sequence_length(q))
