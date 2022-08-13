# from django.db import models  
# from django.urls import reverse, reverse_lazy  

# # Create your models here.  
# # declare a new model with a name"employee"  
# class user(models.Model):  
# # fields of the model  
#         userid = models.AutoField(primary_key=True,serialize = False,verbose_name ='ID')  
#         username = models.CharField(max_length=100)  
#         useremail = models.EmailField()  
#         usercontact = models.CharField(max_length=15)  
#         userdob = models.DateField(blank=True, null=True)# If no date is selected then Django saves blank field value.  
#         def get_absolute_url(self):  

# # return reverse('user-detail', kwargs={'pk': self.pk})  
#     #objects = models.Manager()  
# class Meta:  
#     db_table = "user"  
#     ordering = ['userid',]#sorts the records ascending using 'eid' field   