string = input("vvedite virajenie :\n")
x=0
y=0
z=0
numbers=[""]
notdigits=[""]

for a in string:
    
    if string[0].isdigit()==False or string[len(string)-1].isdigit()==False and string[0]!="(" and string[0]!=")" and string[len(string)-1]!=")"  and string[len(string)-1]!="(":
        print("неправильно введены знаки")
        break
    if string[x].isdigit()==False and string[x-1].isdigit()==False:
        print("знаки введены подряд")
        break
    if string[x].isdigit()== True or string[x]==".":
        numbers[y]+=string[x]
        x+=1
    elif string[x].isdigit()== False:
        if string[x]!="/" and string[x]!="*" and string[x]!="+" and string[x]!="-" and string[x]!=")"
        and string[x]!="(":
            print("error")
            break
        else:
            notdigits.append("")
            notdigits[z]=string[x]
            numbers.append("")
            z+=1
            y+=1
            x+=1
    if x==len(string):
        break

    print(notdigits)
    


while notdigits[0]!="":
    x=0
    for a in string:
    
        if string[0].isdigit()==False or string[len(string)-1].isdigit()==False:
            print("неправильно введены знаки")
            break
        if string[x].isdigit()==False and string[x-1].isdigit()==False:
            print("знаки введены подряд")
            break
    
    for a in notdigits:
        if notdigits[x]=="*":
            numbers[x]=float(numbers[x])*float(numbers[x+1])
            del numbers[x+1]
            del notdigits[x]
            break
        
        elif notdigits[x]=="+" and notdigits[x+1]!="/" and notdigits[x+1]!="*":
            numbers[x]=float(numbers[x])+float(numbers[x+1])
            del numbers[x+1]
            del notdigits[x]
            break
        elif notdigits[x]=="-" and notdigits[x+1]!="/" and notdigits[x+1]!="*":
            numbers[x]=float(numbers[x])-float(numbers[x+1])
            del numbers[x+1]
            del notdigits[x]
            break
        elif notdigits[x]=="/" and numbers[x+1]!='0':
            numbers[x]=float(numbers[x])/float(numbers[x+1])
            del numbers[x+1]
            del notdigits[x]
            break
        elif notdigits[x]=="/" and numbers[x+1]=='0':
            notdigits[0]=""
            break
        x+=1

if notdigits[0]=="" and len(numbers)>1:
    print("division by zero")
else:
    print(numbers[0])
