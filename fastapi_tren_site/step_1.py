# : str - это называется аннотации типов. Это позволяет нам при написании "." после
# переменной смотреть варианты с помощью "ctrl" + "space",
# что мы можем с ней сделать, да и просто так поприятней
def get_full_name(first_name: str,last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


full_title_name = get_full_name(first_name="abricos", last_name="dayn")
print(full_title_name)
