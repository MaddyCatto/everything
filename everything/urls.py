from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def quests(request):
    return HttpResponse('yesyesyes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quests/', quests, name="quests"),
    path('quests/', quests, name="quests"),
]
