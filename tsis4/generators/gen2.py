def even_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


n = int(input())
evens = even_generator(n)
print(','.join(str(even) for even in evens))
