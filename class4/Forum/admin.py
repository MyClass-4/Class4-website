from django.contrib import admin
from Forum.models import *
# Register your models here.


class TopicAdmin(admin.ModelAdmin):
    pass


class PostingAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Topic, TopicAdmin)
admin.site.register(Posting, PostingAdmin)
admin.site.register(Comment, CommentAdmin)
