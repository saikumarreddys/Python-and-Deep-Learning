
print(" ---- Deleting two characters from the input string and reversing the resultant string ----")


# Size of the list
n= int(input("Enter the no of characters :"))
l=[]
for i in range(0,n):
    x=input()
    l.append(x)
print(l)


# Deleting two characters
m = l[0:4]
print(m)

# Reversing the resultant list
n=m[::-1]
print(n)

# Converting to string
rev=''
print(rev.join(n))

# Arithematic Operators
num1 = input("Enter number 1 :")
num2 = input("Enter number 2 :")
n1 = int(num1)
n2 = int(num2)

print( " The sum is ", n1+ n2)
print(" The Difference is ",n1-n2)
print(" The Product is ",n1*n2)
print("The Division is ",n1/n2)