def grocery_store(**kwargs):

    sorted_receipt = sorted(kwargs.items(),key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    sorted_receipt = "\n".join([f"{name}: {quantity}" for name, quantity in sorted_receipt])
    return sorted_receipt


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
