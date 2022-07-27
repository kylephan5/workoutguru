from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from logging.config import valid_ident
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MuscleGroups, Exercises
from .forms import Gurate
from django.urls import reverse
from django.contrib.auth import get_user_model, login
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


def about(response):
    return render(response, "main/about.html", {})


def gurate(response):
    mg = MuscleGroups.objects.filter(email__isnull=True)
    form = Gurate()
    args = {'mg': mg, 'form': form}
    if response.method == "POST":
        id_list = response.POST.getlist('boxes')
        # getting how much time the user can spend on working out
        # time = response.POST['time']
        # args['time'] = time
        # global global_time

        # def global_time():
        # return time
        # Uncheck all events
        mg.update(complete=False)
        # Update the database
        # Creating a user
        User = get_user_model()
        # logging in the user, if cant login then we create a new user and log them in

        try:  # if user is in database, log the user in and update their time to be whatever they put in
            login(response, User.objects.get(
                email=response.POST['email']))
            User.objects.update(
                time=response.POST['time'], left=0, right=1, current=0)
        except:  # if user is not in database, create the user and log them in
            User.objects.create_user(
                email=response.POST['email'], time=response.POST['time'], left=0, right=1, current=0)
            login(response, User.objects.get(
                email=response.POST['email'], time=response.POST['time'], left=0, right=1, current=0))

        # for mg in MuscleGroups.objects.all():  # if muscle group duplicate exists for said user already, then delete it
            # if mg.email == response.user.email:
            # MuscleGroups.objects.get(
            # name=mg, email=response.user.email).delete()

        Exercises.objects.filter(email=response.user).delete()
        for group in id_list:
            copy = MuscleGroups.objects.get(  # copy will hold the muscle group
                name=group, email__isnull=True)

            # if there is a pre-existing exercise with email attached, make selected false
            copy.exercises_set.filter(
                email=response.user, selected=True).delete()
            copy.exercises_set.filter(
                email=response.user, selected=False).delete()

            for exercise in copy.exercises_set.all():  # getting the normal exercises, with no email attached

                copy.exercises_set.get_or_create(  # creating/getting the new updated exercises, with an email attached
                    email=response.user, name=exercise, musclegroup=exercise.musclegroup, time=exercise.time, image=exercise.image, reps=exercise.reps, selected=False)
                copy.save()
        return redirect(reverse(pick))

    else:  # if not a post request
        return render(response, "main/gurate.html", args)


def pick(response):
    # exercises = global_exercises()  # exercises to choose from
    args = []
    # 2 pointer iterate through query set
    User = get_user_model()
    User.objects.filter(email=response.user).update(
        right=len(Exercises.objects.filter(email=response.user))-1)
    while response.user.current < response.user.right:
        if response.method == 'POST':
            if response.POST.get('yes'):
                response.user.time = response.user.time - Exercises.objects.filter(email=response.user)[
                    response.user.current].time
                User.objects.filter(email=response.user).update(
                    time=response.user.time)
                # updating selected to be True
                Exercises.objects.filter(
                    name=Exercises.objects.filter(email=response.user)[response.user.current].name, email=response.user).update(selected=True)
                if response.user.time <= 0:
                    return redirect(reverse(display))
                pass
            elif response.POST.get('no'):
                pass
            elif response.POST.get('done'):
                return redirect(reverse(display))
            # Exercises.objects.filter(email=response.user).first().delete()
            # print(response.user.right)
            # print(response.user.right)
            response.user.current += 1
            User.objects.filter(email=response.user).update(
                current=response.user.current)
            args = {'exercise': Exercises.objects.filter(
                email=response.user)[response.user.current], 'time': response.user.time}
            if response.user.current < response.user.right:
                args['nextexercise'] = Exercises.objects.filter(
                    email=response.user)[response.user.current+1]
                args['exercisesleft'] = response.user.right - \
                    response.user.current
            else:
                args['nextexercise'] = 'None'
                args['exercisesleft'] = 0

            return render(response, "main/pick.html", args)
        else:
            args = {'exercise': Exercises.objects.filter(email=response.user)[
                response.user.current], 'time': response.user.time, 'nextexercise': Exercises.objects.filter(
                    email=response.user)[response.user.current+1], 'exercisesleft': len(Exercises.objects.filter(email=response.user))-1}
            return render(response, "main/pick.html", args)

    if response.user.current == response.user.right:
        if response.method == 'POST':
            if response.POST.get('yes'):
                response.user.time = response.user.time - Exercises.objects.filter(email=response.user)[
                    response.user.current].time
                # updating selected to be True
                Exercises.objects.filter(
                    name=Exercises.objects.filter(email=response.user)[response.user.current].name, email=response.user).update(selected=True)
                pass
            elif response.POST.get('no'):
                pass
        return redirect(reverse(display))
        # args['exercise'] = exercises[0]  # initialize argument
        # going through each exercise in the loop, seeing what user wants


def display(response):
    if response.method == 'POST':
        if response.POST.get('email'):
            args = {'name': response.user, 'selected': Exercises.objects.filter(email=response.user, selected=True)}
            template = render_to_string('main/email.html', args)
            email = EmailMessage(
                'Your Workout Summary - Workout Guru',
                template,
                settings.EMAIL_HOST_USER,
                [response.user],
            )
            email.fail_silently = False
            email.send()

            return render(response, 'main/display.html', {'selected': Exercises.objects.filter(email=response.user, selected=True)})
    return render(response, 'main/display.html', {'selected': Exercises.objects.filter(email=response.user, selected=True)})
