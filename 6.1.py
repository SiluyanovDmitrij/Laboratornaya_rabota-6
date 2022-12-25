posled = input('Введите случайную скобочную последовательность через пробел: ').split()
a = []
b = []
f = False
for i in range(len(posled)):
    if posled[i] == '(':
        a.append(posled[i])
        b.append(i)
    if posled[i] == ')':
        if len(a) == 0:
            print('Неправильная ")" скобка в', i+1)
            f = False
            break
        if len(a) > 0:
            if a[-1] == '(':
                a.pop()
                b.pop()
if len(a) == 0 and f == False:
    print('Все скобки закрыты')
if len(a) > 0 and f == False:
    print('Скобка не закрылась в', b[-1])





