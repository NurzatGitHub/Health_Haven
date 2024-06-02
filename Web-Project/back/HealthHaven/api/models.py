from django.db import models
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     image = models.ImageField(null=True, blank=True, upload_to="images/")
#     phone_number = models.CharField(max_length=255, blank=True, unique=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     blood_group = models.CharField(max_length=5, null=True, blank=True)
#     diagnosis = models.CharField(max_length=255, null=True, blank=True)
#     allergies = models.TextField(blank=True,null=True)
#     contraindications = models.TextField(blank=True,null=True)
#     guardian_contact = models.CharField(max_length=20, null=True, blank=True)
#     hospital = models.CharField(max_length=255, null=True, blank=True)


#     user_permissions = models.ManyToManyField(Permission, related_name="personal_data_permissions")
#     groups = models.ManyToManyField(Group, related_name="personal_data_groups")

#     REQUIRED_FIELDS = ['username', 'password', 'email']


class PersonalData(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    # name = models.CharField(max_length=255, blank=False,default="Nurzat")# Сделал имя обязательным
    # surname = models.CharField(max_length=255, blank=False,default="Turganbek")  # Сделал фамилию обязательной
    # email = models.EmailField(max_length=255, blank=False)  # Сделал email обязательным
    # password = models.CharField(max_length=255,blank=True)
    phone_number = models.CharField(max_length=255, blank=True)# Остальные поля необязательные
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    diagnosis = models.CharField(max_length=255, null=True, blank=True)
    allergies = models.TextField(blank=True,null=True)
    contraindications = models.TextField(blank=True,null=True)
    guardian_contact = models.CharField(max_length=20, null=True, blank=True)
    hospital = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='personaldataset',
        null=True,
        blank=True
    )

    class Meta():
        verbose_name = "PersonalData"
        verbose_name_plural = "PersonalDataset"
    
    def __str__(self):
        return f"image: {self.image}, " \
            f"date_of_birth: {self.date_of_birth}, " \
            f"blood_group: {self.blood_group}, " \
            f"diagnosis: {self.diagnosis}, " \
            f"allergies: {self.allergies}, " \
            f"contraindications: {self.contraindications}, " \
            f"guardian_contact: {self.guardian_contact}, " \
            f"hospital: {self.hospital}"
    
    def to_json(self):
        return {
            "image" : self.image,
            "date_of_birth": self.date_of_birth,
            "blood_group": self.blood_group,
            "diagnosis": self.diagnosis,
            "allergies": self.allergies,
            "contraindications": self.contraindications,
            "guardian_contact": self.guardian_contact,
            "hospital": self.hospital,
        }
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/") 

    def __str__(self):
        return self.title + '  |  ' + str(self.author)
    

