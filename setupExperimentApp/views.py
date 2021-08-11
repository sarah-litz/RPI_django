from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.urls import reverse 
from .models import Experiment
from .forms import ExperimentForm, ScriptForm

# Create your views here.
'''class HomePageView(TemplateView): 
    def get(self, request, **kwargs): # expects an HTTP GET request to the url defined in the urls.py file 
        return render(request, 'index.html', context=None) # renders a template called index.html
'''
def experiments(request): 
    experiments = Experiment.objects.all()
    context = {'experiments': experiments}
    return render(request, 'index.html', context)

def view_experiment(request, exp_id): 
    ''' View an Experiment. Option to edit on this page. '''
    id = exp_id 
    exp = Experiment.objects.get(id = exp_id)
    user_name = exp.user_name
    script_set = exp.script_set.all()
    date = exp.date 
    context = {'experiment':exp, 'id':id, 'user_name':user_name, 'date':date, 'script_set':script_set}
    return render(request, 'view_experiment.html', context)

def edit_experiment(request, exp_id): 
    '''Edit an Existing Experiment's Scripts'''
    id = exp_id 
    exp = Experiment.objects.get(id = exp_id)
    user_name = exp.user_name
    script_set = exp.script_set.all
    print(user_name)
    date = exp.date 

    if request.method != 'POST': 
        # inital request to edit, fill form with current entry  
        form = ExperimentForm(instance=exp) 
        print("BLANK")
    else: 
        # POST data submitted; process data 
        form = ExperimentForm(instance=exp, data=request.POST) 
        if form.is_valid(): 
            form.save()
            return redirect('setupExperimentApp:view_experiment',id) # HELPFUL LINE TO REMEMBER for navigating between pages 
            # return redirect('.', exp_id=exp.id)
    # Display a blank or invalid form 
    context = {'experiment':exp, 'id':id, 'user_name':user_name, 'date':date, 'script_set':script_set, 'form':form}
    return render(request, 'edit_experiment.html', context)


def new_experiment(request): 
    ''' Add a new experiment to the experiment index '''
    if request.method != 'POST': 
        # no data submitted create a blank form 
        form = ExperimentForm() 
    else: 
        # POST data submitted; process data 
        form = ExperimentForm(data=request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('/')
    
    # display a blank or invalid form 
    context = {'form':form}
    return render(request, 'new_experiment.html', context)


def new_script(request, exp_id): 
    ''' Add a new script to an experiment (specified by exp_id) '''

    experiment = Experiment.objects.get(id=exp_id)

    if request.method != 'POST': 
        # no data submitted, create a blank form 
        form = ScriptForm() 
    else: 
        # POST data submitted; process data 
        form = ScriptForm(data=request.POST) 
        if form.is_valid(): 
            new_entry = form.save(commit=False)
            new_entry.experiment = experiment 
            new_entry.save() 
            form.save() 
            return redirect('setupExperimentApp:view_experiment',exp_id)
    
    # display a blank or invalid form 
    context = {'experiment':experiment, 'form':form}
    return render(request, 'new_script.html', context)