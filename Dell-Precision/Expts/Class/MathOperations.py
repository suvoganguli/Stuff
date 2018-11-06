class MathOperations:
    def testAddition (self,x, y):
        return x + y

    def testMultiplication (self,a, b):
        return a * b

tmp = MathOperations()
print tmp.testAddition(2,3)





class MathsOperations2:
    def __init__ (self, x, y):
        self.a = x
        self.b = y
    def testAddition (self):
        return (self.a + self.b)

    def testMultiplication (self):
        return (self.a * self.b)

tmp2 = MathsOperations2(1,2)
print tmp2.testAddition()




class MathsOperations3:
    def testAddition (self, x, y):
        return x + y

    def testMultiplication (self, x, y):
        return x * y

    def otherMath (self, a, b, c, d):
        e = self.testAddition(a, b) + self.testMultiplication(c, d)
        return e

tmp3 = MathsOperations3()
print tmp3.otherMath(1,2,3,4)

