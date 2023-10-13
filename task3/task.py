import csv
import math
#r1 - тип узла r2-чтение запиьс r3 -опубликован на порт
arr=[[1.0,3.0,1.0],[2.0,1.0,0.0],[2.0,1.0,0.0],[2.0,1.0,0.0],[3.0,0.0,1.0]]
x = [[1,2,1],[1,3,1],[1,4,1],[1,5,2]]
def read_csv(file_name,x_cor,y_cor):
    with open(file_name, newline='') as csvfile:
        plot = csv.reader(csvfile, delimiter=' ', quotechar=',')
        for row in plot:
            x.append((row))
        print(x[x_cor][y_cor])
    with open('new-file.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(x[x_cor][y_cor])
def build_table(str):
    ans=[]

def count_entr():
    ans = 0.0
    for i in range(5):
        m = 0.0
        for j in range(3):
            x = arr[i][j]/4.0
            if(x!=0):
                m = m+arr[i][j]/4.0*math.log(x, 2)
        ans = ans + m
    print(-ans)
count_entr()
