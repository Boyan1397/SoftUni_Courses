secret_message = input().split()
final_list = []
for message in secret_message:
    numbers = ''
    for element in message:
        if element.isdigit():
            numbers += element
    message = message.replace(numbers, "")
    final_message = chr(int(numbers))
    
    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]
    final_message += message
    final_list.append(final_message)

print(" ".join(final_list))