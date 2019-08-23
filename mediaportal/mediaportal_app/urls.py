from django.urls import path, re_path
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .views import (CategoryListView, CategoryDetailView,
                    ArticleDetailView, DynamicArticleImageView,
                    CreateCommentView, DisplayArticlesByCategoryView,
                    UserReactionView, RegistrationView,
                    LoginView, UserAccountView,
                    AddArticleToFavorites, RemoveArticleFromFavorites,
                    SearchView)


urlpatterns = [
    path('', CategoryListView.as_view(), name='base_view'),
    path('category/<category_slug>', CategoryDetailView.as_view(), name='category_detail'),
    path('<category_slug>/<article_slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('show_article_image', DynamicArticleImageView.as_view(), name='article_image'),
    path('add_comment', CreateCommentView.as_view(), name='add_comment'),
    path('display_articles_by_category', DisplayArticlesByCategoryView.as_view(), name='articles_by_category'),
    path('user_reaction', UserReactionView.as_view(), name='user_reaction'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login_view'),
    path('add_to_favorites', AddArticleToFavorites.as_view(), name='add_to_favorites'),
    path('remove_from_favorites', RemoveArticleFromFavorites.as_view(), name='remove_from_favorites'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('base_view')), name='logout_view'),
    path('search', SearchView.as_view(), name='search_view'),
    re_path('user_account/(?P<user>[-\w]+)/$', UserAccountView.as_view(), name='account_view'),
]

