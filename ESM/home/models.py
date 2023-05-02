from django.db import models

# Create your models here.

class TUser(models.Model):
    us_id   = models.CharField(max_length=20)
    us_pw   = models.CharField(max_length=20)
    us_api  = models.CharField(max_length=64)
    class Meta:
        db_table = "tuser"
    
class TInput(models.Model):
    i_id        = models.IntegerField(primary_key=True)
    us          = models.ForeignKey(TUser, on_delete=models.CASCADE)
    in_fname    = models.CharField(max_length=30)
    in_ftype    = models.CharField(max_length=4)
    in_contents = models.TextField()
    in_words    = models.TextField()
    in_date     = models.DateField()
    class Meta:
        db_table = "tinput"
    
class TSummary(models.Model):
    s_id        = models.IntegerField(primary_key=True)
    i           = models.ForeignKey(TInput, on_delete=models.CASCADE)
    # in_contents = models.ForeignObject(TInput, on_delete=models.CASCADE,from_fields=['in_contents'],to_fields=['in_contents'])
    su_impwords = models.TextField()
    su_contents = models.TextField()
    class Meta:
        db_table = "tsummary"
    
class TExtent(models.Model):
    e_id        = models.IntegerField(primary_key=True)
    i           = models.ForeignKey(TInput, on_delete=models.CASCADE)
    ex_contents = models.TextField()
    class Meta:
        db_table = "textent"
    
    
class TWord(models.Model):
    w_id        = models.IntegerField(primary_key=True)
    i           = models.ForeignKey(TInput, on_delete=models.CASCADE)
    w_name      = models.TextField()
    w_contents  = models.TextField()
    class Meta:
            db_table = "tword"
    
    

    
#id->input(contents에서 words분리 tword로 단)