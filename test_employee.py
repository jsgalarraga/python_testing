import unittest
from unittest import TestCase
from unittest.mock import patch
from employee import Employee

class TestEmployee(TestCase):

  @classmethod
  def setUpClass(cls):
    '''Runned before anything'''
    pass

  @classmethod
  def tearDownClass(cls):
    '''Runned after everything'''
    pass

  def setUp(self):
    '''Runned before each test'''
    self.emp_1 = Employee('Jaime', 'Sanchez', 30000)
    self.emp_2 = Employee('Arturo', 'Martin', 40000)

  def tearDown(self):
    '''Runned after each test'''
    pass

  def test_email(self):
    self.assertEqual(self.emp_1.email, 'Jaime.Sanchez@email.com')
    self.assertEqual(self.emp_2.email, 'Arturo.Martin@email.com')

    self.emp_1.first = 'Begoña'
    self.emp_2.first = 'Carlos'

    self.assertEqual(self.emp_1.email, 'Begoña.Sanchez@email.com')
    self.assertEqual(self.emp_2.email, 'Carlos.Martin@email.com')

  def test_fullname(self):
    self.assertEqual(self.emp_1.fullname, 'Jaime Sanchez')
    self.assertEqual(self.emp_2.fullname, 'Arturo Martin')

    self.emp_1.first = 'Begoña'
    self.emp_2.first = 'Carlos'

    self.assertEqual(self.emp_1.fullname, 'Begoña Sanchez')
    self.assertEqual(self.emp_2.fullname, 'Carlos Martin')

  def test_apply_raise(self):
    self.emp_1.apply_raise()
    self.emp_2.apply_raise()

    self.assertEqual(self.emp_1.pay, 31500)
    self.assertEqual(self.emp_2.pay, 42000)

  def test_monthly_schedule(self):
    with patch('employee.requests.get') as mocked_get:
      mocked_get.return_value.ok = True
      mocked_get.return_value.text = 'success'

      schedule = self.emp_1.monthly_schedule('May')
      mocked_get.assert_called_with('http://company.com/Sanchez_Jaime/May')
      self.assertEqual(schedule, 'success')

      mocked_get.return_value.ok = False

      schedule = self.emp_2.monthly_schedule('June')
      mocked_get.assert_called_with('http://company.com/Martin_Arturo/June')
      self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
  unittest.main()
