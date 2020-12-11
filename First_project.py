name=input("Enter your name please:")
limit=int(1)
try:
    while(limit<10):
        print("Enter your request which is writing a file or reading a file \n If you want to write a file enter w \n If you want to read a file enter r :Mr:"+name)
        request=input("")
        #This part for write
        if(request=="w"):
            medo1=open(input("Enter the name of the file with the path like (ahmed.txt):"),"w")
            medo1.write(input("Enter what are you want to write in the file \n :"))
            medo1.close()
            print("""//////////////////////////////////////////""")
            #This part for read"
        elif(request=="r"):
            medo2=open(input("Write the name of the file which you want to read it\n Here is the name with the path please :"),"r")
            print("Here is the content: "+medo2.read()+"")
            medo2.close()
            print("""//////////////////////////////////////////""")
        else:
            print("Good bye")
            break
        #This code for stay or close
        limit=input("If you want to go out enter: close \n If you want to stay enter stay:")
        if(limit=="close"):
            limit=10           
            print("Good bye mr:"+name)
            print("This code is written by the coder:Ahmed osama")
        elif(limit=="stay"):
            limit=1
        limit+=1

except:
    print("error")
