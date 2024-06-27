from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView, TemplateView
from django.urls import include, path, re_path
from . import views
from blog_improved.sitemaps import PostSitemap

admin_baseurl = settings.ADMIN_LOGIN_URL

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path(admin_baseurl, admin.site.urls),
    path("about/", views.about, name="about"),
    path("cv/", views.cv, name="cv"),
    re_path("^pgpkey.txt/$", TemplateView.as_view(template_name="pages/pubkey.txt", content_type='text/plain'), name="email-pubkey"),
    path("projects/", views.projects, name="projects"),
    path("license/", views.license, name="license"),
    path("services/", views.service, name="services"),
    re_path(r"^([-\w]+)/success/$", views.SuccessFormCreation.as_view(), name="success"),
    path("call-request/", views.CallRequestForm.as_view(), name="call-request"),
    path("", include("blog_improved.urls"), name="blog"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]
