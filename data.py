import csv

rows = []

for i in range(12,0,-1) :
    if i<10 : date = f"0{i}"  
    else : date = f"{i}"
    file = open(f'Nifty 50 Data\\Jan-{date}.csv', errors="ignore")
    csvreader = csv.reader(file)
    for row in csvreader:
        if(row[1]=="Date") : 
            head = row
            continue
        if(row[1][8:10]==date) : 
            rows.append(row)
        else : break

rows.insert(0,head)

for i in range(len(rows)) : 
    rows[i] = rows[i][:2] + rows[i][4:]

a = 0
rep = 0
while(a<len(rows)-1) : 
    row = rows[a]
    b = a+1
    while(b<len(rows)) : 
        if(row[-1]==rows[b][-1] and row[-2]==rows[b][-2]) :
            del rows[b]
            rep = rep + 1
        else : b = b + 1
    a = a + 1

print(rep)

for i in range(len(rows)) : 
    if(i!=0) : rows[i][0] = i-1

f = open('Nifty 50 Data\\Jan (without retweets).csv','w',newline="")
writer = csv.writer(f)
for row in rows : 
    writer.writerow(row)