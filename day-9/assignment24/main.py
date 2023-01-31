# Dictionary vs list
# Dictionary contains key and value
dict ={"height": 173, "weight": 56.5, "gender":"Male"}
list ={ 173, 56.5, "Male"}

print("--Dictionary--")
print(dict["height"])
print(dict["weight"])
print(dict["gender"])

print("Values Only:", dict.values())
print("keys Only:", dict.keys())

print("--list--")
for item in list:
    print(item)