def get_sort_lines(a):
    b=sorted(a, key=lambda x: x[1], reverse=False)
    c=sorted(b, key=lambda x: x[0], reverse=False)
    return sorted(c, key=lambda x: abs(x[1]-x[0]), reverse=False)


lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))

