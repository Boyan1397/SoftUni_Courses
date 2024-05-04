my_dict = {}
some_names_and_ids = input().split(" -> ")

while some_names_and_ids[0] != "End":
    company_name, employee_id = some_names_and_ids[0], some_names_and_ids[1]
    if company_name not in my_dict.keys():
        my_dict[company_name] = []
    if employee_id not in my_dict[company_name]:
        my_dict[company_name].append(employee_id)

    some_names_and_ids = input().split(" -> ")

for name, some_ids in my_dict.items():
    print(name)
    for ids in some_ids:
        print(f"-- {ids}")