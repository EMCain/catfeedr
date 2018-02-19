from json import dumps

from django.http import HttpResponse

CATS = [
    ("Deadmeow5", "https://upload.wikimedia.org/wikipedia/commons/4/47/CatScratch.JPG"),
    ("Alan Purring", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Chmee2.jpg/1200px-Chmee2.jpg"),
    ("Cats Domino", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Henri%C3%ABtte_Ronner-Knip_-_Katjesspel.jpg/1200px-Henri%C3%ABtte_Ronner-Knip_-_Katjesspel.jpg"),
    ("Kevin Purrant", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Pa013767.jpg/1200px-Pa013767.jpg"),
    ("Pawl Bunyan", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/K%C3%A4tzchen.JPG/1200px-K%C3%A4tzchen.JPG"),
]


def get_next_cat(request):
    """
    return the next cat (name and image URL) in the list.
    """
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

def reset_index(request):
    """
    reset the index to start again at the first cat.
    """
    if request.POST:
        request.session['index'] = 1

    return HttpResponse('', 201)
