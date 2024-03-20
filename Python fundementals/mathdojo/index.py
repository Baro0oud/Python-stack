class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# create an instance:
md = MathDojo()

# Test add method
x = md.add(2).add(2, 5, 1).add(10).result
print(x)  # should print 20

# Test subtract method
y = md.subtract(3).subtract(2, 1).subtract(5).result
print(y)  # should print 9
