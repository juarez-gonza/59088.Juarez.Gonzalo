                ***** Employee *******
- Implementar Unitest para Person, 
 * crear un objeto person y comprobar la funcion get_person la cual devuelve una lista con los datos ingresados en person 
   ejemplo ["Claudio", 32] ---> [<name>, <age>]  
   
   guia:
   - def test_get_person(self)

-Implementar Unitest para Employee la cual hereda de Person,
 * crear un objeto employee y comprobar la funcion get_employee la cual devuelve una lista con los datos ingresados en employee 
   ejemplo ["Claudio", 32, 3000] ---> [<name>, <age>, <salary>]    
 * unitest para pay_tax, comprueba si el empleado tiene menos de 32 años y cobra mas de 3000 paga impuestos
implementar dos casos, cuando paga impuestos y cuando no pata impuestos.
  
    guia:
    - test_get_employee(self):
    - test_pay_tax_pay(self):
    - test_pay_tax_no_pay(self):