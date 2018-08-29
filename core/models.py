from django.db import models as m

# Create your models here.
class Instagram(m.Model):
	name = m.CharField(max_length=50, blank=False, unique=True)
	data = m.TextField()