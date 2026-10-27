from django.shortcuts import render, get_object_or_404, redirect
from .models import Workshop
from .forms import WorkshopForm

def workshop_list_view(request):
    workshops = Workshop.objects.all().order_by('date')
    return render(request, 'workshops/workshop_list.html', {'workshops': workshops})

def workshop_detail_view(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    return render(request, 'workshops/workshop_detail.html', {'workshop': workshop})

def workshop_create_view(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workshop_list')
    else:
        form = WorkshopForm()
    return render(request, 'workshops/workshop_form.html', {'form': form, 'action': 'Create'})

def workshop_update_view(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if request.method == 'POST':
        form = WorkshopForm(request.POST, instance=workshop)
        if form.is_valid():
            form.save()
            return redirect('workshop_detail', pk=workshop.pk)
    else:
        form = WorkshopForm(instance=workshop)
    return render(request, 'workshops/workshop_form.html', {'form': form, 'action': 'Update'})

def workshop_delete_view(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if request.method == 'POST':
        workshop.delete()
        return redirect('workshop_list')
    return render(request, 'workshops/workshop_confirm_delete.html', {'workshop': workshop})