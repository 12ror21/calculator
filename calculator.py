def solve(a: int, b: int, op: str) -> [int, float]:
    conv = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b,
        "^": a ** b,
        "%": a % b,
        "//": a // b
    }
    return conv.get(op, f"No such operation `{op}`!")
