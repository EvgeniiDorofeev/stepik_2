def print_results(m):
    a = sorted(m, key=lambda x: x[0].lower(), reverse=False)
    temp_list = sorted(a, key=lambda x: int(x[1]), reverse=True)
    for i in temp_list:
        print(i[0], i[1])
#rerere
marks = [('english', 100), ('Science', 100), ('maths', 100),
         ('Physics', 100), ('history', 100), ('Music', 100)]
print_results(marks)