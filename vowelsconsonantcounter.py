word=input("ENTER THE SENTENCE OR WORD:")
c=0
b=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(word)):
    if word[i] in b:
        c+=1
    else:
        continue
print(c)