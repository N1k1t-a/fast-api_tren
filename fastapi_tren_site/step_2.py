from typing import Optional


def process_items(items: list[str]) -> None:
    for item in items:
        print(repr(item.upper()))


my_list = ["Абоба", "мармелад", "ниикта"]


process_items(my_list)

# конечно же ничего плохого не произойдет, если передать число, но так яснее хотя бы


def process_items_set_tuple(items_set: set[int], items_tuple: tuple[int, str, int]):
    return items_tuple, items_set


item_tuple, item_set = process_items_set_tuple(items_tuple=(12, 'total', 3), items_set={12, 4, 12, 21})

print(item_tuple, item_set)


def process_items_dict(prices: dict[str, float]) -> None:
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


prices = {
    "apple": 1.2,
    "banana": 0.8,
    "cherry": 2.5
}

process_items_dict(prices)


# Вы также можете использовать Optional, чтобы объявить, что переменная имеет тип,
# например, str, но это является «необязательным», что означает, что она также может
# быть None:

# from typing import Optional


def say_hi(name: Optional[str] = None) -> None:
    if name is not None:
        print(f"hi, {name}!")

    else:
        print("хело мир, манера крутит мир")


say_hi("Nikita")

