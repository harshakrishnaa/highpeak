data=open("C:/Users/HARSHA/Desktop/Highpeak/input_3.txt","r")
goods=dict()
data=list(data)
n=0
line=data[0]
for w in line.split():
            if w.isnumeric():
                n=int(w)
                
for line in data[3:]:
        if ":" in line:
            l=line.split(':')
            goods[l[0]]=int(l[1])
data=open("output_3.txt","w")

new_min,old_min,start,pos1,pos2=0,999999999999,0,0,0
goodss=dict(sorted(goods.items(),key=lambda x: x[1]))
end=n-1
price=list(goodss.values())
while end<len(price):
    new_min=price[end]-price[start]
    if old_min>=new_min:
        pos1,pos2=start,end
        old_min=new_min
    start+=1
    end+=1
goodss=list(goodss.items())
data.write("Number of Employees: "+str(n)+"\n")
data.write("Here the goodies that are selected for distribution are:\n")
for i in range(pos1,pos2+1):
    data.write(goodss[i][0]+": "+str(goodss[i][1])+"\n")
data.write("And the difference between the chosen goodie with highest price and the lowest price is ")
data.write(str(old_min)+"\n")
data.close()
