                ***** Administation *******
- Imprementar Unitest para Administration, 
 * Comprobar que listEmployee tiene agregado el Employee en el legajo correspondiente. Utilizando parameterized
   ej :
   {
    0: {'name': 'Claudio', 'surname': 'Pico', 'age': 30, 'phone': 155858585,salary:30000}, 
    1: {'name': 'Nicolas', 'surname': 'Pico', 'age': 30, 'phone': 155858585,salary:20000}
    }

   guia:
   - def test_add_employee(self, name, surname, age, phone, legajo)
