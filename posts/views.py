from .serializers import PostCreateSerializer,\
                         CategorySerializer,\
                         PostPreviewSerializer,\
                         FullPostViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import permissions
from rest_framework.decorators import api_view
from .logics.posts import get_posts_with_category,\
                          get_all_posts,\
                          get_post_with_pk,\
                          get_following_posts,\
                          follow_post
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from .doc import *
from .models import Categories


@swagger_auto_schema(method='get', **get_categories_doc)
@api_view()
def get_categories(request):
    categories = CategorySerializer(Categories.objects.all(), many=True).data
    return Response(status=200, data=categories)


class PostAPIView(APIView):
    parser_classes = (MultiPartParser, )
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(**post_create_doc)
    @transaction.atomic
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data,
                                          context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=201, data=serializer.data)
        return Response(status=400)


class PostCategoriesAPIView(APIView):
    """
    get posts preview with categories
    """
    @swagger_auto_schema(**get_posts_with_category_doc)
    def get(self, request, pk):
        serializer = PostPreviewSerializer(get_posts_with_category(pk), many=True)
        return Response(status=200, data=serializer.data)


class AllPostsAPIView(APIView):
    @swagger_auto_schema(**get_categories_doc)
    def get(self, request):
        serializer = PostPreviewSerializer(get_all_posts(), many=True)
        return Response(status=200, data=serializer.data)


@swagger_auto_schema(methods=['get'], **get_post_doc)
@api_view()
def post_view(request, pk):
    post = get_post_with_pk(pk)
    if post is not None:
        return Response(status=200,
                        data=FullPostViewSerializer(post).data)
    return Response(status=404)


class FollowingPostsAPIView(APIView):
    """
    просмотр всех избранных постов
    - headers: Authorization Token dlfasldflasdfjlsadfa
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        data = get_following_posts(request.user)
        if data is not None and len(data) != 0:
            return Response(status=200,
                            data=PostPreviewSerializer(instance=data,
                                                       many=True).data)
        return Response(status=400)


class FollowPost(APIView):
    """
    добавить пост в избранное
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, post_pk):
        post = get_post_with_pk(post_pk)
        if post is not None:
            follow_post(post, request.user)
            return Response(status=200)
        return Response(status=400)

