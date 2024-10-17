def translate_to_robber_lang(s):
    a=['a','e', 'i', 'o', 'u']
    k=[]

    for y in s:
        for j in a:
            if y==' ' or y=='!':
                k.append(y)
                break
            elif y.lower() in a:
                k.append(y)
                break
            else:
                if y is not a:
                    k.append(y+'o'+y)
                break
        continue
    return ''.join(k)

print(translate_to_robber_lang("This is kinda fun"))