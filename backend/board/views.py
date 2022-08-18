from rest_framework import viewsets

from board.models import Post, Comment
from board import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        else:  # create/retrieve/update/destroy
            return serializers.PostDetailSerializer

    # POST 요청 시에 호출되며, serializer로 쓰기가 불가능하므로 인스턴스에 직접 저장
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    # http_method_names = ['post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def get_serializer_class(self):
        if self.action == 'update':
            return serializers.CommentUpdateSerializer
        else:  # create/retrieve/update/destroy
            return serializers.CommentSerializer
