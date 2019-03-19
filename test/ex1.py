value = input("Nhap n so nguyen: ")
l = value.split(' ')
t = tuple(l)
result = 0
for i in t:
    result+= int(i)
print("Tong: ",result)
