class Orange():
    def __init__(self,w,c):
        """Weightz are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("created!")

    def rot(self, days, temp): # this is a method as it's a function inside of a class
        self.mold = days * temp


orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

