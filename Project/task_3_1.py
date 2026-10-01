import math

print("=== Константы ===")
print("math.pi =", math.pi)
print("math.e =", math.e)

print("math.tau =", math.tau, "(tau = 2*pi)")
print("math.inf =", math.inf, ", -math.inf =", -math.inf, ", math.nan =", math.nan)

print("\n=== Округления (в чём разница?) ===")
x = 7.6
print("math.floor(x) =", math.floor(x), "(вниз)")
print("math.ceil(x) =", math.ceil(x), "(вверх)")
print("round(x) =", round(x), "(банковское округление)")
print("math.trunc(x) =", math.trunc(x), "(отбрасывание дробной части)")
print("round(2.5) =", round(2.5), ", round(3.5) =", round(3.5), "<- почему по-разному?")

print("\n=== Степени, корни, логарифмы ===")
print("math.sqrt(144) =", math.sqrt(144))
print("math.pow(2,10) =", math.pow(2, 10), "(всегда float)")
print("2 ** 10 =", 2 ** 10, "(int, точное)")
print("math.exp(1) =", math.exp(1))
print("math.log(1024, 2) =", math.log(1024, 2))
print("math.log10(1000) =", math.log10(1000))
print("math.log2(1024) =", math.log2(1024))

print("\n=== Факториал, НОД, НОК, комбинаторика ===")
print("math.factorial(10) =", math.factorial(10))
print("math.gcd(48, 180) =", math.gcd(48, 180))
print("math.lcm(4, 6) =", math.lcm(4, 6))
print("math.comb(10, 3) =", math.comb(10, 3), "(сочетания)")
print("math.perm(10, 3) =", math.perm(10, 3), "(размещения)")
print("math.isqrt(50) =", math.isqrt(50), "(целый корень)")

print("\n=== Точность вещественных чисел ===")
print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)
print("math.isclose(0.1+0.2, 0.3) =", math.isclose(0.1 + 0.2, 0.3))
print("math.fsum([0.1]*10) =", math.fsum([0.1]*10), "vs sum() =", sum([0.1]*10))
print("math.copysign(5, -1) =", math.copysign(5, -1))

print("\n=== Дежурные (comb vs perm) ===")
n = 12
k = 3
ways_choose = math.comb(n, k)
ways_arrange = math.perm(n, k)
print("Способов выбрать 3 дежурных из 12 (сочетания):", ways_choose)
print("Способов расставить 3 дежурных по позициям (размещения):", ways_arrange)
