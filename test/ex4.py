item = input('Nhap chuoi: ').split(',')
item.sort(reverse=True)
print(''.join(item))