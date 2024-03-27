from random import randrange

# a = [3.5,7,8,9]
# for num in a :
#     num = num + 5
# return a


# no 10
# a = [1.3, 5.4, 6.1, 1.1, 9.2]
# b = [round(num**3,2) for num in a ]
# print(b)

# no 11
# w, h = 4, 6
# a = [[randrange(4,8) for x in range (w)] for y in range(h)]
# b = [[randrange(1) for c in range (w)] for u in range(h)]
# print(a, b)

#no 17
#w, h = 4, 6
# a = [[randrange(4,8) for x in range (w)] for y in range(h)]
# b = [[ for c in range (w) if c > 3.14] for u in range(h) if u > 3.14]
a = [5.2, 4.7, 8.9, 6.7, 5.9, 2.2]
b = [i for i in range(len(a)) if a[i] > 3.14 ]
print(b)
for element in b:
    print(a[element])

# no 17a
a = [[randrange(4,8) for x in range (w)] for y in range(h)]
b = [[i for i in range(len(a)) if a[i] > 3.14] for j in range(len(a)) if a[i] > 3.14  ]