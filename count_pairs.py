t = int(input())


def total_indices(a, l, r):
    count = 0
    real_count = 0
    n = len(a)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            sum = a[i] + a[j]
            if l <= sum <= r:
                count += 1
                real_count = int(count / 2)

    print(real_count)


for k in range(t):
    input_str = input().split()
    n = int(input_str[0])
    l = int(input_str[1])
    r = int(input_str[2])
    a = input().split()
    for p in range(n):
        a[p] = int(a[p])
    total_indices(a, l, r)
