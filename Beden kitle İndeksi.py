print("""*******************************
Beden Kitle İndeksini Hesapla
*******************************""")
kilo=float(input("Kilonusu giriniz:"))
boy=float(input("Boyunuzu giriniz(metre):"))
BKİ=kilo/(boy*boy)
if BKİ<18.5:
    print("Zayıf")
elif BKİ>=18.5 and BKİ<25:
    print("Normal")
elif BKİ>=25 and BKİ<30:
    print("Fazla Kilolu")
elif BKİ>=30:
    print("Obez")
print("BKİ",BKİ)







print("****hazırlayan:Emrld****")