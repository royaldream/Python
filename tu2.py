# from blaze import date

snack = ["Pizza", "Dosa", "Burger", "Roti", 100]
print snack.reverse()
print snack
print snack[2]
numbers = [100, 90, 300, 150, 500]
print numbers[1:3]
# print numbers.sort()
print numbers
numbers.append(200)
numbers.insert(2, 30)
print numbers
print min(numbers[1:4])
print max(numbers[1:4])

# a= (1, 2)
# a[1] = 10
# print a[1]

a = 1
b = 2
a, b = b, a
print a, b

mul = {'name' : "Parth Roy", 'age' : 20, 'date' : "05-11-1999" }
print mul['name']
print mul['age']
print mul['date']