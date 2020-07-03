a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ins = int(input("insert : "))
new_a = [x for x in a if x < ins]

print(new_a)