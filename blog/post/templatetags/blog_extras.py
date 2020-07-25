from django import template

register = template.Library()

@register.filter
def add_link(value):
    body = value.body
    tags = value.hashtags.all()

    for tag in tags:
        body = body.replace(f"{tag.content}", f"<a href = '/hashtag/{tag.id}/'>{tag.content}</a>")
    return body