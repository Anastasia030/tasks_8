number_a, number_b, number_c, number_d = map(int, input().split())

print(sum(list(map(lambda x: 1 if x % number_c != 0 and x % 10 == number_d else 0, range(number_a, number_b + 1)))))