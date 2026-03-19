def make_sandwich(*items_on_sandwich):
    print(items_on_sandwich)
    orders["make_sandwich"] = items_on_sandwich
    return make_sandwich


make_sandwich("greenchilli", "redchilli")


for sandwich in items_on_sandwich:
    print(f"\t They have ordered :{make_sandwich}")
