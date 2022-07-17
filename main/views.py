from logging.config import valid_ident
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MuscleGroups, Exercises
from .forms import Gurate
from django.urls import reverse
import random
# Create your views here.


def base(response):
    mg = MuscleGroups()
    return render(response, "main/index.html", {"musclegroups": mg})


def chest(response):
    return render(response, "main/chest.html", {})


def shoulders(response):
    return render(response, "main/shoulders.html", {})


def triceps(response):
    return render(response, "main/triceps.html", {})


def back(response):
    return render(response, "main/back.html", {})


def biceps(response):
    return render(response, "main/biceps.html", {})


def legs(response):
    return render(response, "main/legs.html", {})


def gurate(response):
    mg = MuscleGroups.objects.all()
    form = Gurate()
    args = {'mg': mg, 'form': form}
    if response.method == "POST":
        id_list = response.POST.getlist('boxes')
        # getting how much time the user can spend on working out
        time = response.POST['time']
        args['time'] = time
        global global_time

        def global_time():
            return time
        # Uncheck all events
        mg.update(complete=False)
        # Update the database
        for group in id_list:
            MuscleGroups.objects.filter(name=group).update(complete=True)

        filtered = MuscleGroups.objects.filter(complete=True)
        # whatever muscle group user wants
        args['filtered'] = filtered

        # create argument key,val pair that has exercises
        exercises = []
        for group in filtered:
            name = group.name
            for exercise in group.exercises_set.all():
                exercises.append(exercise)

        # randomized order of exercise display
        random.shuffle(exercises)
        # initialize selected list every time
        args['selected'] = []

        global global_exercises, global_args

        def global_exercises():  # globalize both variables
            return exercises

        def global_args():
            return args
        return redirect(reverse(pick))

    else:  # if not a post request
        return render(response, "main/gurate.html", args)


def pick(response):
    exercises = global_exercises()  # exercises to choose from
    args = global_args()
    args['exercise'] = exercises[0]  # initialize argument
    # going through each exercise in the loop, seeing what user wants
    while len(exercises)-1 != 0 and int(args['time']) > 0:
        if response.method == 'POST':
            if response.POST.get('yes'):
                args['time'] = int(args['time']) - exercises[0].time
                args['selected'].append(exercises.pop(0))
                if int(args['time']) <= 0:
                    return redirect(reverse(display))
                pass
            elif response.POST.get('no'):
                exercises.pop(0)
                pass
            args['exercise'] = exercises[0]
            # each iteration
            return render(response, "main/pick.html", args)
        else:  # before anything is selected
            return render(response, "main/pick.html", args)

    if len(exercises)-1 == 0:
        args['exercise'] = exercises[0]
        if response.method == 'POST':
            if response.POST.get('yes'):
                args['selected'].append(exercises.pop(0))
                pass
            elif response.POST.get('no'):
                exercises.pop(0)
                pass
            return redirect(reverse(display))


def display(response):
    args = global_args()

    total_time = 0
    for exercise in args['selected']:
        total_time += exercise.time

    args['total_time'] = total_time
    return render(response, 'main/display.html', args)
