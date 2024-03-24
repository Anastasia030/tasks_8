import json

numbers = input()

answer = json.loads(numbers)
print(sorted(answer.items(), key=lambda item: item[1][1], reverse=True))
