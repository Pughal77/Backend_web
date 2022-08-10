from django.forms import ModelForm
from .models import community_article_data

class new_entry(ModelForm):
    class Meta:
        model = community_article_data
        fields = ("title", "entry")
    



    


    


