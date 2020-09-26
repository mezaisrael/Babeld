from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweets

# Create your views here.
def home_view(request, *args, **kwargs):
    #  return HttpResponse("<h1>Hello Wordl</h1>")
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    '''
    REST API VIEW
    return json data
    '''
    qs = Tweets.objects.all()
    tweet_list = [{"id": x.id, "content": x.content} for x in qs]

    data = {
        "response": tweet_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    return json data
    '''
    data = {
        "id": tweet_id,
        #  "image":
    }

    status = 200
    try:
        obj = Tweets.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404


    return JsonResponse(data, status=status)

