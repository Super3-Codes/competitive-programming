def run_test_case():
    n = int(input())
    out = [0] * n
    in_degree = [0] * n
    sink = 0
    source = 0

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            u = row[j]
            if u == 1:
                in_degree[j] += 1
                out[i] += 1

    for i in range(n):
        if in_degree[i] == 0:
            source += 1
        if out[i] == 0:
            sink += 1

    print(source, end=" ")
    for i in range(n):
        if in_degree[i] == 0:
            print(i + 1, end=" ")
    print()

    print(sink, end=" ")
    for i in range(n):
        if out[i] == 0:
            print(i + 1, end=" ")
    print()


test = 1
# test = int(input())
while test > 0:
    run_test_case()
    test -= 1
