from calculator import solve

def main():
    try:
        a, op, b = map(lambda x: int(x) if x.isnumeric() else x, input().split())
        print(solve(a, b, op))
    except:
        print("Wrong input format, ex. `2 + 2`")

if __name__ == "__main__":
    main()
