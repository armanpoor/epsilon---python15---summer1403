import datetime

while 4 > 3:
    chosen_method = int(input("agr mikhay khodet dasty saat ro begy lotfn addad 1 v agr mikhay khode computer motevajeh saat beshe addad 2 ra vared kon"))
    if chosen_method == 1 :
        zaman  = int(input("sara lotfan saat ra vared kon: "))
        if zaman>24 or zaman<0:
            print("sara khanoom lotfan saat ra dorost vared kon(dar bazeye 0 ta 24)")
            continue
        if zaman<=6 and zaman>0:
            print("nime shab bekheir")
            break
        if zaman <=14 and zaman >6:
            print("zohr bekheir")
            break
        if zaman <=19 and zaman >14:
            print("bad az zohr bekheir")
            break
        if zaman <=24 and zaman >19:
            print("shab bekheir")
            break
    elif chosen_method == 2:
        # گرفتن زمان فعلی
        now = datetime.datetime.now()
        # نمایش زمان
        if now.hour >=0 and now.hour < 6:
            print("sobh bekheir. ", "alan saat: ", now.hour)
            break
        if now.hour <=14 and now.hour >6:
            print("zohr bekheir", "alan saat: ", now.hour)
            break
        if now.hour <=19 and now.hour >14:
            print(f"bad az zohr bekheir. alan saat: {now.hour}")
            break
        if now.hour <=24 and now.hour >19:
            print("shab bekheir", "alan saat: ", now.hour)
            break

print("alan az block while oomadim biroon")