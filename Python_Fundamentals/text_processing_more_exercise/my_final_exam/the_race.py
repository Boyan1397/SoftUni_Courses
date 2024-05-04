import re

pattern = r"([#$*&%])([A-Za-z]+)([#$*&%])=(\d+)!!(.+)"

while True:
    message = input()
    matches = re.findall(pattern, message)

    if not matches:
        print('Nothing found!')
        continue

    matches = matches[0]

    first_symbol, second_symbol = matches[0], matches[2]
    if first_symbol != second_symbol:
        print('Nothing found!')
        continue

    geohash_length, geohash_code = int(matches[3]), matches[-1]
    if geohash_length != len(geohash_code):
        print('Nothing found!')
        continue

    decrypted_message = ''
    for element in geohash_code:
        new_element = chr(ord(element) + geohash_length)
        decrypted_message += new_element

    print(f"Coordinates found! {matches[1]} -> {decrypted_message}")
    break