from django.forms import ModelForm
from cognitive.models import Soldier


class CognitiveInterviewForm(ModelForm):

    class Meta:
        model = Soldier
        fields = '__all__'
        