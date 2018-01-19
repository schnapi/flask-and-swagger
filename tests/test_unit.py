import json
import unittest
from ..core.app import app


class TestPetsEndpoint(unittest.TestCase):

    def setUp(self):
        ''' fire up a test instance of the flask app '''
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        ''' 
            tear down app, reverse any changes made 
            - remove the brand inserted in test_post()
        '''
        pass

    def test_put(self):
        '''
            update a pet with id 1 in database
            - test that the response status code == 200 and the returned pet object is updated
        '''
        pet = {"species": "test", "birthday": "2017-05-25", "name": "test", "gender": "w"}
        headers = {'content-type': 'application/json'}
        result = self.app.put('/apiPets/pet/1', data=json.dumps(pet), headers=headers)
        self.assertEqual(result.status_code, 200)
        res = json.loads(result.get_data(as_text=True))
        self.assertEqual(res, pet)

    def test_get(self):
        ''' 
            get all pets
            - test status code + json properties are not null
        '''
        result = self.app.get("/apiPets/pets")
        self.assertEqual(result.status_code, 200)
        res = json.loads(result.get_data(as_text=True))
        print(res)
        for pet in res:
            self.assertIsNotNone(pet['id'])
            self.assertIsNotNone(pet['species'])
            self.assertIsNotNone(pet['gender'])
            self.assertIsNotNone(pet['name'])
            self.assertIsNotNone(str(pet['birthday']))


if __name__ == '__main__':
    unittest.main()
