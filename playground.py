class TestClass():
    def test1(self):
        x = input('Enter a number: ')
        return int(x)
    
    def test2(self, squared):
        return squared ** 2


y = TestClass()

# print(y.test1(10))
z = y.test1()
print(y.test2(z))