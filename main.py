import sys

def power_sum(arr):
    if not arr:
        return 0
    first = arr[0]
    if first < 0:
        return (first ** 4) + power_sum(arr[1:])
    return power_sum(arr[1:])

def process_cases(cases):
    if not cases:
        return
    
    x, arr = cases[0]
    
    if x != len(arr):
        print(-1)
    else:
        print(power_sum(arr))
    
    process_cases(cases[1:])

def read_cases(lines, index, n):
    if n == 0:
        return []
    
    x = int(lines[index])
    arr = list(map(int, lines[index + 1].split()))
    
    return [(x, arr)] + read_cases(lines, index + 2, n - 1)

def main():
    n = int(input())
    cases = []

    for _ in range(n):
        x = int(input())
        arr = list(map(int, input().split()))
        cases.append((x, arr))

    process_cases(cases)

if __name__ == "__main__":
    main()