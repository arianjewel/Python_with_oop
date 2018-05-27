import csv

field_names=['Name','Author','Publisher','Price','Catagory']

book1=['Computer Programming Part 1','Tamim Shahriar','Onnorokom Prokasoni','240.00','Programming']
book2=['Computer Programming Part 2','Tamim Shahriar','Dimik Prokasoni','250.00','Programming']
book3=['Learn Programming With Python','Tamim Shahriar','Dimik Prokasoni','200.00','Programming']

book_list=[book1,book2,book3]

with open('books.csv','w') as csvf:
    csv_writer=csv.writer(csvf,delimiter=',',quotechar='/',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(field_names)
    for book in book_list:
        csv_writer.writerow(book)
    #csv_writer.writerows(book_list)






'''import csv

field_names=['Name','Author','Publisher','Price']

book1={'Name': 'Computer Programming, Part 1','Author': 'Tamim Shahriar','Publisher': 'Onnorokom Prokasoni','Price': '240.00'}
book2={'Name': 'Computer Programming, Part 2','Author': 'Tamim Shahriar','Publisher': 'Dimik Prokasoni','Price': '240.00'}
book3={'Name': 'Learn Programming With Python','Author': 'Tamim Shahriar','Publisher': 'Dimik Prokasoni','Price': '200.00'}

book_list=[book1,book2,book3]

with open('book_list.csv','w') as csvf:
    csv_writer=csv.DictWriter(csvf,field_names)
    csv_writer.writeheader()
    csv_writer.writerows(book_list)'''
