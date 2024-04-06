name = input()
reverse_name = ''

for c in name:
    reverse_name = c + reverse_name

if name == reverse_name:
    print("1")
else:
    print("0")