d1 = {}
print type(d1)
d2 = {
    "Name": "Parth Roy",
    "age": 20,
    "obj": {"spi": 10, "cgpi": 10}
    }
print d2["Name"], d2["age"]
print d2["obj"]["spi"]
d2["education"] = "Computer Engineering"
print d2
d3 = d2
d4 = d2.copy()
del d2["Name"]
print d3, d4
print d3.keys()
d4.update({"Name": "Royal Dreams"})
print d4.values()
print d4.items()