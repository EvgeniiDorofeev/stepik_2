tables = {
    1: 'Andrey',
    2: None,
    3: 'Gena',
    4: 'Artem',
    5: 'Vasiliy',
    6: None,
    7: 'Artur',
    8: None,
    9: 'Misha',
}
def is_table_free(n):
    if tables[n]==None:
        return True
    return False
def reserve_table(a,b):
    if is_table_free(a)==True:
        tables[a]=b
def delete_reservation(q):
    tables[q]=None
print(tables)
delete_reservation(1)
delete_reservation(3)
reserve_table(6, 'Chubaka')
print(tables)