a=input("ENTER NAME,ROLLNUMBER,DEPARTMENT IN THIS FORMAT:")
words=a.split(',')
if len(words)<3:
    print("INVALID INPUT")
else:
    print(words[0],'|',words[1],'|',words[2])
