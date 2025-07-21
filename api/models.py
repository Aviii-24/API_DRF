from django.db import models

# Create your models here.

from django.db import models

class WheelSpecification(models.Model):
    inspector_name = models.CharField(max_length=100)
    form_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='wheel_specs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form_number

class BogieChecksheet(models.Model):
    inspector_name = models.CharField(max_length=100)
    remarks = models.TextField()
    date_checked = models.DateTimeField()

    def __str__(self):
        return self.inspector_name
