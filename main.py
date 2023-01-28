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
                self.eat = 0
        def eat(self,human):
                self.eat += 20
                print(self.name, "eat", human.title)
                
        def final(self):
                if self.eat == 100:
                        print('eat good')
                        self.alive = False        
class human:
        def __init__(self,title):
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
        