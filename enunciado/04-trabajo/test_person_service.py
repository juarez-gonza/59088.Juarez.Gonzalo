from person_service import PersonService
from person import Person
from repository import Repository
from parameterized import parameterized, param
import unittest


class TestPersonService(unittest.TestCase):

    def setUp(self):
        Person._id_count = 0
        self.person_service = PersonService(Repository())
        to_add = [
            Person('federico', 'gonzales', '20'),
            Person('claudio', 'pico', '33'),
            Person("nicolas", "pico", '40')
        ]
        for person in to_add:
            self.person_service.add_one(person)

    def tearDown(self):
        Person._id_count = 0
        del self.person_service

    def test_add_one(self):
        added = self.person_service.add_one(Person("Gonzalo", "Juarez", 19))
        self.assertEqual(added.id, Person._id_count - 1)

    def test_delete_one(self):
        added = self.person_service.add_one(Person("Gonzalo", "Juarez", 19))
        self.assertIsNotNone(added.id)
        self.person_service.delete_one(added.id)

        # para mostrar que la key ya no existe en el repositorio
        with self.assertRaises(KeyError):
            self.person_service.repository.persons[added.id]

    def test_find_one(self):
        # caso verdadero, en setUp el id 1 corresponde a claudio
        found = self.person_service.find_one(1)
        self.assertEqual(self.person_service.repository.persons[1], found)
        # caso de error en la búsqueda(devuelve falso para no salir del
        # programa cuando se corra desde la terminal con
        # stdin ante un error del usuario)
        self.assertFalse(self.person_service.find_one(100))

    def test_find_many(self):
        found = self.person_service.find_many()
        self.assertEqual(found, self.person_service.repository.persons)

    @parameterized.expand([
        param([
            Person("Gonzalo", "Juarez", 19),
            Person("Santiago", "Juarez", 22)
        ])
    ])
    def test_id(self, person_arr):
        # consistencia de id al agregar, eliminar, volver a agregar
        self.person_service.add_one(person_arr[0])
        self.assertEqual(person_arr[0].id, Person._id_count - 1)

        self.person_service.delete_one(person_arr[0].id)

        self.person_service.add_one(person_arr[1])
        self.assertEqual(person_arr[1].id, Person._id_count - 1)

        self.person_service.add_one(person_arr[0])
        self.assertEqual(person_arr[0].id, Person._id_count - 1)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPersonService)
    unittest.TextTestRunner().run(suite)
