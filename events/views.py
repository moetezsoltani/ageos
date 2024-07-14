from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Publication, Formation
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'publications/publication_list.html', {'publications': publications})


def publication_detail(request, id):
    publication = get_object_or_404(Publication, id=id)
    return render(request, 'publications/publication_detail.html', {'publication': publication})


@login_required
def publication_delete(request, id):
    publication = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')
    return render(request, 'publications/publication_confirm_delete.html', {'publication': publication})

def formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'formations/formation_list.html', {'formations': formations})

def formation_detail(request, formation_id):
    formation = get_object_or_404(Formation, pk=formation_id)
    return render(request, 'formations/formation_detail.html', {'formation': formation})

def missions_view(request):
    return render(request, 'missions.html')

def members_view(request):
    return render(request, 'members.html')

def admin_check(user):
    return user.is_staff

@user_passes_test(admin_check)
def admin_dashboard(request):
    user_count = User.objects.count()
    event_count = Event.objects.count()
    publication_count = Publication.objects.count()
    formation_count = Formation.objects.count()

    # User growth data
    last_month = timezone.now() - timedelta(days=30)
    user_growth = User.objects.filter(date_joined__gte=last_month).annotate(date=Count('date_joined'))
    user_dates = [user.date_joined.strftime('%Y-%m-%d') for user in user_growth]
    user_counts = [user.date for user in user_growth]

    context = {
        'user_count': user_count,
        'event_count': event_count,
        'publication_count': publication_count,
        'formation_count': formation_count,
        'user_dates': user_dates,
        'user_counts': user_counts,
    }
    return render(request, 'admin_dashboard.html', context)

