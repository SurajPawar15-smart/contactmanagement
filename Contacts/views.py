from django.shortcuts import render, redirect
from .models import People
from .forms import PeopleForm


def view_contacts(request):
    people = People.objects.all()
    context = {'people': people}
    return render(request, 'contacts/views.html', context)


def add_contacts(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('contacts')
    else:
        form = PeopleForm
    return render(request, "contacts/add-contact.html", {'form':form})


def edit_contacts(request, people_id):
    people = People.objects.get(id=people_id)
    if request.method == "POST":
        form = PeopleForm(request.POST, instance=people)
        form.save()
        return redirect('contacts')
    else:
        form = PeopleForm(instance=people)
    context = {'form': form}
    return render(request, 'contacts/edit-contact.html', context)


def delete_contacts(request, people_id):
    people = People.objects.get(id=people_id)
    people.delete()
    return redirect('contacts')