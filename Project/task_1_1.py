import sys

print('Версия Python:', sys.version.split()[0])
print('Интерпретатор:', sys.executable)
print('Количество путей поиска:', len(sys.path))
for p in sys.path[:4]:
    print('  ', p)

import math, random
print('math.pi =', math.pi)
print('random.random() =', random.random())

mods = sorted(sys.modules)
print('Всего загружено модулей:', len(mods))
print('Пример:', mods[:5])

public = [n for n in dir(math) if not n.startswith('__')]
print('Публичных имён в math:', len(public))
print('Первые 8:', public[:8])

print('Мой __name__=', __name__)

#вопросы для самопроверки