""""
10'un altında 3 veya 5'in katı olan tüm doğal sayıları listelersek 3, 5, 6 ve 9 elde ederiz. 
Bu katların toplamı 23'tür. 1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.

"""


list_of_three=[]                                           
list_of_five=[]
list_of_tf=[]

for i in range(0,334):
    if(i*3<1000):
        list_of_three.append(i*3)
    if(i*5<1000):
        list_of_five.append(i*5)
    if(i*15<1000):
        list_of_tf.append(i*15)
        
print( sum(list_of_three)+ sum(list_of_five) -  sum(list_of_tf))
    
