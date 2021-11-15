x = int(input("Please enter x: "))
y = int(input("Please enter y: "))
result = 0

for i in range(1, y + 1):
    result = x ** i
print(result)