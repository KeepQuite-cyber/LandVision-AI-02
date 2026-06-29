from django.urls import path

from .views import AIChatAPIView

app_name = "ai"

urlpatterns = [

    path(
        "ai/chat/",
        AIChatAPIView.as_view(),
        name="chat"
    ),

]