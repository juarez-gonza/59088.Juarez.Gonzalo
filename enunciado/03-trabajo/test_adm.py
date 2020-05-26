import unittest
from administration import Administration
from employee import Employee
from parameterized import parameterized, param


class TestAdm(unittest.TestCase):

    def setUp(self):
        self.adm = Administration()
    #     self.adm.add_employee(Employee("Gonzalo", 19, "Juarez", 666, 20000).get_employee())
    #     self.adm.add_employee(Employee("X", 22, "Y", 666, 35000).get_employee())
    # opción útil para inicializar previo a cada test en lugar de en parameterized.expand
    # (parameterize.expand crea cuantas copias de la función sean necesarias para los distintos parámetros)

    def tearDown(self):
        self.adm = None

    @parameterized.expand([
        param([
            Employee("Gonzalo", 19, "Juarez", 666, 20000).get_employee(),
            Employee("X", 22, "Y", 666, 35000).get_employee()
        ])
    ])
    def test_legajo(self, employee_arr):
        for i in range(len(employee_arr)):
            self.adm.add_employee(employee_arr[i])
        key_list = [*self.adm.listEmployee]
        self.assertListEqual(key_list, [i for i in range(len(key_list))])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdm)
    unittest.TextTestRunner().run(suite)
