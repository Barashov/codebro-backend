from posts.models import Posts


def get_posts_with_category(pk):
    return Posts.objects.filter(categories=pk)


def get_all_posts():
    return Posts.objects.all()


def get_post_with_pk(pk):
    try:
        return Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return
