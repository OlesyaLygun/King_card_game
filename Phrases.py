def ReadReact (filename1, filename2, mas):
    with open(filename1, encoding='UTF8') as import_file1:
        with open(filename2, encoding='UTF8') as import_file2:
            for line in import_file1:
                mas.append(line)
                st=import_file2.readline()
                if len(st.split())==2:
                    stk=st.split()[0]+', '+st.split()[1]
                else:
                    stk=st.split()[0]+', '+st.split()[1]+' '+st.split()[2]
                mas.append(stk)
            

def ReadQuest (filename, mas):
    with open(filename, encoding='UTF8') as import_file:
        for line in import_file:
            mas.append(line)
            
def ReadDateAns(filename, mas, k):
    mas=list()
    f=open(filename)
    for line in f:
        dataline=list()
        i=0
        while i<k:
            dataline.append(line)
        mas.append(dataline)
    

def CheckDeath (string):
    print(string.split())
    if len(string.split()) == 2:
        return True
    elif len(string.split()) > 2:
        print('here')
        return(False)
    '''global DeathMarker
    line=mas[i]
    #print(line)
    Leng=len(mas)
    check = line.strip().split()[0].lower()
    if check==marker:
        DeathMarker=True
        for i in range(i, Leng):
            mas[i]='Death'
    #else:
      #  DeathMarker=False'''



DeathMarker=False
Test=[]
marker='Death'
ReadReact ('no.txt', 'nonum.txt', Test)

#print(DeathMarker)
#print (Test)
#print(Leng)
#for i in range (Leng):
  #  CheckDeath(Test, i, marker)
  #  print(Test[i])
  #  if DeathMarker:
   #     mas[i]='DEATH'