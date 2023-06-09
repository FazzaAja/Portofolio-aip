from django.db import models

# Create your models here.


class Foto(models.Model):
    foto = models.ImageField(upload_to='foto/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True) 
    judul = models.CharField(max_length=50)
    keterangan = models.TextField()


    def __str__(self):
        return self.judul

