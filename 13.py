check_word = lambda x: x.upper().startswith(('Q','R')) and x.upper().endswith(("A", "E", "O", "I", "U"))


print(check_word.__name__)
print(check_word('radio'))