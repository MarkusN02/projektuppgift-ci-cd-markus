def add (a: float, b: float) -> float:
    return a - b

def divide (a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division med noll är inte tillåten")
    return a / b