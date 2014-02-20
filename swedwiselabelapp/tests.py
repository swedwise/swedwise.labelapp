import unittest

class ProjectorViewsUnitTests(unittest.TestCase):
    def test_index_view(self):
        from views import index_view
        result = index_view({})
        self.assertEqual(len(result.keys()), 0)

class ProjectorFunctionalTests(unittest.TestCase):
    def setUp(self):
        from application import main
        app = main()
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'GODSFLAGGA' in res.body)
