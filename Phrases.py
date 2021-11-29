def ReadReact (filename1, filename2, mas):
    i=0
    with open(filename1, encoding='UTF8') as import_file1:
        with open(filename2, encoding='UTF8') as import_file2:
            for line in import_file1:
                mas.append(line)
                st=import_file2.readline()
                mas.append(st)
            
Test=[]
ReadReact ('yes.txt', 'yesnum.txt', Test)
print (*Test, sep='\n')
        