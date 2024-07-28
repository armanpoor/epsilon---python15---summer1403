#list
# برای ذخیره کردین چندین داده به صورت همزمان درون یک متغییر
# miveHa = ["sib", "golaby", "narangy"]
# # tavasot tabe len v pas dadan yek list be an, mitavanim tedad value haye list ro zakhire konim 
# lenght = len(miveHa)
# print(lenght)
# print(type(miveHa))


#index
# thislist = ["apple", "banana", "cherry"]
# #               0       1           2
# #               -3      -2          -1
# dovominKhooneList = thislist[1]
# akharinKhooneList = thislist[-1]
# avlinKhooneList = thislist[-3]
# print(avlinKhooneList)


#range in index
# mitavanim be noyee kalame range ra be farsi "ta" mani konim
# range ta khooneye yeki mande be akhar miravad (ta yeki ghablesh miravad)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#            -7         -6          -5      -4        -3      -2        -1
# print(thislist[2:9])
#vaghty ke "az" koja shoroo shavad ra nanevisim, computer az index 0 shoroo mikonad
# print(thislist[:3])
# vaghty ke "ta" koja tamam shavad ra nanevisim, computer ta index akhar list edame midahad
# print(thislist[2:])
# print(thislist[-4:-1])


# check if an item exists in a list
# thislist = ["apple", "cherry","banana" ,"orange", "kiwi", "melon", "mango"]
# if "banana" in thislist:
#     print("are azizm mozm darim")
# else:
#     print("moteasefane moz ha tamoom shode")


    
# #Change Item Value
# thislist = ["apple","cherry","banana","orange","kiwi", "melon", "mango"]

# #جایگزین کردن یک مقدار دیگر با یکی از مقادری لیست
# # thislist[3] = "golaby"

# #بدون جایگزین کردن، مقداری را به "اندیس خاصی" از لیست اضافه کنم
# # thislist.insert(2 , "golaby")

# # دستور اپند یک مقدار را به آخر لیست اضافه می کند
# thislist.append("watermelon")
# print(thislist)






#Extend List
# be manzoor gostaresh daden yek list estefade mishavad
thislist = ["apple", "banana", "cherry"]
thatlist = ["mango", "pineapple", "papaya"]
# yani this list ra gostaresh bede ba "thatlist"
thislist.extend(thatlist)
print(thislist)