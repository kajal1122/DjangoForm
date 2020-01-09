from django.forms import ModelForm
from .models import QuestionSet

class QuestionForm(ModelForm):
    class Meta:
        model = QuestionSet
        fields = ['feel_on_completing_project','projects_on_hold','finished_project','project_name','why_to_finish_project','my_dream_day',
        'when_will_finish_project','tools_and_tech','how_to_stay_focused']
