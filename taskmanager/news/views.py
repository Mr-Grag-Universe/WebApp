from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
    pass
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_vew.html'
    context_object_name = 'article'


def work_with_data(form):
    title = form.cleaned_data['title']
    file = open("data.txt", 'w')
    file.write(title)


def output(request):
    file = open("data.txt", "r")
    text = file.readline()
    dic = {
        'text': text,
    }
    return render(request, 'news/output.html', dic)


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            work_with_data(form)
            return redirect('output')

    form = ArticlesForm()
    data = {
        'form': form,
    }

    return render(request, 'news/create.html', data)

