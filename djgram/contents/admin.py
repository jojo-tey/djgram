from django.contrib import admin

# from contents.models import Content, Image, FollowRelation


class ImageInline(admin.TabularInline):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('user', 'created_at',)


admin.site.register(Content, ContentAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)


class FollowRelationAdmin(admin.ModelAdmin):
    pass


admin.site.register(FollowRelation, FollowRelationAdmin)
