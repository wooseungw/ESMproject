from django.db import models

# Create your models here.

class TUser(models.Model):
    us_username = models.CharField(max_length=64)
    us_pw = models.CharField(max_length=128)
    us_api  = models.CharField(max_length=64)
    class Meta:
        db_table = "tuser"
        
        
    
class TInput(models.Model):
    i_id        = models.IntegerField(primary_key=True)
    us          = models.ForeignKey(TUser, on_delete=models.CASCADE)
    in_fname    = models.CharField(max_length=40)
    in_ftype    = models.CharField(max_length=4)
    in_contents = models.TextField()
    in_date     = models.DateField()
    class Meta:
        db_table = "tinput"
    
class TContnets(models.Model):
    c_id        = models.IntegerField(primary_key=True)
    i           = models.ForeignKey(TInput, on_delete=models.CASCADE)
    # in_contents = models.ForeignObject(TInput, on_delete=models.CASCADE,from_fields=['in_contents'],to_fields=['in_contents'])
    co_indexs = models.TextField()
    co_contents = models.TextField()
    co_ketwords = models.TextField()
    class Meta:
        db_table = "tcontnets"
    
    
    

    
#id->input(contents에서 words분리 tword로 단)