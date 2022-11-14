from employee.models import *

belek = Employee(position='Programmer', salary=10000,work_experience='2000-05-05', name='Belek',birth_date='1974-03-11')
belek.save()

manas = Employee(position='Fronded', salary=13000, work_experience='2010-07-05',name='Manas', birth_date='2000-05-12')
manas.save()

aman =Employee(position='Backend', salary=15000,work_experience='2010-06-05', name='Aman',birth_date='1999-06-07')
aman.save()
aza = Employee(position='Tester', salary=16000,work_experience='2015-06-05',name='Azamat', birth_date='2001-06-07')
aza.save()

p=Passport.objects.create(inn=26345197476354, id_card='AN6573245', employee=Employee(id=1))
p1=Passport.objects.create(inn=24565198476354, id_card='AN3453265', employee=Employee(id=2))
p2=Passport.objects.create(inn=23545248686654, id_card='AN2567468', employee=Employee(id=3))
p3=Passport.objects.create(inn=26692435268353, id_card='AN3453265', employee=Employee(id=4))
p3=Passport(inn=26692435268353, id_card='AN3453265', employee=Employee(id=4))
p3.save()
p3.delete()

w = WorkProject(project_name='Django_models2')
w.save()

m = Membership(workproject=w, employee=belek, date_joined='2022-01-03')
m.save()
m1 = Membership(workproject=w, employee=manas, date_joined='2022-01-03')
m1.save()
m2 = Membership(workproject=w, employee=aman, date_joined='2022-01-03')
m2.save()
m3 = Membership(workproject=w, employee=aza, date_joined='2022-01-03')
m3.save()

m3.delete()


aida = Employee(position='Beckend', salary=12000,
              work_experience='2018-05-05', name='Aida',
              birth_date='2001-07-07')
aida.save()

sadyr = Client(addres='Isanova 105', phone_number='0700346572',
               name='Sadyr', birth_date='2002-06-08')
sadyr.save()
sadyr.delete()

zul = Client(addres='Tynystanova 86', phone_number='0772453267',
             name='Zulaika', birth_date='2000-05-09')
zul.save()

nurs = Client(addres='Moskovskaia 50', phone_number='0555345673',
              name='Nursultan', birth_date='1997-04-09')
nurs.save()

ver=VipClient(vip_status_start='2022-05-06', donation_amount=500, addres='Asanbai 15',
              phone_number='0700010101', name='Veronika', birth_date='2000-05-07')


Employee.objects.all()

Passport.objects.all()

WorkProject.objects.all()

Client.objects.all()

VipClient.objects.all()
