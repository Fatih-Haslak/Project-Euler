#ekok X e kadar olan sayılara tam bölünebilen en kucuk sayi
sonuc=0
obeb=1
flag=-1
print("----------------")
def ekok(x1,x2):
    global flag
    global sonuc
    global obeb

    if(x2==11):
       return sonuc
    
    else:

        if(x1<x2):  
            k=x1
            b=x2
        else:
            k=x2
            b=x1
      
        for i in range(2,k+2):

            if(x1 % i ==0 and x2 % i==0):
                
                obeb=i
                flag=1
        
        if(flag!=1):
            obeb=1
        sonuc = int( (x1 * x2) / obeb)

        print("{} -> x1 {} ->  x2 ".format(x1,x2))

        print("Bulunan obeb -> ",obeb)

        print("Bulunan okek ->",sonuc)

        print("----------------")

        flag=0

        return ekok( sonuc, (x2+1) )
                
b=ekok(2,3)
print("| - > Sonucumuz {}'dir < - |".format(b))