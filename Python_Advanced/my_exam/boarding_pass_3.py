def boarding_passengers(capacity, *args):
    capacity = int(capacity)
    total_guests = 0
    boarding_dict = {}
    result = ""

    for passengs, my_benefits in args:
        passengs = int(passengs)

        if capacity > 0:
            if capacity >= passengs:
                total_guests += passengs
                capacity -= passengs

                if my_benefits not in boarding_dict:
                    boarding_dict[my_benefits] = 0
                boarding_dict[my_benefits] += passengs

            else:
                continue
        else:
            break

    sorted_board_dict = dict(sorted(boarding_dict.items(), key= lambda x: (-x[1], x)))

    result += f"Boarding details by benefit plan:\n"
    for curr_benefit, my_num in sorted_board_dict.items():
        result += f"## {curr_benefit}: {my_num} guests\n"
    if total_guests == sum(x[0] for x in args):
        result += "All passengers are successfully boarded!"
        return result.strip()
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
        return result.strip()
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."
        return result.strip()




print(boarding_passengers(150,
                          (35, 'Diamond'),
                          (55, 'Platinum'),
                          (35, 'Gold'),
                          (25, 'First Cruiser')))


print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))


