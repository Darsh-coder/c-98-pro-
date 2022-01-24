from lib2to3.pgen2.token import NAME


def swapfiledata ():
     
    filename1 = input("ENTER THE FILE 1")
    filename2 = input("ENTER THE FILE 2")

    f1 = open(filename1)
    f2 = open(filename2)

    data_a = f1.read()
    data_b = f2.read()

    with open (filename1,'w') as a :
        a.write(data_b)

    

    with open (filename2,'w') as b :
        b.write(data_a)

 

 
swapfiledata ()