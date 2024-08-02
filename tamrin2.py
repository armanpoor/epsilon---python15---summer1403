import datetime
chozen_method = int(input("Age mikhay khodet behem saat ro dasty begy adad 1 v age mikhay khodam saat ro befahmam adad 2 ra vared kon: "))
    
while 1 <10 :
    if chozen_method == 1:
        zaman = int(input("Sara Alan Sa'at Chande: "))
        if zaman>24 or zaman<0:
            print("Sara khanoom loftn addy dar bazeye 0 ta 24 vared konid!") 
            continue
    
        elif zaman>0 and zaman<6:
            print("Nime Shab Bekheyr!")
            break

        elif zaman>6 and zaman<12:
            print("Sobh Bekheyr!")
            break
            
        elif zaman>12 and zaman<18:
            print("Ba'ad Az Zohr Bekheyr!")
            break
            
        elif zaman>18 and zaman<24:
            print("Shab Bekheyr!")
            break
    
    if chozen_method == 2:
        zaman = datetime.datetime.now().hour

        if zaman>0 and zaman<6:
            print("Nime Shab Bekheyr!")
            break

        elif zaman>6 and zaman<12:
            print("Sobh Bekheyr!")
            break
            
        elif zaman>12 and zaman<18:
            print("Ba'ad Az Zohr Bekheyr!")
            break
            
        elif zaman>18 and zaman<24:
            print("Shab Bekheyr!")
            break