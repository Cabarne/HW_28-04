class Title:
    def __init__ (self, name):
        self.name = name
    def __str__(self):
        return f"-= {self.name} =-"
           
nameTitle = Title ("Programming in Python 3")
print (nameTitle.__str__().upper())



