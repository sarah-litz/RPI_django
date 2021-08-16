from django.db import models
from pychartjs import BaseChart, ChartType, Color 

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
    
    # GANTT CHART # # # # # # # # 
    class MyBarGraph(BaseChart): 
        
        type = ChartType.HorizontalBar

        class labels: ["1", "2", "3", "4"],   # FOR ALL DATA POINTS TO SHOW UP YOU MUST HAVE THE CORRECT NUMBER OF LABELS LISTED! 
        
        class data: 
            
            class dataset1: 
                data = 0, 100, 150, 600
                backgroundColor = Color.RGBA(63,103,126,0)
                hoverBackgroundColor = Color.RGBA(50,90,100,0)
            class dataset2: 
                data = 100, 100, 200, 200, 100,
                backgroundColor = [Color.Red, Color.Green, Color.Blue, Color.Yellow]
        
        class options:

            title = {"text": "TITLE", "display": True} 
            animation = {"duration": 10}
            hover = {"animationDuration": 10 }
            responsiveAnimationDuration = 0

            legend = {
                    'display': 'false', 
                    'position': 'bottom', 
                    'labels': {
                        'fontColor': Color.Gray, 
                        'fullWidth': True
                        }
                    }
            scales = {
                "xAxes": [{
                    "label": "Durations", 
                    "ticks": { 
                        "beginAtZero": True, 
                    }, 
                    "gridLines": { }, 
                    "stacked": True, 
                }], 
                "yAxes": [{
                    "id": "events",
                    "gridLines": { 
                        "display":False, 
                        "color": "#fff", 
                        "zeroLineColor": "#fff", 
                        "zeroLineWidth": 0, 
                    }, 
                    "ticks": {
                        # "callback": "<<function(value, index, values) {return value + ' Big Ones';}>>",
                    }, 
                    "stacked": True, 
                }], 
                "legend":{
                    "display":False
                }
            }
    
    
    graph = MyBarGraph() 
    graphJSON = graph.get() 
    
    
    

    # # # # # # # # # # # # # # # 


