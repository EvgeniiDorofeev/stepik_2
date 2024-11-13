tables = {
  1: 'Andrey',
  2: None,
  3: None,
  4: None,
  5: 'Vasiliy',
  6: None,
  7: None,
  8: 'Stas',
  9: None,
}
def is_table_free(n):
    if tables[n]==None:
        return True
    return False
def get_free_tables():
    a=[]
    for i in tables:
        if tables[i]==None:
            a.append(i)
    return a
print(is_table_free(1))
print(is_table_free(2))
print(get_free_tables())