
#B. Albert

from django.db import models

class Person(models.Model):

    #Définition des champs
    def __str__(self):
        return self.first_name + " " + self.last_name

    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

class Message(models.Model):

    #Définition des champs
    def __str__(self) -> str:
        if len(self.contents) > 20:
            return self.contents[:19] + "..."
        else:
            return self.contents
    author = models.ForeignKey('Person', on_delete=models.CASCADE)
    contents = models.TextField()
    publication_date = models.DateField()


class Faculty(models.Model):

    #Définition des champs
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

class Campus(models.Model):
    #Définition des champs
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

class Job(models.Model):
    #Défintition des champs
    def __str__(self):
        return self.title
    title = models.CharField(max_length=30)


class Cursus(models.Model):
    #Définition des champs
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=30)


class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    Job = models.ForeignKey('Job', on_delete=models.CASCADE)

class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE)
    year = models.IntegerField()


