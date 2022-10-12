'''
a = ["Nursultanuly", "Daulet", "21", "Almaty", "SU"]
b = ["Tegi: ", "Aty: ", "Jasy: ", "Kalasy: ",  "Univer: "]
print(b[0] + a[0],"\n" + b[1]+ a[1],"\n" + b[2]+a[2],"\n" + b[3]+a[3],"\n" +  b[4]+a[4])
'''
'''
sandar = []
san = input("butin san engiz(0 sony): ")
while san!="0":
    s = int(san)
    sandar.append(s)
    san = input("butin san engiz(0 sony): ")
print(sandar)
sort = sorted(sandar)
#sort = sorted(sandar,reverse = True)
print(sort)
'''
'''
a = [7, 11, 20, 1, 32, 4, 60, 1]
c = a.count(1)
print(c)
if c==2:
    print(a.index(1))
a.insert(3,15)
a.remove(4)
print(a)
a.clear()
print(a)
'''