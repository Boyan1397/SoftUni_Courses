def boarding_passengers(capacity, *args):
    capacity = int(capacity)
    my_dict = {}
    total_guests = 0
    output = ""

    for passengers, benefits_type in args:
        passengers = int(passengers)
        if capacity > 0:
            if capacity >= passengers:
                total_guests += passengers
                capacity -= passengers
                if benefits_type not in my_dict:
                    my_dict[benefits_type] = 0
                my_dict[benefits_type] += passengers
            else:
                continue
        else:
            break


    sorted_dict = dict(sorted(my_dict.items(), key= lambda x: (-x[1], x)))

    output += f"Boarding details by benefit plan:\n"
    for benefit, number in sorted_dict.items():
        output += f"## {benefit}: {number} guests\n"
    if total_guests == sum(x[0] for x in args):
        output += "All passengers are successfully boarded!"
        return output.strip()
    elif capacity == 0:
        output += "Boarding unsuccessful. Cruise ship at full capacity."
        return output.strip()
    else:
        output += f"Partial boarding completed. Available capacity: {capacity}."
        return output.strip()