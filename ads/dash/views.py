from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from home.models import Confirm, Password, Referral
from .models import Yt, Person, Viewed
import datetime

def dash(request):
    if request.user.is_authenticated:
        tot = 0
        per = Person.objects.filter(username=request.user.username).first()
        ref = Referral.objects.filter(username=request.user.username).count()
        yy = Yt.objects.filter(username=request.user.username)
        yt = yy.count()
        for y in yy:
            tot += y.views 

        context = {
            'pts': per.points,
            'ref': ref,
            'yt':yt,
            'tot':tot
        }
        return render(request, "dash_index.html", context)

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")

def earn_points(request):
    if request.user.is_authenticated:
        yt = Yt.objects.all()
        yy = dict()
        arr = ['Vlog', 'Interview Q/A video', 'Tutorial', 'Product Review', 'Video Testimonial', 'Animation Video', 'Event video', 'Brand Film',
            'Unboxing Video', 'Educational Video', 'Live Stream', 'Recipe video', 'Favorites/Best of video', 'Video Game Video', 'Collection Video',
            'Comedy skit', 'Prank video']

        for k in arr:
            yy[k] = list()

        for y in yt:
            if y.views >= y.demand:
                y.delete()
            else:
                if Viewed.objects.filter(username=request.user.username).filter(video_id=y.video_id).exists():
                    vi = Viewed.objects.filter(username=request.user.username).filter(video_id=y.video_id).first()
                    x = datetime.datetime.strptime(vi.time, '%Y-%m-%d %H:%M:%S.%f')
                    if datetime.datetime.now() >= x:
                        yy[y.category].append(y)

                else:
                    yy[y.category].append(y)

        context = {
            'yy': yy,
            'arr':arr
        }
        print(yy)
        return render(request, "earn_points.html", context)

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")

def category(request, cat):
    if request.user.is_authenticated:
        arr = ['vlog', 'interview-qa-video', 'tutorial', 'product-review', 'video-testimonial', 'animation-video', 'event-video', 'brand-film',
            'unboxing-video', 'educational-video', 'live-stream', 'recipe-video', 'favoritesbest-of-video', 'video-game-video', 'collection-video',
            'comedy-skit', 'prank-video']
        if cat not in arr:
            messages.info(request, "This is not a valid category")
            return redirect("earn_points")
        else:
            p = 0
            xx = -1
            f = 0
            ar = ['Vlog', 'Interview Q/A video', 'Tutorial', 'Product Review', 'Video Testimonial', 'Animation Video', 'Event video', 'Brand Film',
                'Unboxing Video', 'Educational Video', 'Live Stream', 'Recipe video', 'Favorites/Best of video', 'Video Game Video', 'Collection Video',
                'Comedy skit', 'Prank video']
            for cc in arr:
                if f == 0:
                    xx += 1
                    if cc == cat:
                        p = xx
                        f = 1
                else:
                    break

            yt = Yt.objects.filter(category=ar[p])
            yy = list()
            for y in yt:
                if y.views >= y.demand:
                    y.delete()
                else:
                    if Viewed.objects.filter(username=request.user.username).filter(video_id=y.video_id).exists():
                        vi = Viewed.objects.filter(username=request.user.username).filter(video_id=y.video_id).first()
                        x = datetime.datetime.strptime(vi.time, '%Y-%m-%d %H:%M:%S.%f')
                        if datetime.datetime.now() >= x:
                            yy.append(y)

                    else:
                        yy.append(y)


            context = {
                'yt': yy
            }
            return render(request, "category.html", context)
        

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")

def watch_video(request, video_id):
    if request.user.is_authenticated:
        yt = Yt.objects.filter(video_id=video_id).first()
        return render(request, "watch_video.html", {'p':yt})

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")

def create_views(request):
    if request.user.is_authenticated:
        per = Person.objects.get(username=request.user.username)
        if request.method == "POST":
            if not request.POST['video_url'] or not request.POST['demand']:
                messages.info(request, "Please fill all the required fields!")
                return redirect("create_views")

            arr = ['Vlog', 'Interview Q/A video', 'Tutorial', 'Product Review', 'Video Testimonial', 'Animation Video', 'Event video', 'Brand Film',
            'Unboxing Video', 'Educational Video', 'Live Stream', 'Recipe video', 'Favorites/Best of video', 'Video Game Video', 'Collection Video',
            'Comedy skit', 'Prank video']

            category = request.POST['category']
            video_url = request.POST['video_url']
            demand = int(request.POST['demand'])
            video_id = video_url.split('watch?v=')[1].split("&")[0]

            if category not in arr:
                messages.info(request, "Please select a video Category!")
                return redirect("create_views")

            if per.points <= demand*10:
                mess = "You dont have engough Points to redeem " + demand + "views."
                messages.info(request, mess)
                return redirect("create_views")
            else:
                per.points -= demand*10
                per.save()
            if Yt.objects.filter(video_id=video_id):
                yt = Yt.objects.get(video_id=video_id)
                yt.category = category
                yt.demand += demand
                yt.save()
                messages.info(request, "Video views demand Edited")
                return redirect("dash")

            else:
                yt = Yt.objects.create(username=request.user.username, demand=demand, video_id=video_id, views=0, category=category)
                yt.save()
                messages.info(request, "Video Boosted!")
                return redirect("dash")

        context = {
            'per': per
        }
        return render(request, "add_views.html", context)

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")

def reward(request):
    if request.user.is_authenticated:
        per = Person.objects.get(username=request.user.username)
        if request.method == "POST":
            video_id = request.POST['video_id']
            if Yt.objects.filter(video_id=video_id).exists():
                yt = Yt.objects.filter(video_id=video_id).first()
                yt.views += 1
                yt.save()
                per.points += 10
                per.save()
                if Viewed.objects.filter(username=request.user.username).filter(video_id=video_id).exists():
                    vi = Viewed.objects.filter(username=request.user.username).filter(video_id=video_id).first()
                    vi.time = str(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                    vi.save()

                else:
                    x = str(datetime.datetime.now() + datetime.timedelta(minutes = 30))
                    vi = Viewed.objects.create(username=request.user.username, video_id=video_id, time=x)
                    vi.save()

            return redirect("earn_points")
        
    else:
        messages.info(request, "You need to login first!")
        return redirect("login")


def my_videos(request):
    if request.user.is_authenticated:
        yt = Yt.objects.filter(username=request.user.username)
        context = {
            'yt':yt
        }
        return render(request, "my_videos.html", context)

    else:
        messages.info(request, "You need to login first!")
        return redirect("login")