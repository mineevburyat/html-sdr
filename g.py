def gen_x():
    num = 1
    while num < 5:
        if num % 2 == 0:
            yield num
        num += 1

print(next(gen_x()))
print(next(gen_x()))