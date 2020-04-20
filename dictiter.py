grades = {'Ashwin':99,'David':100,'Clay':89}
#for key in grades.keys():
#    print(key,grades[key])
it = iter(grades.keys())
print(it.next())
print(it.next())
print(it.next())
ti = iter(grades.values())
print(ti.next())
print(ti.next())
print(ti.next())



