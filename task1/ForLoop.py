import random

rolls = [random.randint(1, 6) for _ in range(20)]
count_6 = rolls.count(6)
count_1 = rolls.count(1)

count_two_sixes_in_a_row = sum(1 for i in range(len(rolls) - 1) if rolls[i] == 6 and rolls[i + 1] == 6)

print(f"Number of times rolled 6: {count_6}")
print(f"Number of times rolled 1: {count_1}")
print(f"Number of times two 6s were rolled in a row: {count_two_sixes_in_a_row}")
