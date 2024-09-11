class memorization_fibo:
    print('fibo function')
    print('test')
    def __init__(self, rn):
        self.rn = rn

    def fibo(self,n, memo = {}):
        if n in memo:
            return memo[n]
        elif n<=1:
            return n
        memo[n] = self.fibo(n-1, memo) + self.fibo(n-2, memo)
        return memo[n]

    def fibo_series(self):
        for i in range(self.rn):
            print(self.fibo(i))

obj = memorization_fibo(10)
obj.fibo_series() 