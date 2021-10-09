from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    post_code = models.CharField(max_length=10)
    business_size = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    abn_number = models.CharField(max_length=50)
    vehicle = models.CharField(max_length=100)
    driver_license = models.ImageField(upload_to='contractor/license')
    image = models.ImageField(upload_to='contractor/images')
    insurence = models.ImageField(upload_to='contractor/insurence')
    bank_name = models.CharField(max_length=100)
    bsb_number = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    occupation = models.CharField(max_length=150)
    apprentice = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    dob = models.DateField()
    address = models.CharField(max_length=150)
    legall_in_au = models.CharField(max_length=100)
    work_in_ct = models.CharField(max_length=100)
    experience_ct = models.CharField(max_length=100)
    aboriginal = models.CharField(max_length=100)
    islander = models.CharField(max_length=100)
    medical = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    interpreter = models.CharField(max_length=100)
    em_name = models.CharField(max_length=100)
    em_phone = models.CharField(max_length=30)
    em_relation = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
