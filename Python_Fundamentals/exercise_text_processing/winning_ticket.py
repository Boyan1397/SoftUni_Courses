def check_ticket(my_ticket):
    if len(my_ticket) != 20:
        return "invalid ticket"
    else:
        left_half = my_ticket[:10]
        right_half = my_ticket[10:]
        special_symbols = '@', '#', '$', '^'
        for symbol in special_symbols:
            for uninterruptedly_repeated in range(10,5,-1):
                current_repeated_symbols = symbol * uninterruptedly_repeated
                if current_repeated_symbols in left_half and current_repeated_symbols in right_half:
                    if len(current_repeated_symbols) == 10:
                        return f'ticket "{my_ticket}" - {uninterruptedly_repeated}{symbol} Jackpot!'
                    elif len(current_repeated_symbols) != 10:
                        return f'ticket "{my_ticket}" - {uninterruptedly_repeated}{symbol}'
        return f'ticket "{my_ticket}" - no match'


tickets = [element.strip() for element in input().split(", ")]
for ticket in tickets:
    print(check_ticket(ticket))