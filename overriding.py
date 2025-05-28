

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def move(self):
        return f"{self.name} moves"

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    
    def speak(self):  
        return f"{self.name} makes a mammalian sound"
    
    def breathe(self):
        return f"{self.name} breathes air"

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span
    
    def speak(self):  
        return f"{self.name} chirps"
    
    def fly(self):
        return f"{self.name} flies with {self.wing_span}cm wingspan"

class Bat(Mammal, Bird):  
    def __init__(self, name, fur_color, wing_span):
        
        Mammal.__init__(self, name, fur_color)
        self.wing_span = wing_span
    
    def speak(self):  
        return f"{self.name} squeaks"
    
    def echolocate(self):
        return f"{self.name} uses echolocation"


animal = Animal("Generic Animal")
dog = Mammal("Rex", "brown")
parrot = Bird("Polly", 25)
bat = Bat("Bruce", "black", 30)

print(f"Animal: {animal.speak()}")
print(f"Dog: {dog.speak()}")  
print(f"Parrot: {parrot.speak()}")  
print(f"Bat: {bat.speak()}")  

print("\n=== Method Resolution Order (MRO) ===")
print(f"Bat MRO: {Bat.__mro__}")
print(f"Bat MRO (names): {[cls.__name__ for cls in Bat.__mro__]}")


print(f"\nBat calling move(): {bat.move()}")  
print(f"Bat calling breathe(): {bat.breathe()}")  
print(f"Bat calling fly(): {bat.fly()}")  


print(f"\nMethod resolution:")
print(f"bat.speak is from: {bat.speak.__func__.__qualname__}")
print(f"bat.breathe is from: {bat.breathe.__func__.__qualname__}")
print(f"bat.fly is from: {bat.fly.__func__.__qualname__}")


class FlyingMammal(Mammal, Bird):
    def __init__(self, name, fur_color, wing_span):
        super().__init__(name, fur_color)  
        self.wing_span = wing_span
    
    def speak(self):
        
        mammal_sound = super().speak()
        return f"{mammal_sound} and also flies"

flying_squirrel = FlyingMammal("Glider", "gray", 15)
print(f"\n=== Super() with MRO ===")
print(f"Flying Squirrel: {flying_squirrel.speak()}")
print(f"FlyingMammal MRO: {[cls.__name__ for cls in FlyingMammal.__mro__]}")