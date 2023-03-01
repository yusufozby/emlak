from django.db import models

# Create your models here.

class Yeni(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Başlık")
    text_info = models.TextField(max_length = 1000, verbose_name = "Açıklama")
    text = models.TextField(max_length=5000, verbose_name = "Text")  
    advisor = models.CharField(max_length = 100, verbose_name= "Danışman")
    date = models.DateTimeField(("Tarih"), auto_now_add=True,blank=True,null=True)
    image = models.FileField(upload_to='',verbose_name='Fotoğraf 1',blank=True,null=True)
    image_2 = models.FileField(upload_to='',verbose_name='Fotoğraf 2',blank=True,null=True)
    image_3 = models.FileField(upload_to='',verbose_name='Fotoğraf 3',blank=True,null=True)
    image_4 = models.FileField(upload_to='',verbose_name='Fotoğraf 4',blank=True,null=True)
    image_5 = models.FileField(upload_to='',verbose_name='Fotoğraf 5',blank=True,null=True)
    bd_image = models.FileField(upload_to='',verbose_name='Bd Fotoğraf',blank=True,null=True)
    owner = models.CharField(max_length = 100,verbose_name="Ev Sahibi",blank=True,null=True)
    fiyat = models.IntegerField(verbose_name="Fiyatı",blank=True,null=True)
    feature = models.CharField(max_length=100 , verbose_name= "Özellik")
    


    def __str__(self):
        show = 'Başlık: ' + self.title
        show += ', Danışman: ' + self.advisor
        return show