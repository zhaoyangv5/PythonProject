from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        lables = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        # 属性widgets。小部件（widget）是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets，可覆盖Django选择的默认小部件