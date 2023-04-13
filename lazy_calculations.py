import time

print('__iter__' in dir(range))

# Вариант 1
generator1 = (time.sleep(x) for x in range(3))
def sleep():
    for x in range(3):
        yield time.sleep(x)


# Вариант 2
generator2 = sleep()





