# #fileni o'qib oldik
# with open("file.txt", "r") as a:
#     content = a.read()
#     lines = content.splitlines()
#     data = {}
#     for i in lines:
#         data[i[:-2]] = int(i[-2:])
#
#
# #kodni sharti bajarildi
# for key, value in data.items():
#     if value < 80:
#         data[key] = value + 5
#
#
# #endi faylga saqlaymiz
# with open("file.txt", "w") as a:
#     for key, value in data.items():
#         a.write(f"{key}{value}\n")
import logging

# import json
# shartidagi_data = {
#     "John Smith - ": 85,
#     "Emiyl Johnson - ": 90,
#     "Michael Brown - ": 78,
#     "Sarah Davis - ": 92,
#     "David Wilson - ": 69
# }
#
#
# #json file yaratib unga ma'lumot joylaymiz
#with open("file_path.json", 'w') as json_file:
#     json.dump(shartidagi_data, json_file, indent=4)
#
#
# #joylangan ma'lumotlarni o'qiymiz
# with open('file_path.json', 'r') as file:
#     data = json.load(file)
#
#
# #sharti bo'yicha o'zgartirib 80 dan kichkinalarga 5 ball qo'shamiza
# for key, value in data.items():
#     if value < 80:
#         data[key] = value+5
#
#
# #yangi datani jsonga yuklaymiz
# with open("file_path.json", 'w') as json_file:
#     json.dump(data, json_file, indent=4)
#
#tayyor



# import csv
#
# data = [
#     {"Name:":"John Smith", "Baho:":85},
#     {"Name:":"Emily Johnson", "Baho:":90},
#     {"Name:":"Michael Brown", "Baho:":78},
#     {"Name:":"Sarah Davis", "Baho:":92},
#     {"Name:":"David Wilson", "Baho:":69},
# ]
#
# def write_to_csv(data):
#     with open("file.csv", "w") as file:
#         main = ["Name:","Baho:"]
#         a = csv.DictWriter(file, fieldnames=main)
#         a.writeheader()
#         for i in data:
#             a.writerow(i)
#
# write_to_csv(data)
#
# def read_all():
#     with open("file.csv", "r") as file:
#         a = csv.DictReader(file)
#         p = {}
#         for i in a:
#             name = i["Name:"]
#             baho = i["Baho:"]
#             p[name] = int(baho)
#         return p
#
# dicto1 = read_all()
# print(dicto1)
# for key, value in dicto1.items():
#     if value < 80:
#         dicto1[key] = int(value + 5)
#
# p = []
# for key, value in dicto1.items():
#     j = {}
#     j["Name:"]=key
#     j["Baho:"]=value
#     p.append(j)
#
# write_to_csv(p)


import pickle

data = [
    {"Name:":"John Smith", "Baho:":85},
    {"Name:":"Emily Johnson", "Baho:":90},
    {"Name:":"Michael Brown", "Baho:":78},
    {"Name:":"Sarah Davis", "Baho:":92},
    {"Name:":"David Wilson", "Baho:":69},
]

def write_to_pickle(d, filename):
    with open(filename, "wb") as file:
        pickle.dump(d, file)

def read_from_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

write_to_pickle(data, "file.pkl")

loaded_data = read_from_pickle("file.pkl")
print(loaded_data)
for i in loaded_data:
    if i["Baho:"]<80:
        i["Baho:"] += 5

write_to_pickle(loaded_data, "file.pkl")

updated_data = read_from_pickle("file.pkl")
print(updated_data)
#tayyor
