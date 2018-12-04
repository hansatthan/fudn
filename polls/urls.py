from django.urls import path
from django.conf.urls import url


from . import views
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url('delete', views.delete, name='delete'),
    # ex: /polls/5/results/
    url('results', views.results, name='results'),
    # ex: /polls/5/vote/
    url('full', views.full, name='full'),
    url('update', views.update, name='update'),

]