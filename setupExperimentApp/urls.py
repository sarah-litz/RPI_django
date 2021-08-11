""" defines URL patterns for setupExperimentApp """

from django.urls import path 
from . import views

app_name = 'setupExperimentApp'
urlpatterns = [ # var for storing list of individual pages 
    # Example: 
        # views.index specifies which function to call in views.py
        # name='index' names this url pattern so we can refer to it easily later on 
        # path('', views.index, name='index'), 
    
    # path( '', views.HomePageView.as_view() ), 
    path( '', views.experiments, name='experiments'), 


    # Page for viewing an existing experiment's details. 
    path('view_experiment/<int:exp_id>/', views.view_experiment, name='view_experiment'), 

    # Page for editing an existing experiment 
    path('edit_experiment/<int:exp_id>/', views.edit_experiment, name='edit_experiment'), 

    # Page for adding a new experiment 
    path('new_experiment/', views.new_experiment, name='new_experiment'), 


    # Page for adding a new Script to an experiment 
    path('new_script/<int:exp_id>/', views.new_script, name='new_script'), 
    

]