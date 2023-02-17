from posts.models import Posts
from users.models import User


def get_posts_with_category(pk):
    return Posts.objects.filter(categories=pk)


def get_all_posts():
    return Posts.objects.all()


def get_post_with_pk(pk):
    try:
        return Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return


def get_following_posts(user):
    if user is not None:
        posts = Posts.objects.filter(followers=user)
        if posts is not None and len(posts) != 0:
            return posts
    return


def follow_post(post: Posts, user: User):
    post.followers.add(user)
