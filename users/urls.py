from django.conf.urls import patterns, url, include
#from users.views import UsersMeView,  UsersMeLanguage
import views

router = ExtendedSimpleRouter()
router.register(r'users', UsersView)

urlpatterns = patterns('',
                       url(r'^users/me/$', views.UsersMeView.as_view()),
                       url(r'^users/me/language/$', views.UsersMeLanguage.as_view()),
                       url(r'^', include(router.urls))
                       )

