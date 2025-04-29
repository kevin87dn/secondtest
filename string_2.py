stra = 'My name is %s'%('Kien')
strb = 'My friends: %s, %s, %s.' %('Jim','Tom','Harry')
numa = '%d' %(7)
numb = '%d - %d = %d' %(10,3,7)
numc = '%.3f is a float' %(3.14141414)
print(str

	a)
print(strb)
print(numa)
print(numb)
print(numc)

# Class Something
class Something:
	def __repr__(self):
		return 'This is __repr__'
	def __str__(self):
		return 'This is __str__'

sth = Something()
print(type(sth))
print(sth)
sth



# f string

str1 = f'Tet 2021'
print(str1)

# format
k = 'Toi la {}? Day la {}?'.format('ai','dau')
l = 'Toi la {1}? Day la {0}?'.format('ai','dau')
m = 'Toi la {{0}}? Day la {1} {1}?'.format('ai','dau')
m = 'Toi la {who}? Day la {where}?'.format(who = 'ai',where ='dau')
print(k)
print(l)
print(m)

x = '{:^20}'.format('Hello!')
x1 = '{:*^30}'.format('Hello!')
y = '{:@<20}'.format('Hello!')
z = '{:->20}'.format('Hello!')
xyz = 'This is{:-^40} test'.format('Hello!')
print(x)
print(x1)
print(y)
print(z)
print(xyz)
print(x1,y)
# Table

# ---- phần định dạng 
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '') 
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten',  'Noi sinh') 
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano',  'Japanese') 
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969',  'Sunny Leone', 'Canada') 
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '') 
 
# ---- phần xuất kết quả 
print(row_1) 
print(row_2) 
print(row_3) 
print(row_4) 
print(row_5) 