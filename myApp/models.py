from django.db import models

# Create your models here.

class Yeni(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Başlık")
    text_info = models.CharField(max_length = 1000, verbose_name = "Açıklama")
    text = models.TextField(max_length=5000, verbose_name = "Text")  
    yazar = models.CharField(max_length = 100)
    image = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    image_2 = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    image_3 = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    image_4 = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    image_5 = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    # image_6 = models.FileField(upload_to='',verbose_name='Fotoğraf',blank=True,null=True)
    owner = models.CharField(max_length = 100,verbose_name="Ev Shibi",blank=True,null=True)
    fiyat = models.IntegerField(verbose_name="Fiyatı",blank=True,null=True)

    def __str__(self):
        show = 'Başlık: ' + self.title
        show += ', Yazar: ' + self.yazar
        return show