
x = int(input())
y = input()

y_list = y.split()
# print(y_1list)

min = 0
choc_replaced = -1
for i in y_list:
    
    if (int(i) > min):
        choc_replaced = choc_replaced + 1
        # print(choc_replaced)
        min = int(i)
    else:
        min = int(i)

print(choc_replaced)