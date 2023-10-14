text = input().upper()
set_text = list(set(text))
result = []

for t in set_text:
    result.append(text.count(t))

if result.count(max(result)) > 1:
    print("?")
else:
    print(set_text[result.index(max(result))])