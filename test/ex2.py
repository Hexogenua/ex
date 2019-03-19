day1 = input('day 1: ').split(',')
day2 = input('day 2: ').split(',')
j=0
lst = []
for i in day1:
    lst.append(i)
    lst.append(day2[j])
    j+=1


print(lst)