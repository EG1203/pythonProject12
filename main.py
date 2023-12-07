### N1
def max_even_number(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    return max(even_numbers) if even_numbers else None

arr = (17, 71, 79,  2,  1, 46, 57, 62,  3, 56, 13, 21, 11,  4, 12, 62, 57, 69, 89, 41)  # кортеж
max_even = max_even_number(arr)

### N2
def symmetric_rows(matrix):
    return [int(row == row[::-1]) for row in matrix]

matrix = (
    (7, 9, 5, 1, 2),
    (6, 3, 3, 5, 8),
    (2, 6, 5, 3, 5),
    (6, 6, 5, 1, 7),
    (9, 3, 2, 3, 4)
)
symmetry_result = symmetric_rows(matrix)

### N3
def remaining_pins(n, throws):
    pins = ['I'] * n
    for l, r in throws:
        for i in range(l - 1, r):
            pins[i] = '.'
    return ''.join(pins)

n = 10
throws = [(2, 4), (5, 7)]
pins_result = remaining_pins(n, throws)


### N4
def count_families(newspaper, journal, both):
    newspaper_set = set(range(newspaper))
    journal_set = set(range(journal))
    both_set = set(range(both))
    unique_families = (newspaper_set | journal_set) - both_set
    return len(unique_families)

newspaper = 75
journal = 27
both = 13
families_count = count_families(newspaper, journal, both)

### N5
cube_dict = {num: num**3 for num in range(1, 11)}

