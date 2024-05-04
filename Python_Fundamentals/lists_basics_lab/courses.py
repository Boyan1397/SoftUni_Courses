number = ['cat','dog','beast']
index = 0
while index < len(number):
    print(number[index], end=" ")
    index += 1

while number:
    print(number[0], end=" ")
    number.remove(number[0])
