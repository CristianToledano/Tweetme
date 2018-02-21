# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView, CreateView
from django.shortcuts import render
from .forms import TweetModelForm
from .mixins import FormUserMixin
from .models import Tweet


class TweetCreateView(CreateView, FormUserMixin):
    form_class = TweetModelForm
    template_name = 'create_view.html'
    success_url = '/tweet/create'


def tweet_create_view(request):
    form = TweetModelForm(request.post or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.User
        instance.save()
    context = {
        'form': form
    }
    return render(request, 'create_view.html', context)


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "details_view.html"

    def get_object(self):
        obj = Tweet.objects.all()
        context = []
        for o in obj:
            context.append(o)
        return context


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "list_view.html"

    def get_object(self):
        return Tweet.objects.get(id=1)


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.all()
#     for o in obj:
#         context = {
#             "object": obj
#         }
#     return render(request, "details_view.html", context)
#
#
# def tweet_list_view(request):
#     context = None
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         context = {
#             "objects_list": obj
#         }
#     return render(request, "list_view.html", context)
