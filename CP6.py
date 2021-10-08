min=int(99999999999)
f=int(0)
count=int(0)
print("Введите длину листа")
try:
    x=int(input())
    array=[0]*x
    for i in range(x):
        array[i]=int(input("Введите число "))
    print("Массив",array)
    print("Введите дельта")
    delta=int(input())
except ValueError:
    print("Incorrect value")
    exit()
else:
        for i in range(x):
            if array[i]< min:
                min=array[i]
for i in range(x):
    if (array[i]-min==delta) | (array[i]+min==delta):
        f=1
        count+=1
if f==0:
    print("Нет подходящих элементов или дельта отрицательная")
else:
    print("Количество элементов удволетворяющих условию", count)    
    
