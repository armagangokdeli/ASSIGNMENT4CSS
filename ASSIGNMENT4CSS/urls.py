from django.conf.urls import include, url,patterns
from assignment4 import views

urlpatterns = [
    url(r'^addteacher/$',views.addteacher),
    url(r'^all-teachers/$',views.all_teachers),
    url(r'^addstudent/$',views.addstudent),
    url(r'^all-students/$',views.all_student),
    url(r'^addcourse/$',views.addcourse),
    url(r'^all-courses/$',views.all_course),
]