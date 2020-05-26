import unittest
from employee import Person, Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.personTest = Person("Gonzalo", 19, "Juarez", 666)
        self.employeeTestArr = [
            Employee("Gonzalo", 19, "Juarez", 666, 20000), 
            Employee("X", 22, "Y", 666, 35000)
        ]

    def tearDown(self):
        self.personaTest = Person("Gonzalo", 19, "Juarez", 666)
        self.employeeTestArr = [
            Employee("Gonzalo", 19,"Juarez", 666, 20000),
            Employee("X", 22, "Y", 247, 35000)
        ]

    def test_get_person(self):
        self.assertDictEqual(self.personTest.get_person(), {
            "nombre":"Gonzalo",
            "edad": 19, 
            "apellido": "Juarez", 
            "numero": 666
        })

    def test_get_employee(self):
        self.assertDictEqual(self.employeeTestArr[0].get_employee(), {
            "nombre":"Gonzalo", 
            "edad": 19, 
            "apellido": "Juarez", 
            "numero": 666,
            "salario": 20000
        })

    def test_pay_taxes(self):
        self.assertEqual(self.employeeTestArr[1].pay_tax(), "Paga impuestos")

    def test_no_pay_taxes(self):
        self.assertEqual(self.employeeTestArr[0].pay_tax(), "No paga impuestos")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmployee)
    unittest.TextTestRunner().run(suite)