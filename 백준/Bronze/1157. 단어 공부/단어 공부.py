text = input()
dict = {}

for t in text:
    if t.upper() in dict:
        dict[t.upper()] += 1
    else:
        dict[t.upper()] = 1

sorted_dict = sorted(dict.items(), key= lambda x:x[1], reverse= True)
max_value = max(sorted_dict, key= lambda x:x[1])

count = 0
for key, value in sorted_dict:
    if value == max_value[1]:
        count += 1

if count > 1:
    print("?")
else:
    print(max_value[0])