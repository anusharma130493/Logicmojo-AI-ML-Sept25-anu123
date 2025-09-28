class animal:
  def __init__(self,name):
     self.name =name

  def speak(self):
    return f"{self.name} in animal class"  

class dog(animal):
  def speak(self):
    print(f"{self.name} dogClass")

d=dog("buddy")   
d.speak() 