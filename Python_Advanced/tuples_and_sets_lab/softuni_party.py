n_lines = int(input())
reservation_codes = set()

for _ in range(n_lines):
    code = input()
    if len(code) == 8:
        reservation_codes.add(code)

command_guest = input()
while command_guest != "END":
    if command_guest in reservation_codes:
        reservation_codes.discard(command_guest)

    command_guest = input()
print(len(reservation_codes))
print('\n'.join(sorted(reservation_codes)))