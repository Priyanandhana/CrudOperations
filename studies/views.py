from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Study
from .forms import StudyForm
import os

# View for displaying the list of studies
def study_list(request):
    studies = Study.objects.all()

    # Adding file names to each study
    for study in studies:
        if study.attachment:
            study.file_name = os.path.basename(study.attachment.name)
        else:
            study.file_name = None

    return render(request, 'studies/study_list.html', {'studies': studies})


# View for adding a new study
def study_add(request):
    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new study record
            return redirect('study_list')  # Redirect to the study list after adding
        else:
            print(form.errors)  # Log errors for debugging
    else:
        form = StudyForm()  # Show an empty form for a GET request
    return render(request, 'studies/study_add.html', {'form': form})


# View for viewing a study's details
def study_view(request, id):
    study = get_object_or_404(Study, id=id)
    file_name = os.path.basename(study.attachment.name) if study.attachment else None
    return render(request, 'studies/study_view.html', {'study': study, 'file_name': file_name})


# View for editing an existing study
def study_edit(request, id):
    # Get the study object based on the id
    study = get_object_or_404(Study, id=id)

    if request.method == 'POST':
        form = StudyForm(request.POST, request.FILES, instance=study)
        if form.is_valid():
            # Handle file update here
            new_attachment = form.cleaned_data.get('attachment')
            if new_attachment and new_attachment != study.attachment:
                if study.attachment and os.path.isfile(study.attachment.path):
                    os.remove(study.attachment.path)
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)

    return render(request, 'studies/study_edit.html', {'form': form, 'study': study})



# View for deleting a study
def study_delete(request, study_id):
    study = get_object_or_404(Study, id=study_id)

    if request.method == 'POST':
        study.delete()  # Delete the study
        return redirect('study_list')  # Redirect to study list after deletion

    return render(request, 'studies/study_delete.html', {'study': study})

from django.shortcuts import render, redirect
from .models import Study

def study_delete_bulk(request):
    if request.method == 'POST':
        study_ids = request.POST.getlist('study_ids')
        if study_ids:
            Study.objects.filter(id__in=study_ids).delete()
        return redirect('study_list')  # Redirect to a page after deletion
