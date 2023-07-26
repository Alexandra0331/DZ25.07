# 1.Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


from collections import Counter
my_list = ['g', 2, 3, 'g', 2, 4, 5] #[1, 2, 3, 1, 2, 4, 5]
counter = Counter(my_list)
duplicates = [element for element, count in counter.items() if count > 1]
print(duplicates)
