from typing import List, Optional

def get_first_repeated_word(words:List[str])->Optional[str]:
    'Находит первый дубль в списке'
    a=[]
    for i in words:
        if i in a:
            return i
        a.append(i)




print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(['hello', 'hi', 'hello']))


