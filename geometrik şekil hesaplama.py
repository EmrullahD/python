print(""""****************
      GEOMETRİK ŞEKİL BULMA
      *************************""")
a=input("Üçgen veya dörtgenden birini seçiniz: ")
if a=="üçgen":
    x=float(input("üçgenin 1. kenarını giriniz:"))
    y= float(input("üçgenin 2. kenarını giriniz:"))
    z = float(input("üçgenin 3. kenarını giriniz:"))
    if (x==y or x==z or y==z)and (abs(y -z )<x<y+z and abs(x-z)<y<x+z and abs(x-y)<z<x+y):
        print("üçgeniniz ikizkenar üçgendir")
    elif x==y==z and (abs(y-z)<x<y+z and abs(x-z)<y<x+z and abs(x-y)<z<x+y):
        print("üçgeniniz eşkenar üçgendir")
    elif x!=y!=z and (abs(y-z)<x<y+z and abs(x-z)<y<x+z and abs(x-y)<z<x+y):
        print("üçgeniniz çeşitkenar üçgendir")
    else:
        print("üçgen belirtmiyor")
if a=="dörtgen":
    b = float(input("dörtgenin 1. kenarını giriniz:"))
    c = float(input("dörtgennin 2. kenarını giriniz:"))
    d = float(input("dörtgenin 3. kenarını giriniz:"))
    g = float(input("dörtgenin 4. kenarını giriniz:"))
    if b==c==d==g and b!=0 and c!=0 and d!=0 and g!=0:
        print("dörtgeniniz karedir")
    elif ((b==c and d==g) or (b==d and g==c) or (b==g and c==d)) and b!=0 and c!=0 and d!=0 and g!=0:
        print("dörtgeniniz dikdörtgendir")
    elif ((b==c and d!=g)or(b==d and g!=c) or (b==g and c!=d) or( b!=c and d==g) or (b!=d and g==c) or (b!=g and c==d)or b!=c!=d!=g) and b!=0 and c!=0 and d!=0 and g!=0:
        print ("dörtgeniniz çeşitkenar dörtgendir")
    else:
        print("dörtgen belirtmiyor")


