from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    phone = models.TextField(max_length=15)
    city = models.TextField(max_length=25)
    state = models.TextField(max_length=25)
    zipcode = models.TextField(max_length=15)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")