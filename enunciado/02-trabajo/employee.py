# declaramos la clase persona
class Person:
    # declaramos el metodo __init__ 
    def __init__(self, nombre, edad, apellido, numero):
        self.nombre=nombre
        self.edad=edad
        self.apellido=apellido
        self.numero=numero

 
    #Devuelve una lista con el nombre y la edad
    #return ["Claudio", 32]
    def get_person(self):
        print(self.__dict__)
        return self.__dict__
 
 
# declaramos la clase Employee
# la clase empleado hereda los atributos y metodos de la clase Persona
class Employee(Person):
    # declaramos el metodo __init__ para Employee
    def __init__(self, nombre, edad, apellido, numero, salario):
        # llamamos al metodo init de la clase padre
        Person.__init__(self, nombre, edad, apellido, numero)
        #ingresamos salary para employee
        self.salario=salario

    #Devuelve una lista con los atributos
    #return ["Claudio", 32, 30000]
    def get_employee(self):
       return self.__dict__

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    # return "Paga impuestos" or "No paga impuestos"
    def pay_tax(self):
        if self.salario > 30000 and self.edad < 32:
            return "Paga impuestos"
        else:
            return "No paga impuestos"
