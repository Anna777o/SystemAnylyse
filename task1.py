import csv
def read_csv(file_name,x_cor,y_cor):
    x = []
    y = []
    with open(file_name, newline='') as csvfile:
        plot = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in plot:
            x.append((row))
        print(x[x_cor][y_cor])
    with open('new-file.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(x[x_cor][y_cor])



read_csv('example.csv',5,3)
