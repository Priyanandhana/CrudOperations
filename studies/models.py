from django.db import models
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(f"File size should not exceed 5 MB. Current size: {value.size / 1024 / 1024:.2f} MB.")
    valid_extensions = ['.pdf', '.docx', '.ppt', '.pptx', '.xls', '.xlsx']
    import os
    ext = os.path.splitext(value.name)[1]  # Get file extension
    if ext.lower() not in valid_extensions:
        raise ValidationError(f'Unsupported file extension. Allowed types: {", ".join(valid_extensions)}')

class Phase(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'phase'
        managed = False

    def __str__(self):
        return self.name


class Study(models.Model):
    study_name = models.CharField(max_length=100, db_column='study_name')
    study_description = models.TextField(db_column='study_description')
    study_phase = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE,
        db_column='study_phase',
        to_field = 'name'
    )
    sponsor_name = models.CharField(max_length=100, db_column='sponsor_name')
    attachment = models.FileField(max_length=100,upload_to='attachment/', validators=[validate_file_extension],null=True,blank=True,db_column='attachment')

    def __str__(self):
        return self.study_name

