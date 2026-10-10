import sys, site

print("Исполняемый файл:", sys.executable)
print("Префикс       :", sys.prefix)
print("Базовый префикс:", sys.base_prefix)
print("В виртуальном окружении?", sys.prefix != sys.base_prefix)
print("site-packages :", site.getsitepackages())
