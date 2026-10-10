import math

def word_count(text: str) -> int:
    """Число слов в тексте."""
    return len(text.split())

def char_stats(text: str) -> dict:
    """Базовая статистика символов + информационная энтропия Шеннона."""
    letters = [c for c in text if c.isalpha()]
    n = len(text)
    entropy = -sum(text.count(c) / n * math.log2(text.count(c) / n)
                   for c in set(text)) if n else 0
    return {"всего": n, "букв": len(letters),
            "уникальных": len(set(c.lower() for c in letters)),
            "энтропия": round(entropy, 3)}