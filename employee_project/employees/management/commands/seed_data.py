import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee
from attendance.models import Attendance, Performance

class Command(BaseCommand):
    help = 'Seed the database with fake employees, attendance, and performance data'

    def handle(self, *args, **kwargs):
        fake = Faker('en_IN')  # Indian locale for names

        # 1️⃣ Departments
        dept_names = ['HR', 'IT', 'Sales', 'Marketing', 'Finance']
        departments = []
        for name in dept_names:
            dept, created = Department.objects.get_or_create(name=name)
            departments.append(dept)
        self.stdout.write(self.style.SUCCESS(f'{len(departments)} departments created'))

        # 2️⃣ Employees
        num_employees = 50
        employees = []
        for _ in range(num_employees):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)
        self.stdout.write(self.style.SUCCESS(f'{len(employees)} employees created'))

        # 3️⃣ Attendance (last 60 days)
        statuses = ['Present', 'Absent', 'Late']
        today = date.today()
        for emp in employees:
            for i in range(60):
                att_date = today - timedelta(days=i)
                Attendance.objects.create(
                    employee=emp,
                    date=att_date,
                    status=random.choices(statuses, weights=[0.7, 0.2, 0.1])[0]
                )
        self.stdout.write(self.style.SUCCESS('Attendance records created'))

        # 4️⃣ Performance (random ratings over last 6 months)
        for emp in employees:
            for i in range(6):
                review_date = today - timedelta(days=i*30)
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=review_date
                )
        self.stdout.write(self.style.SUCCESS('Performance records created'))
