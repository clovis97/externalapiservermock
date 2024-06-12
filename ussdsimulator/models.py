from django.db import models

class Pensionnaire(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    num_cnssap = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=300)
    pin = models.CharField(max_length=4, null=True)

class Paiement(models.Model):
    pensionnaire = models.ForeignKey(Pensionnaire, on_delete=models.CASCADE)
    depositaire = models.CharField(max_length=100)
    montant_en_cdf = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=50)
    date = models.DateTimeField()
    etat = models.CharField(max_length=20)

class Interaction(models.Model):
    pensionnaire = models.ForeignKey(Pensionnaire, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class SessionLevel(models.Model):
    session_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    level = models.IntegerField(default=0)
    confirm_pin = models.CharField(max_length=4, null=True, blank=True)
