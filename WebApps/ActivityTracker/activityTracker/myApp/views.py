from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from .models import Activity, TimeLog

# Create your views here.

# Shows a list of all of the activities and how long has been spent in hours doing each activity
# The time spent is the sum of all of the time logs for that activity.
# Each activity should have a link to the /activity/<id> page, where id is the id of the activity
# Has a link to the /new_activity page

def indexPage(request):
    activities = Activity.objects.all()
    # start_time = datetime.strptime(request.POST.get("start_time"), '%Y-%m-%dT%H:%M')
    return render(request, "myApp/index.html", {"activities": activities})

# Has a form that allows a user to create a new activity
# When the form is submitted they are redirected to the /activity/<id> page for the new activity that was just created

def new_activity(request):
    if request.method == "POST":
        params = request.POST
        activity = Activity(
            name=params.get("name")
        )

        activity.save()
        return redirect(f"/activity/{activity.id}")
    else:
        return render(request, "myApp/new_activity.html")

# Displays the name of the Activity
# Displays a list of all of the TimeLogs for the Activity.
# Each TimeLog displays how long was spent as well as the start and end times (in human-readable format)
# Displays a link to the /activity/<id>/new_timelog page

def activity(request, id):
    activity = Activity.objects.get(id=id)
    timelogs = TimeLog.objects.filter(activity=activity)
    return render(request, "myApp/activity.html", {"activity": activity, "timeLogs": timelogs})

# Displays the title of the activity
# Displays a form that the users can submit to create a new TimeLog
# Use an <input type="datetime-local"> as the inputs for the start and end times.
# When the form is submitted, redirect to the /activity/<id> page

def new_timelog(request, id):
    activityObj = Activity.objects.get(id=id)
    if request.method == "POST":
        # print(request.POST.get("start_date"))
        startTime = datetime.strptime(request.POST.get("start_time"), '%Y-%m-%dT%H:%M')
        endTime = datetime.strptime(request.POST.get("end_time"), '%Y-%m-%dT%H:%M')
        timelog = TimeLog(
            start_time = startTime,
            end_time = endTime,
            activity = activityObj,
        )
        timelog.save()
        return redirect(f"/activity/{id}/")

    else:
        # activity = Activity.objects.get(id=id)
        return render(request, "myApp/new_timelog.html", {"activity": activityObj})
