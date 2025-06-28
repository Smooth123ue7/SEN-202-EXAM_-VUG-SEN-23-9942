from django.db import models

# Reusable Address model
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

# Abstract base class for staff
class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)  # Linked Address

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

# Manager subclass
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def get_role(self):
        return "Manager"

# Intern subclass
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end = models.DateField()

    def get_role(self):
        return "Intern"