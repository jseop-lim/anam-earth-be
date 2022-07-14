from rest_framework import serializers
from board.models import Post, Comment


class CommentListSerializer(serializers.ModelSerializer):
    """
    댓글 목록, 생성
    """
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content']


class CommentUpdateSerializer(serializers.ModelSerializer):
    """
    댓글 상세, 수정
    """
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content']
        read_only_fields = ['user']


class PostListSerializer(serializers.ModelSerializer):
    """
    게시글 목록에서 출력되는 정보
    """
    class Meta:
        model = Post
        fields = ['id', 'user', 'subject', 'created_at']


class PostDetailSerializer(serializers.ModelSerializer):
    """
    게시글 상세에서 출력되는 정보
    """
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'subject', 'content', 'created_at', 'comments']
        read_only_fields = ['user']
