#روش هایی که تا بحال برای ذخیره کردن داده یادگرفته ایم
a = 2
b = "sara"
c = [4,976,"ali","mohammad"]
# be alamat [] dar engilsh migan: squeare bracket

#dictionary
# be alamat {} dar engilsh migan: curly bracket
# car = {
#     "brand":"saipa" ,
#     "model": "shahin",
#     "year": 1403
#     }
# # چجوری میتونم به ولیو هر اندیس دسترسی داشته باشم؟
# brand_MyCar = car["brand"]
# model_MyCar = car["model"]
# year_MyCar = car["year"]
# print(brand_MyCar ,model_MyCar, year_MyCar)


# rafie_car = {
#     "model": "iranKhodro",
#     "year" : 1395,
#     "esm_mashin": "denaPlus"
# }

# salary_car = {
#     "model":"bahmanKHodro",
#     "year" : 1397,
#     "esm_mashin": "rispect"
# }

# if salary_car["year"] > rafie_car["year"]:
#     print("mashin salary jadid tar ast")
# else:
#     print("mashin rafie jadid tar ast")


# # حلقه ها در لیست
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# indexs_of_thisdict = []
# values_of_thisdict = []

# #توسط حلقه زیر ما به هر اندیس از دیکشنری دسترسی داریم
# # dar har halghe, andis dar motheghair x rikhte mishavad v dar halghe bady andis bady jaygozin ba meghdar ghably x mishavad
# for x in thisdict:
#     indexs_of_thisdict.append(x)

# for y in thisdict.values():
#     values_of_thisdict.append(y)
    
# print("andis haye dictioanry: ", indexs_of_thisdict)
# print("value haye dictioanry: ", values_of_thisdict)


# Nested Dictionaries
# دیکشنری های تو در تو

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "farzand 1: " : child1,
  "farzand 2: " : child2,
  "farzand 3: " : child3
}

print(myfamily)


