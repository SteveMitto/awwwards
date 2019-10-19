from django.test import TestCase
from django.contrib.auth.models import User
from . models import Country,Tag,Post,Rating,Follow,Like,Profile,Profession

class ProfessionTest(TestCase):
    new_profess= Profession(profession = 'Web Developer')
    def setUp(self):
        self.new_profess= Profession(profession = 'Web Developer')

    def test_init(self):
        self.assertTrue(isinstance(self.new_profess,Profession))

    def test_save(self):
        self.new_profess.save_professions()
        all_professions= Profession.objects.all().count()
        self.assertTrue(all_professions,1)

class CountryTest(TestCase):
    new_country= Country(name = 'Web Developer')
    def setUp(self):
        self.new_country= Country(name = 'Web Developer')

    def test_init(self):
        self.assertTrue(isinstance(self.new_country,Country))

    def test_save(self):
        self.new_country.save_country()
        all_professions= Country.objects.all().count()
        self.assertTrue(all_professions,1)


class ProfileTest(ProfessionTest,CountryTest,TestCase):
    def setUp(self):
        user = User(username = "John" , password="1q3e5t7u")
        user.save()
        country=CountryTest.new_country
        country.save_country()
        profession=ProfessionTest.new_profess
        profession.save_professions()
        self.new_profile = Profile.objects.filter(user=user).first()
        # self.new_profile.profession.set(profession)
        # self.new_profile.country.set(country)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
