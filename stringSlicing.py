#this program illustrate string slicing
#this program illustrate string functions like upper(),lower(),replace()


b="PYTHON is fun"
print(b[:6])
print(b[7:])
print(b[1:11])
print(b[-2:])
print(b[:-5])
print(b[-5:-2])


print(b.upper())
print(b.lower())
c=b.replace("PYTHON","C++")
d=b.replace("python","C++")

print(b)
print(c)
print(d)