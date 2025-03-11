from django.test import TestCase

class AdditionTest(TestCase):

    def setUp(self) -> None:
        super(AdditionTest, self).setUp()

    def simple_test_addition(self):
        self.assertEqual(1 + 1, 2)
