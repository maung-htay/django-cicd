from django.urls import path, include
from .views import PostList, PostDetail, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("post1", PostViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("post/", PostList.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]