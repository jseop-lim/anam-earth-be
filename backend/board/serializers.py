from rest_framework import serializers
from board.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    댓글 목록, 생성
    """
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'username', 'post', 'content', 'created_at']  # TODO user


class CommentUpdateSerializer(serializers.ModelSerializer):
    """
    댓글 상세, 수정
    """
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content']  # TODO user
        # read_only_fields = ['user']  # TODO user


class PostListSerializer(serializers.ModelSerializer):
    """
    게시글 목록에서 출력되는 정보
    """
    class Meta:
        model = Post
        fields = ['id', 'username', 'subject', 'created_at']  # TODO user


class PostDetailSerializer(serializers.ModelSerializer):
    """
    게시글 상세에서 출력되는 정보
    """
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'subject', 'content', 'created_at', 'comments']  # TODO user
        # read_only_fields = ['user']  # TODO user
