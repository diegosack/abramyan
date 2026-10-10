import random

EVENTS = [
    ("Микрометеорит пробил обшивку",     -15, 0.4),
    ("Солнечная вспышка: радиация",      -10, 0.2),
    ("Удачная коррекция курса",           +5, 0.2),
    ("Найдены запасы предыдущей миссии", +20, 0.1),
    ("Отказ системы охлаждения",         -25, 0.1),
]

def random_event(seed=None):
    """(описание, изменение ресурса) — случайное событие с весами."""
    rnd = random.Random(seed)
    names, weights, deltas = [e[0] for e in EVENTS], [e[2] for e in EVENTS], [e[1] for e in EVENTS]
    ch = rnd.choices(EVENTS, weights=weights, k=1)[0]
    return ch[0], ch[1]
