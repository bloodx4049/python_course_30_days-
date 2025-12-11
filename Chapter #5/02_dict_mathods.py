marks = {
    "awais" : 80,
    "mati" : 100,
    "sami" : 90,
    "osam" : 81,
}

print(marks.items())  # dict_items([('awais', 80), ('mati', 100), ('sami', 90), ('osam', 81)])         

print(marks.keys())   # dict_keys(['awais', 'mati', 'sami', 'osam'])
print(marks.values()) # dict_values([80, 100, 90, 81])
print(marks.update({"awais": 95, "mati": 99}))  # None
print(marks)  # {'awais': 95, 'mati': 100, 'sami': 90, 'osam': 81}

print(marks.get("sami"))  # 90
print(marks.get("ibrahim"))  # None   

d = {"a": 1, "b": 2}
print(d.pop("a"))  # 1
print(d)           # {'b':2}

d = {"a": 1, "b": 2}
d.popitem()
print(d)  # {'a':1}
 
d = {"a": 1, "b": 2}
d.clear()
print(d)  # {}

d = {"a": 1, "b": 2}
copy_d = d.copy()
print(copy_d)

d = {"name": "Ali"}
d.setdefault("age", 18)
print(d)  # {'name':'Ali', 'age':18}
