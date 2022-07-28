class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)    #加self 是定义在类里面的函数，就算调用自己也要用self
                                                #不能用fib(n) =  fib(n-1) + fib(n-2) 原因是：函数不能被赋值，只能被调用
