
sonuc=0
temp=0
liste_=[]

start=900
end=999


def palindrom_mu(sayi):
    temp=sayi
    ters = 0    
    while(sayi > 0):    
        gecici = sayi %10    
        ters = (ters *10) + gecici    
        sayi = sayi //10

    if(temp==ters):
       
        return True
    else:
      
        return False

def bul(start,end):
    for i in range(start,end):
        for a in range(start,end):
            sonuc=i*(a)
            if(palindrom_mu(sonuc)):
                liste_.append(sonuc)

while(True):
    bul(start,end)
    if(len(liste_)==0):
        start-=100
    else:
        print(liste_)
        break
