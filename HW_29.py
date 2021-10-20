a = [int(s) for s in input('Введите пожалуйста список чисел: ').split()]
k = int(input('Введите пожалуйста индекс элемента в списке: '))
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))