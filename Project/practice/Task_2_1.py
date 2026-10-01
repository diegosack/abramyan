import random

random.seed(42)
print("random()                 :", round(random.random(), 6))
print("uniform(1, 10)           :", round(random.uniform(1, 10), 3))
print("randint(1, 6)            :", random.randint(1, 6))
print("randrange(0, 100, 5)     :", random.randrange(0, 100, 5))


print("\n--- Статистика 10000 бросков одного кубика ---")
random.seed(2026)
counts = {i: 0 for i in range(1, 7)}
N = 10_000
for _ in range(N):
    counts[random.randint(1, 6)] += 1

for face, cnt in sorted(counts.items()):
    bar = "#" * (cnt // 50)
    print(f"{face}: {cnt:5d} ({cnt / N * 100:5.2f}% | Отклонения: {round(cnt / N * 100- 16.67, 2)}%) {bar}")
