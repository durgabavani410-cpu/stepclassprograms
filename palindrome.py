a=input("enter the word to check:")
b=len(a)
c=0
for i in range(0,b):
    if a[i]==a[-i-1]:
        print(a[i],"=",a[-i-1])
        c+=1
    else:
        print(a[i],"=!",a[-i-1])
print(c)
print(b)
if c==b:
    print("THE WORD IS PALINDROME BY  ITERATIVE CHECK")
else:
    print("THE WORD IS NOT PALINDROME BY  ITERATIVE CHECK")






