# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  DetailView,
                                  DeleteView,
                                  ListView,
                                  UpdateView)
from django.shortcuts import render, get_object_or_404

from .forms import TweetModelForm
from .mixins import FormUserMixin, UserOwnerMixin
from .models import Tweet
from django.urls import reverse_lazy


class TweetCreateView(FormUserMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'create_view.html'
    success_url = '/tweet/create'

    def form_invalid(self, form):
        form.instance.user = self.request.user


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


class TweetUpdateView(UpdateView, LoginRequiredMixin, UserOwnerMixin):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "update_view.html"
    success_url = '/tweet/list'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'delete.confirm.html'
    success_url = reverse_lazy('home')


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        return context


def tweet_detail_view(request, pk=None):
    obj = get_object_or_404(Tweet, pk=pk)
    context = {
        "object": obj
    }
    return render(request, "details_view.html", context)
