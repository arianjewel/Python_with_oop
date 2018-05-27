import csv

with open('book_list.csv',newline='') as csvfile:
    csv_reader=csv.reader(csvfile)
    for row in csv_reader:
        print(row)
