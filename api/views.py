from json import dumps

from django.http import HttpResponse

CATS = [
    ("Deadmeow5", "https://commons.wikimedia.org/wiki/File:CatScratch.JPG#/media/File:CatScratch.JPG"),
    ("Alan Purring", "https://commons.wikimedia.org/wiki/File:Chmee2.jpg#/media/File:Chmee2.jpg"),
    ("Cats Domino", "https://commons.wikimedia.org/wiki/File:Henri%C3%ABtte_Ronner-Knip_-_Katjesspel.jpg#/media/File:Henri%C3%ABtte_Ronner-Knip_-_Katjesspel.jpg"),
    ("Kevin Purrant", "https://commons.wikimedia.org/wiki/Category:Playing_cats#/media/File:Pa013767.jpg"),
    ("Pawl Bunyan", "https://commons.wikimedia.org/wiki/File:K%C3%A4tzchen.JPG#/media/File:K%C3%A4tzchen.JPG"),
]

# Create your views here.

def get_next_cat(request):
    index = request.session.get('index', 1)

    cat = CATS[index]
    data = {
        'name': cat[0],
        'image': cat[1],
    }
    json = dumps(data)

    index += 1
    if index > len(CATS):
        index = 1
    request.session['index'] = index

    return HttpResponse(json, content_type='application/json')
