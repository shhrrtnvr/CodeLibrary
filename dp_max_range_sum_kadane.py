def kadane(a):
    sum, ans = 0, 0
    for val in a:
        sum += val
        ans = max(ans, sum)
        if sum < 0:
            sum = 0
    return ans

if __name__ == '__main__':
    A = [1, 2, 5, -6, 3, 8, -4, 1]
    g = (A[i] for i in range(1, 5))
    print(kadane(g))