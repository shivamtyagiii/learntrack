from django.shortcuts import render
from .models import Goal


def goal_list(request):
    goals = Goal.objects.all().order_by("-created_at")
    return render(request, "goals/goal_list.html", {"goals": goals})
