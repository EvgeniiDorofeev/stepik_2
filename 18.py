def print_results(m):
    temp_list = sorted(m, key=lambda x: int(x[1]), reverse=True)
    for i in temp_list:
        print(i[0], i[1])

marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
print_results(marks)