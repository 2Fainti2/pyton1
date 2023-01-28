class animal:
        def __init__(self,name):
                self.name = name
                self.legs = 4
                self.body = 1
        def run(self):
                print(self.name,"runing")
        def jump(self):
                print(self.name,"jumping")

class dog(animal):
        def __init__(self,name):
                self.claws= 20
                
                
        





obj1 = animal('animal')
obj1.run()
obj1.jump()