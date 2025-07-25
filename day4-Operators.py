# Arithmetic operators 

x = 10
y = 3
# +  -  *  / %  // **
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =', x*y)
print('x / y =', x/y)
print('x % y =', x%y)
print('x // y =', x//y)
print('x ** y', x**y)

#comparion operators

# == >  <  >=  <=  != 
# a = 5
# b = 7
# print('5 == 7 ',a == b)   #5 == 7 False
# print('5 > 7 ',a > b)     # 5 > 7 false
# print('5 < 7', a < b)
# print('5 <= 7', a <= b)
# print('5 >= 7', a>=b)
# print('5 != 7', a!=b)

# Assignment operators 
# =     +=   -=     *=    /=     //=    %=     **=         &=

p = 10
print(p, 'after assign')
p+=1   # p = p+1
print(p, 'after p+=1')
p-=1   # p = p-1
print(p, 'after p-=1')
p*=5
print(p,'after p*=5')
# p/=3    # p = p/3
# print(p, 'after p/=3')

p//=3  # p = p//3
print(p, 'after p//=3')

p**=3   # p = p**3
print(p, 'after p**=3')


# logical operators 
# and or not 

print (5 > 2 and 10 > 11)  # False
age = 20
isIndian = True
nationality = 'Indian'
print(age>18  and  nationality == 'Indian')   #True
print(age > 10 or isIndian)     
print(not isIndian) 


a = 5 
b = 3
print(a & b)   
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)
print('a',a,'b',b)
# temp = a
# a = b
# b =temp 
# print('a',a,'b',b)

a = a^b
b = a^b
a = a^b
print('a',a,'b',b)

num = 65

# num % 2 == 0
# num & 1    # odd   


print('P' in 'Python')
numList = [1,2,3,4,5,6]
print(4 not in numList)

n1 = 33
n2 = 33
print(n1 is n2)

print(bin(n1))

