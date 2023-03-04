from django.contrib import admin
from django.urls import path


def quests(request):
    return render('yesyesyes')

urlpatterns = [
    path('quests/', quests, name="quests"),
]
asdas