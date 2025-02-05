from abc import  abstractmethod
# La herencia multiple, es capacidad de una clase de hererdad de mas de una clase, 
#   La herencia multiple puede servir para:
#     Reutilizacion de codigo: Evita la repeticion del codigo,
#     Creacion de Mixins: Que es una clase que no tiene sentido por si sola, pero que puede ser util para otras clases.
#     Modelado de relaciones complejas: Permite modelar objetos que comparten caracteristicas de clases distintas.
#     Extension de funcionalidades: Puede combinar funcionalidades de distintas clases sin necesidad de modificar su implementacion original.

# Ejemplo


class SpeakHability:
    @abstractmethod
    def speak(self,message):
        print(message)


class WalkHability:
    @abstractmethod
    def walk(self,name,direction):
        print(f"{name} is moving to {direction}")


class Robot(SpeakHability,WalkHability):
    def __init__(self,name):
        self.name = name
    def presentation(self):
        print(f"Hello, my name is {self.name}")

robot = Robot("R2D2")
robot.presentation()

robot.speak("Hello, I'm here to help you:")
robot.walk(robot.name,"Right")
