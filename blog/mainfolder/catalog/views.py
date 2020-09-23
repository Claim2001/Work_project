from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .models import Article, Like, Comments, Profile
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RenewArticleForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify


def index(request):
    num_art = Article.objects.all().count()

    return render(request, 'index.html', context={'num_art': num_art},)


class ArticleListView(generic.ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.all().order_by('article_text')


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'catalog/article_detail.html'
    model = Article
    slug_url_kwarg = "slug"
    queryset = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context["form_comments"] = CommentForm
        return context

    # def get_queryset(self):
    #     context = super(ArticleCreateView, self)
    #     context["form_comments"] = CommentForm
    #     return context


    # def get(self, request, pk):
    #     context = {}
    #     comments = Comments.objects.filter(comments_article__slug=pk)
    #     context["comments"] = comments
    #     form_comments = CommentForm
    #     context["article"] = get_object_or_404(Article, slug=pk)
    #     context["form_comments"] = form_comments
    #     context["like_count"] = Like.objects.filter(article__slug = pk).count()
    #     return render(request, 'catalog/article_detail.html', context)


class AddComment(LoginRequiredMixin, generic.View):

    def post(self, request, art_id):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.comments_article = Article.objects.get(id=art_id)
                comment.comments_user_id = request.user.id
                form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteComment(LoginRequiredMixin, generic.View):

    def post(self, request, comment_id):
        comment = get_object_or_404(Comments, pk=comment_id)
        if request.user.id == comment.comments_user.id:
            comment.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class OnlikeView(LoginRequiredMixin, generic.View):

    def post(self, request, pk):
        if Like.objects.filter(article_id=pk, user_id=request.user.id):
            Like.objects.filter(article_id=pk, user_id=request.user.id).delete()
        else:
            Like.objects.create(article_id=pk, user_id=request.user.id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@permission_required
def renew_art_staff(request, pk):
    art_text = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = RenewArticleForm(request.POST)
        if form.is_valid():
            art_text.article_text = form.cleaned_data['new_text']
            art_text.save()
            return HttpResponseRedirect(reverse('articles'))
    else:
        form = RenewArticleForm(initial={'new_text': art_text})
    return render(request, 'catalog/art_renew_staff.html', {'form': form, 'article': art_text})


class CreateUserView(generic.View):

    def get(self, request):
        return render(request, 'registration/registration.html')

    def post(self, request):
        user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        Profile.objects.create(user=user, level=3)
        return HttpResponseRedirect(reverse('articles'))


class ArticleCreateView(generic.CreateView):
    # template_name = 'catalog/article_form.html'
    # def get(self):
    #     return HttpResponseRedirect(reverse('index'))
    model = Article
    fields = ['article_title', 'article_additional_title', 'article_text', 'article_image']


class ArticleUpdateView(UpdateView):
    model = Article
    slug = slugify('article_title')
    fields = ['article_title', 'article_additional_title', 'article_text', 'article_image']


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles')

