from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

class DynamicTemplateView(TemplateView):
    def get_template_names(self):
        return [self.kwargs['template_name']]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("leads.urls"), name="leads"),
    path('template/<str:template_name>', 
         DynamicTemplateView.as_view(),
         name='template'),
]