class FruitBox:
    def __init__(self, apples, oranges):
          
        if type(apples) == int:
            self.apples = apples
        if type(oranges) == int:
            self.oranges = oranges
        if type(apples) != int or type(oranges) != int:
            print("\n ERROR \n")
        if (self.apples + self.oranges) >= 50:
            self.apples = False
            self.oranges = False
            print ("\n FULL BOX \n")

    def __add__(self, other):
        total_apples = self.apples + other.apples          
        total_oranges = self.oranges + other.oranges          
        return f"\n Total apples: {total_apples}, Total oranges: {total_oranges}\n"

    def __str__(self):
        return f"\n Apples: {self.apples}, Oranges: {self.oranges}\n"
       
box1 = FruitBox(10,20)  
box2 = FruitBox(15,10)
box3 = box1 + box2

print(box1.__str__())

print (box2.__str__())

print (box3)




