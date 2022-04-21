import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from .models import *


def index(request):
    bio_title = 'Giorgia Longoni'
    bio_text = '''Italian interior architect passionate about conceptual design and the mechanical engineering. Grown up in the Italian furniture and design district around Milan, Giorgia has always spoken the workshop language staying by her father side. She worked with carpenters, glass-makers, marble-cutters and metalworkers to produce the furniture components, then assembled and sold in the family showroom.
    During the years, she has expanded and refined her taste, also thanks to the influences of her professional career as interior designer by a famous architectural firm in Milan, where she designed private houses, restaurants, clubs and luxury brands shops all around the world.'''
    bio_text = bio_text.splitlines()
    
    slides = MainPageCoverPhotos.objects.all().order_by('order')
    categories = Category.objects.all()
    retail = categories.get(name='retail')
	
    try:
        hospitality = categories.get(name='hospitality')
    except ObjectDoesNotExist:
        print('There are no hospitality projects present in DB.')

    try:
        headquarter = categories.get(name='headquarter')
    except ObjectDoesNotExist:
        print('There are no headquarter projects present in DB.')

    try:
        residential = categories.get(name='residential')
    except ObjectDoesNotExist:
        print('There are no residential projects present in DB.')

    try:
        scenography = categories.get(name='scenography')
    except ObjectDoesNotExist:
        print('There are no scenography projects present in DB.')

    try:
        project_id = (Project.objects.all().filter(
            name='via petrarca').first()).id
        studio_photos = Photo.objects.all().filter(project_id=project_id)
    except ObjectDoesNotExist:
        print('There are no studio photos present in DB.')

    category_covers = {
        'retail': (retail.photo if retail else ''),
        'hospitality': (hospitality.photo if hospitality else ''),
        'headquarter': (headquarter.photo if headquarter else ''),
        'residential': (residential.photo if residential else ''),
        'scenography': (scenography.photo if scenography else ''),
    }

    projects = Project.objects
    projects_present = {
        'retail': projects.filter(category=retail.id).count() > 0,
        'hospitality': projects.filter(category=hospitality.id).count() > 0,
        'headquarter': projects.filter(category=headquarter.id).count() > 0,
        'residential': projects.filter(category=residential.id).count() > 0,
        'scenography': projects.filter(category=scenography.id).count() > 0,
    }

    return render(request,
                  'main/index.html',
                  context={
                      "bio_title": bio_title,
                      "bio_text": bio_text,
                      "slides": slides,
                      "category_covers": category_covers,
                      "projects_present": projects_present,
                      "studio_photos": studio_photos
                  })


def projects(request, type):
    c = Category.objects.all().filter(name=type).first()
    pp = Project.objects.filter(category=c.id).order_by('order')

    return render(request,
                  'main/gallery.html',
                  context={
                      "projects": pp,
                      "category": c.name
                  })


def project_detail(request, id):
    p = Project.objects.filter(id=id).first()
    project_caption = p.caption
    photo_objects = Photo.objects.filter(project=p.id)
    details = {"caption": project_caption, "name": p.name, "photos": {}}
    for po in photo_objects:
        details["photos"][str(po.order)] = {
            "caption": po.caption,
            "photo": po.photo.url,
        }
    return JsonResponse(details)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')