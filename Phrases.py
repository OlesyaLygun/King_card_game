def ReadReact (filename1, filename2, mas):
    with open(filename1, encoding='UTF8') as import_file1:
        with open(filename2, encoding='UTF8') as import_file2:
            for line in import_file1:
                mas.append(line)
                st=import_file2.readline()
                stk=st.split()[0]+', '+st.split()[1]
                mas.append(stk)
            

def ReadQuest (filename, mas):
    with open(filename, encoding='UTF8') as import_file:
        for line in import_file:
            mas.append(line)

def CheckDeath (mas, i, marker):
    global DeathMarker
    line=mas[i]
    check = line.strip().split()[0].lower()
    if check==marker:
        DeathMarker=True



Test=[]
marker='ваши'
ReadReact ('yes.txt', 'yesnum.txt', Test)
#CheckDeath(Test, 1, marker)
print (Test)
#Leng=len(Test)
#for i in range (Leng):
  #  if not DeathMarker:
  #      print(Test[i])
   # else:
    #    print('Death',)
