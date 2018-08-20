from django.shortcuts import render
from .models import Video
from .form import VideoForm

def showvideo(request):

    lastvideo= Video.objects.order_by('-pk')[0]
    defaultvid = Video.objects.first()
    videofile= lastvideo.videofile
    
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context= {
        'videofile': videofile,
              'form': form,
              'defaultvid': defaultvid
              }
    
    return render(request, "videos.html", context)
