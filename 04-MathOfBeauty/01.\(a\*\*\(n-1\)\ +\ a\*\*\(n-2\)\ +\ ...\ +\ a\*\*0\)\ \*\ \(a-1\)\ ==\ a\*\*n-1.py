def cc(a, n):
    sum = 0
    for i in range(n):
      sum += a**i
    print(sum*(a-1), (a**n-1))

cc(2, 5)
