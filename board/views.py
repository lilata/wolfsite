from django.shortcuts import render, redirect, reverse
from django.http import Http404, HttpResponseServerError
from .models import Thread, Reply
# Create your views here.
def main(request):
    threads = Thread.objects.all()
    return render(request, 'board/index.html',{
        "threads": threads,
    })

def thread(request, thread_id: str):
    thread_id = int(thread_id)
    t = Thread.objects.filter(pk=thread_id).first()
    if t is None:
        return Http404()
    else:
        return render(request, 'board/thread.html', {"thread": t})

def add_thread(request):
    if request.method == 'GET':
        return render(request, 'board/add_thread.html')
    if request.method == 'POST':
        text = request.POST.get('text')
        img = request.FILES.get('file')
        if request.user.is_authenticated:
            t = Thread(user=request.user, image=img, text=text)
        else:
            t = Thread(image=img, text=text)
        t.save()
        t.refresh_from_db()
        return redirect(reverse('board_thread', kwargs={
            "thread_id": t.pk
        }))

def add_reply(request):
    if request.method == 'GET':
        belongs_to_pk = request.GET.get('belongs_to_pk')
        if not belongs_to_pk:
            raise ValueError('invalid thread primary key')
        return render(request, 'board/add_reply.html', {
            'belongs_to_pk': belongs_to_pk
        })
    if request.method == 'POST':
        belongs_to_pk = request.POST.get('belongs_to_pk')
        text = request.POST.get('text')
        img = request.FILES.get('file')
        if request.user.is_authenticated:
            r = Reply(user=request.user,
                      image=img,
                      text=text,
                      belonging_thread_id=belongs_to_pk)
        else:
            r = Reply(image=img,
                      text=text,
                      belonging_thread_id=belongs_to_pk)
        r.save()
        return redirect(reverse('board_thread', kwargs={
            "thread_id": belongs_to_pk
        }))