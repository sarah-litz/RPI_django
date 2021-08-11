from django.db import models

# Create your models here.

# Step 1 in writing database web app is to define models 
# models – essentially, your database layout, with additional metadata.


class Experiment(models.Model): 
    user_name = models.CharField(max_length=200)
    date = models.DateTimeField('date', auto_now_add=True)
    # by placing ForeignKey(Experiment) in Script Class, we give the Experiment class instances access to this list through the use of Script_set
    # def __str__(self): 
    #    return str(self.date)

class Script(models.Model): 
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    SCRIPT_CHOICES = [ ('Magazine', 'Magazine'), 
                       ('Autoshape', 'Autoshape') ]
    type = models.TextField(choices = SCRIPT_CHOICES)

