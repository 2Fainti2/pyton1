from random import randint
class Student:
        def __init__(self, name):
                self.name = name
                self.gladness = 0
                self.progress = 0
                self.many = 1000
                self.alive = True
        def work(self):
                self.many += 100
                self.gladness -= 10
                self.progress += 10
                print('work')
        def study(self):
                self.many -=30
                self.progress += 20
                self.gladness -= 10
                print('Study time')
        def chill(self):
                self.many -= 250
                self.gladness += 35
                self.progress -= 8
                print('Chill time')
        def sleep(self):
                self.gladness += 4
                print('Sleep time')
        def say_hello(self):
                print('Hello!')
        def exam(self):
                self.progress += 30
                self.gladness -= 15
                self.many -= 100
                print('work on the exam')
        def live(self):
                live_cube = randint(1,6)
                if live_cube == 1:
                        self.study()
                elif live_cube == 2:
                        self.chill()
                elif live_cube == 3:
                        self.sleep()
                elif live_cube == 6:
                        self.work()
                elif live_cube == 4:
                        self.say_hello()
                elif live_cube == 5:
                        self.exam()
                        self.final()
        def final(self):
                if self.progress == 100:
                        print('Amazing! You graduated!')
                        self.alive = False
                elif self.progress < -20:
                        print('Too bad... You are stupid')
                        self.alive = False
                elif self.gladness < -20:
                        print('Depression :(')
                        self.alive = False
class pet:
        def __init__(self,name):
                self.name = name
                self.eating = 0
        def eat(self,human):
                self.eating += 20
                print(self.name, "eat",)
                
        def final(self):
                if self.eating == 100:
                        print('eat good')
                        self.alive = False        
class human:
	def __init__(self,title):
			self.title = title
			self.eat_pet="None"
	def eat(self,pet):
			print(pet.name,"eat")
                

print('Bob\'s life')
obj1 = Student('Bob')
for i in range(365):
	if obj1.alive == False:
		break
	obj1.live()

print('Jane\'s life')
obj2 = Student('Jane')
for i in range(365):
	if obj2.alive == False:
		break
	obj2.live()

pet1 = pet('Bobby')
human1 = human('John')
pet1.eat(human1)
human1.eat(pet1)



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
                super().__init__(name)
                self.tail= 1
        def barks(self):
                print(self.name,"barks")
class cat(animal):
        def __init__(self,name):
                super().__init__(name)
                self.claws= 20
        def scratches(self):
                print(self.name,"scratches") 
class hamster(animal):
        def __init__(self,name):
                super().__init__(name)
                self.nose= 1
        def eats(self):
                print(self.name,"eats")                 
                


        





obj1 = animal('animal')
obj1.run()
obj1.jump()
obj2 = dog("dog")
obj2.run()
obj2.jump()
obj2.barks()
obj3 = cat("cat")
obj3.run()
obj3.jump()
obj3.scratches()
obj4 = hamster("hamster")
obj4.run()
obj4.jump()
obj4.eats()



class Man:
        def __init__(self,name):
                self.name = name
                self.legs = 2
                self.body = 1
                self.Hands = 2
        def go(self):
                print(self.name,"going")
        def jump(self):
                print(self.name,"jumping")

class teacher (Man):
        def __init__(self,name):
                super().__init__(name)
                self.Weight= 70
        def teach(self):
                print(self.name,"teach")
        def work(self):
                print(self.name,"work")
                
class Disciple (Man):
        def __init__(self,name):
                super().__init__(name)
                self.growth = 160
        def Learning(self):
                print(self.name,"Learning")
        def play(self):
                print(self.name,"play")                
             
                


        





obj5 = Man('Man')
obj5.go()
obj5.jump()
obj6 = teacher("teacher")
obj6.go()
obj6.jump()
obj6.teach()
obj6.work()
obj7 = Disciple("Disciple")
obj7.go()
obj7.jump()
obj7.Learning()
obj7.play()
