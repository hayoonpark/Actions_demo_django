from django.urls import path

from actions_demo.views import MemoAPIView

demo_url_patterns = [
    path("", MemoAPIView.as_view())
]