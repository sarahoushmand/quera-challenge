import statistics
product = 1
number = 4
ls = []
while number >= 1:
    i = float(input())
    product = product * i
    ls.append(i)
    number -= 1
sumLs = format(sum(ls), ".6f")
averageLs = format(statistics.mean(ls), ".6f")
maxLs = format(max(ls), ".6f")
minLs = format(min(ls), ".6f")
product = format(product, ".6f")

print('Sum : ', sumLs)
print('Average : ', averageLs)
print('Product : ', product)
print('MAX : ', maxLs)
print('MIN : ', minLs)