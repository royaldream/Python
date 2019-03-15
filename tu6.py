foods = ["Dosa", "Pizza", "Munchurian", "Soup"]
for food in foods:
    print food
for ch in foods[3]:
    print ch
i = 0
while i < len(foods):
    print foods[i]
    i += 1

foods_with_keyValue = [[1,"Dosa"], [2, "Pizza"], [3, "Munchurian"], [4, "Soup"] ]

for index, item in foods_with_keyValue:
    print "Food index :-", index, " name:-", item