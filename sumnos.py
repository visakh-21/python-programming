#program to find the sum of n natural numbers
n=int(input("enter the limit: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    


print("The sum is", sum)  
