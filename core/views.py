from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "Welcome to LearnTrack! Your learning journey starts here."
    )