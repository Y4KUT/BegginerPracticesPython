class Animal():
    def __init__(self,name="empty",age=0,height=0,weight=0):
        print("Animal init funct. running")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def showinfo(self):
        print("Animal's information...")
        print("Name: {} \nAge: {} \nHeight: {} \nWeight: {}".format(self.name,self.age, self.height,self.weight))


class Dog(Animal):
    def __init__(self,name,age,height,weight,dog_breed):
        super().__init__(name, age, height, weight)
        self.dog_breed = dog_breed

    def showinfo(self):
        print("Dog's information...")
        print("Name: {} \nAge: {} \nHeight: {} \nWeight: {} \nBreed: {}".format(self.name,self.age, self.height,self.weight,self.dog_breed))

    def attack(self):
        print("Order understanding by dog...")
        print("Dog attacked!!!")

    def change_name(self,new_name):
        self.name = new_name

    def change_weight(self,new_weight):
        self.weight = new_weight


class Cat(Animal):
    def __init__(self,name,age,height,weight,cat_breed):
        super().__init__(name,age,height,weight)
        self.cat_breed = cat_breed

    def showinfo(self):
        print("Cat's information...")
        print("Name: {} \nAge: {} \nHeight: {} \nWeight: {} \nBreed: {}".format(self.name,self.age, self.height,self.weight,self.cat_breed))

    def makesound(self):
        print("Meowww Meowww Meowww ^.^")

    def change_name(self,new_name):
        self.name = new_name

    def change_weight(self,new_weight):
        self.weight = new_weight


class Bird(Animal):
    def __init__(self,name,age,height,weight,bird_breed):
        super().__init__(name,age,height,weight)
        self.bird_breed = bird_breed

    def showinfo(self):
        print("Bird's information...")
        print("Name: {} \nAge: {} \nHeight: {} \nWeight: {} \nBreed: {}".format(self.name,self.age,self.height,self.weight,self.bird_breed))

    def talk(self):
        a = input("Write the word that you wanted to bird tells you: ")
        print("Cik cik", a)

    def change_name(self,new_name):
        self.name = new_name

    def change_weight(self,new_weight):
        self.weight = new_weight
while True:
    print(""" Welcome to the Animal Registeration Programme...
    
    Which animal do you want to register?
    
    Press 1 for Dogs
    Press 2 for Cats
    Press 3 for Birds
    Press anything else for quiting the system...


            """)
    a = int(input("Select one of the options: "))
    if a == 1:
        print("Please write your dog's informations...")
        dog_name = input("Dog's name: ")
        dog_age = input("Dog's age: ")
        dog_height = input("Dog's height: ")
        dog_weight = input("Dog's weight: ")
        dog_breed = input("Dog's breed: ")
        dog1 = Dog(dog_name,dog_age,dog_height,dog_weight,dog_breed)
        while True:
            print(""" Please select the option that you want to do...

            Press 1 to Display Dog's Information
            Press 2 to Attack the Dog
            Press 3 to Change the Dog's Weight
            Press 4 to Change the Dog's name
            Press anything else to quit from the system

            """)
            b = int(input("Select one of the options: "))
            if b==1:
                dog1.showinfo()
            elif b==2:
                dog1.attack()
            elif b==3:
                new_weight = input("Write the new weight of your dog: ")
                dog1.change_weight(new_weight)
            elif b==4:
                new_name= input("Write the new name of your dog: ")
                dog1.change_name(new_name)
            else:
                print("Quiting from the system...")
                break

    elif a == 2:
        print("Please write your cat's informations...")
        cat_name = input("Cat's name: ")
        cat_age = input("Cat's age: ")
        cat_height = input("Cat's height: ")
        cat_weight = input("Cat's weight: ")
        cat_breed = input("Cat's breed: ")
        cat1 = Cat(cat_name,cat_age,cat_height,cat_weight,cat_breed)
        while True:
            print(""" Please select the option that you want to do...
            Press 1 to Display Cat's Information
            Press 2 to Make the Cat Talk
            Press 3 to Change the Cat's name
            Press 4 to Change the Cat's weight
            Press anything else to quit from the system

            """)
            b = int(input("Select one of the options: "))
            if b == 1:
                cat1.showinfo()
            elif b == 2:
                cat1.makesound()
            elif b == 3:
                new_name = input("Write the new name of your cat: ")
                cat1.change_name(new_name)
            elif b == 4:
                new_weight = input("Write the new weight of your cat: ")
                cat1.change_weight(new_weight)
            else:
                print("Quiting from the system...")
                break

    elif a == 3:
        print("Please write your bird's informations...")
        bird_name = input("Bird's name: ")
        bird_age = input("Bird's age: ")
        bird_height = input("Bird's height: ")
        bird_weight = input("Bird's weight: ")
        bird_breed = input("Bird's breed: ")
        bird1 = Bird(bird_name,bird_age,bird_height,bird_weight,bird_breed)
        while True:
            print(""" Please select the option that you want to do...
            Press 1 to Display Bird's Information
            Press 2 to Make the Bird Talk
            Press 3 to Change the Bird's name
            Press 4 to Change the Bird's weight
            Press anything else to quit from the system
            """)
            b = int(input("Select one of the options: "))
            if b == 1:
                bird1.showinfo()
            elif b == 2:
                bird1.talk()
            elif b == 3:
                new_name = input("Write the new name of your bird: ")
                bird1.change_name(new_name)
            elif b == 4:
                new_weight = input("Write the new weight of your bird: ")
                bird1.change_weight(new_weight)

            else:
                 print("Quiting from the system...")
                 break

    else:
        print("Quiting from the system...")
        break
