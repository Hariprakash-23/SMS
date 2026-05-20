from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student
from datetime import date

class StudentModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='hari',
            password='test123'
        )

        self.student = Student.objects.create(
            user=self.user,
            Reg_no='101',
            Name='Hari',
            DOB=date(2004, 1, 1),
            Address='Punjab',
            Phone='9876543210'
        )

    def test_student_creation(self):

        self.assertEqual(self.student.Name, 'Hari')

    def test_student_reg(self):

        self.assertEqual(self.student.Reg_no, '101')

    def test_phone_length(self):

        self.assertEqual(len(self.student.Phone), 10)