from django.db import models
from django import forms
# Create your models here.

class QuestionSet(models.Model):

    feel_on_completing_project = models.TextField(verbose_name='What will I feel on completing this project?')
    projects_on_hold = models.TextField(verbose_name='What other projects I will put on hold for this project?')
    finished_project = models.TextField(verbose_name='What will the finished project look like?')


    project_name = models.CharField(verbose_name='Project Name',max_length=150)
    why_to_finish_project = models.TextField(verbose_name='Why do I have to finish this project?')
    my_dream_day = models.TextField(verbose_name='What does my dream day look like?')


    when_will_finish_project = models.DateField(verbose_name='When will I finish this project?')
    tools_and_tech = models.TextField(verbose_name='What Tools and Tech will I use?')
    how_to_stay_focused = models.TextField(verbose_name='How will I stay focused?')
