from django import forms
from .models import Topic

#モデルを継承したフォームクラス。このフォームクラスを使うことでバリデーションができる
class TopicForm(forms.ModelForm):

    class Meta:
        #Topicのcommentを元にバリデーションを行う
        model   = Topic
        fields  = [ "comment","title" ]