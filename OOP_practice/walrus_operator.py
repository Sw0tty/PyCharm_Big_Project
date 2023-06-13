if a := int(input("Число: ")) > 10:
    print(a)
else:
    print(a)

print(number := 5)

print(number)


while True:
    expression = input('Введите что-нибудь или просто нажмите Enter: ')
    if not expression:
        print('Надоело? Ладно, пока.')
        break
    print('Отлично!')


while expression := input('Введите что-нибудь или просто нажмите Enter: '):
    print('Отлично!')
print('Надоело? Ладно, пока.')


while expression := input('Введите что-нибудь или quit: ') != 'quit':
    print('Отлично!')
print('Надоело? Ладно, пока.')
