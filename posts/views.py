from django.http.response import HttpResponse
from django.shortcuts import render
import time
import json
# Create your views here.
def index(request):
    return render(request , "posts/index.html")

def getPosts(request, start, end):
    posts =[]
    for i in range(start,end+1):
        posts.append(f"#Post{i}")
    print(posts)

    time.sleep(1)

    posts = json.dumps(posts)
    return HttpResponse(posts)