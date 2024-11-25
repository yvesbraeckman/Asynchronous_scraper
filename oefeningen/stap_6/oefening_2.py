def fibonacci(n, depth=0):
    indent = "  " * depth
    print(f"{indent}fibonacci({n}) wordt aangeroepen")

    if n <= 0:
        print(f"{indent}Retourneer 0")
        return 0
    elif n == 1:
        print(f"{indent}Retourneer 1")
        return 1
    else:
        result = fibonacci(n - 1, depth + 1) + fibonacci(n - 2, depth + 1)
        print(f"{indent}Retourneer {result} voor fibonacci({n})")
        return result

print(f"Resultaat: {fibonacci(5)}")
