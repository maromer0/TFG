lst = input("shopping list: ")
print(lst.replace(',', '\n'))
print('\n'.join(lst.split(',')))
for i in lst:
    if (i == ','):
        article = lst[:lst.find(',')]
        lst = lst[lst.find(',') + 1:]
        print(article)
print(lst)