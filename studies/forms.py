from django import forms
from .models import Study, Phase

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['study_name', 'study_phase', 'sponsor_name', 'study_description','attachment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['study_phase'].queryset = Phase.objects.all()

    def clean_attachment(self):
        file = self.cleaned_data.get('attachment', None)
        valid_mime_types = [
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ]
        if file and file.content_type not in valid_mime_types:
            raise forms.ValidationError('Unsupported file type. Please upload a valid file (pdf,xlxs,xls,docx,ppt,pptx).')
        return file