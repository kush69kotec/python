# вариант с использованием list comprehensions
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [src[i] for i in range(len(src)) if src.count(src[i]) == 1]
print(result)

# вариант с использованием генератора и поочередным закреплением его элементов в список
gen = (src[i] for i in range(len(src)) if src.count(src[i]) == 1)
result = []
while True:
    try:
        result.append(next(gen))
    except Exception:
        break
print(result)
