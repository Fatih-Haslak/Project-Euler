# kareler toplamı ile toplamlar kare farkı

sonuc_1=0
sonuc_2=0
for i in range(1,101):
    sonuc_1+=i*i
    sonuc_2+=i

print((sonuc_2*sonuc_2)-sonuc_1)