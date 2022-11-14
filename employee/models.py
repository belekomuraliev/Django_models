from django.db import models
import datetime

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField( null=True,blank=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Пользователь {self.name} успешно сохранен')

    def get_age(self):
        age = datetime.datetime.today() - self.birth_date
        print(age)

class Employee(AbstractPerson):
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    work_experience = models.DateField()

class Passport(models.Model):
    inn = models.IntegerField()
    id_card = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f'Имя {self.employee.name} иин {self.inn} № паспорта{self.id_card}'

    def get_gender(self):
        if self.inn[0] == 2:
            return 'mail'
        if self.inn[0] == 1:
            return 'fimail'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Пользователь {self.employee} успешно сохранен')


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Проект {self.project_name} успешно сохранен')
class Membership(models.Model):
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f' {self.workproject} {self.employee}'
#
class Client(AbstractPerson):
    addres = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

class VipClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField(null=True)

    def __str__(self):
        return f' {self.name} {self.vip_status_start} {self.donation_amount}'
