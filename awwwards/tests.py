from django.test import TestCase
from . models import Country,Tag,Post,Rating,Follow,Like,Profile,Profession

class ProfessionTest(TestCase):
    def setUp(self):
        self.new_profess= Profession(profession = 'Web Developer')

    def test_init(self):
        self.assertTrue(isinstance(self.new_profess,Profession))

    def test_save(self):
        self.new_profess.save_professions()
        all_professions= Profession.objects.all().count()
        self.assertTrue(all_professions,1)
