# Chuỗi trần	
print(r'OK, neu mot ngay nao do')

# Nối chuỗi
strA = "Nguyen"
strB = "Trung Kien"
strC = strA + " " + strB
print(strC)
strD = strC*5
print(strD)

# In

strK = "Kien"
strChild1 = "ie"
strChild2 = "k"
strL = strChild1 in strK
strM = strChild2 in strK
print(strL)
print(strM)
 
# Indexing
strF = strK[2]
strG = strK[-1]
strH = strK[len(strK)-3]
print(strF)
print(strG)
print(strH)

# Cut string
strCut1 = strK[1:3]
strCut2 = strK[1:len(strK)]
strCut3 = strK[1:None]
strCut4 = strK[None:None]
strCut5 = strK[None:2]
strCut6 = strK[None:]
strCut7 = strK[:]

strCut8 = strA[1:4:2]

print(strCut1)
print(strCut2)
print(strCut3)
print(strCut4)
print(strCut5)
print(strCut6)
print(strCut7)
print(strCut8)


# Ép kiểu
a = "7.1"
b = "8"
c = "-10"
d = 7.1

var_a = float(a)
var_b = int(b)
var_c = int(c)
var_d = int(d)


print(var_a)
print(var_b)
print(var_c)
print(var_d)
print(type(var_c))
print(type(d))
print(type(var_d))

# Change string

str1 = "Kiên"
str2 = str1[0:0:-1]
str3 = "Đ" + str1[1:]
print(str2)
print(str3)

print(str2, str3)
