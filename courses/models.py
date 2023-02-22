from django.db import models
from faker import Faker

from groups.models import Group
from students.models import Student
from teachers.models import Teacher


class Course(models.Model):
    course = models.CharField(max_length=55)
    # description = models.TextField(null=True, blank=True)
    # course = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='group')
    # teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    # students = models.ManyToManyField(Student)

    def __str__(self):
        return f'Group name: {Group.name} == str{self.course}'

    # @classmethod
    # def generate_fake_data(cls, count):
    #     f = Faker()
    #     lst1 = ['Day', 'Night']
    #     for _ in range(count):
    #         cr = cls()
    #         cr.name = f.random.choice(lst1)
    #         cr.description = f.sentence()
    #         cr.clean_fields()
    #         cr.save()
