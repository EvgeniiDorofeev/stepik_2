
def count_words(a):
    k=0
    s=a.split()
    print(s)
    for i in s:
        k+=1
    return k
print(count_words('I like learn python'))