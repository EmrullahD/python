print("""--------******************---------
RANDOM SAYI TAHMİN ETME OYUNUNA HOŞGELDİNİZ
--------******************----------""")

import random
import time
giriş_hakkı = 5

i=random.randint(1,100)

while True:

    sayı = int(input("1 ile 100 arasında bir sayı giriniz::"))

    if i == sayı:
        print("girdiginiz sayı değerlendiriyor....")
        time.sleep(1)
        print("kazandınız mı acaba....")
        time.sleep(2)
        print("vee....")
        time.sleep(2)
        print(":) :)Tebrikler, bildiniz..")
        break
    elif i>sayı:
        print("girdiginiz sayı değerlendiriyor....")
        time.sleep(2)
        print("şansına güveniyorum.....")
        time.sleep(2)
        print("maalesef, hemen daha büyük sayı giriniz")
        giriş_hakkı -= 1
    elif i<sayı:
        print("girdiginiz sayı değerlendiriyor....")
        time.sleep(1)
        print("sanki bildiniz....")
        time.sleep(2)
        print("vee....")
        time.sleep(2)
        print("hayırrrr olamaz ,daha küçük bir sayı giriniz")
        giriş_hakkı -= 1

    if giriş_hakkı==0:
        print(" :( :( maalesef giriş hakkınız bitmiştir,kaybettiniz ......")
        time.sleep(2)
        print("tekrar deneyiniz")
        time.sleep(2)
        break
