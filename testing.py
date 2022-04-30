x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print (county)
for county in counties_dict.keys():
    print (county)
for voters in counties_dict.values():
    print (voters)
for county in counties_dict:
    print(counties_dict.get(county))
for key, value in dictionary_name.items():
    print(key, value)