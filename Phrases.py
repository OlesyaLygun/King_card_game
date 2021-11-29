def ReadReact (filename1, filename2, mas):
    with open(filename1, encoding='UTF8') as import_file1:
        with open(filename2, encoding='UTF8') as import_file2:
            for line in import_file1:
                mas.append(line)
                st=import_file2.readline()
                mas.append(st)
            

def ReadQuest (filename, mas):
    with open(filename, encoding='UTF8') as import_file:
        for line in import_file:
            mas.append(line)

Test=[]
ReadQuest ('yes.txt', Test)
print (*Test, sep='\n')
