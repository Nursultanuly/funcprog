'''
Resume = [("Aty: ","Daulet"),("Tegi: ","Nursultanuly"),("Jasy: ",21)]
for i in Resume:
    print(i)
print(len(Resume))
print("\n")
Resume.insert(4,("Number: ","87077819761"))
for i in Resume:
    print(i)
Resume.sort()
del(Resume[1])
print("\n")
for i in Resume:
    print(i)
'''
'''
set_a = {"LaLiga","EPL","Ligue 1","Bundesliga"}
for i in set_a:
    print(i)
set_a.remove("Ligue 1")
#set_a.discard("KPL")
set_a.add("Serie A")
set_a.pop()
print("\n")
for i in set_a:
    print(i)
set_a.clear()
print("\n")
for i in set_a:
    print(i)
'''
'''
car = {
  "Company": "Mercedes",
  "model": "CLS",
  "year": 2018
}
car["year"] = 2020
#del car["year"]
#car.pop("year")
car["litre"] = 3
#car.popitem()
print(car)
col = car.setdefault("color", "Black")
print(col)
print(car.keys())
print("\n")
name = ('Daulet', 'Nurdaulet', 'Ali')
age = 21
stud = dict.fromkeys(name, age)
print(stud)
print("\n")
BO = {1: 2, 2: 4, 3: 9}
BO[5]=11
print(BO)
print(BO[1])
BO.clear()
print(BO)
print("\n")
d = {a: a ** 2 for a in range(6)}
print(d)
del(d)
print(d)
'''