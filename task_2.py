number_a, number_b, number_c, number_d = map(int, input().split())

print(sum(filter(lambda number: number % number_c == 0 and number % number_d == 0, range(number_a, number_b + 1))))
