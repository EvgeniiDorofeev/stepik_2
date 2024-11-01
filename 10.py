tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}


def is_table_free(n):
    if tables[n] == None:
        return True
    return False


def reserve_table(a, b, c):
    if is_table_free(a) == True:
        tables[a]={}
        tables[a]['name'] = b
        tables[a]['is_vip'] = c

def delete_reservation(q):
    tables[q]=None


print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)
