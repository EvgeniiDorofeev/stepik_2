def get_reverse(a):
    b=[]
    for i in a[::-1]:
        b.append(i)
    return (''.join(b))
print(get_reverse("I am testing string"))