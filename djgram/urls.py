"""djgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.shortcuts import redirect
from contents.views import HomeView, RelationView
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "djgram Admin"
admin.site.site_title = "djgram Admin Site"
admin.site.index_title = "Hello everyone:)"


class NonUserTemplateView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        # 유저가 로그인 되어있을때 로그인이나 회원가입 페이지로 들어가려고 하면 컨텐츠 홈으로 리다이렉트
        if not request.user.is_anonymous:
            return redirect('contents_home')
        return super(NonUserTemplateView, self).dispatch(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('apis/', include('apis.urls')),
    path('', HomeView.as_view(), name='contents_home'),
    path('login/', NonUserTemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', NonUserTemplateView.as_view(template_name='register.html'), name='register'),
    path('relation/', RelationView.as_view(), name='contents_relation'),
]

# DEBUG_TOOLBAR has issue in django 3.1 // solving

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
