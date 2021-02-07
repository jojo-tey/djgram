from django.views.generic.base import TemplateView
# TemplateView= 템플릿이 주어지면 해당 템플릿으로 렌더링
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from contents.models import Content, FollowRelation


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        user = self.request.user
        followees = FollowRelation.objects.filter(
            follower=user).values_list('followee__id', flat=True)
        lookup_user_ids = [user.id] + list(followees)
        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(
            user__id__in=lookup_user_ids
        )

        return context


@method_decorator(login_required, name='dispatch')
class RelationView(TemplateView):

    template_name = 'relation.html'

    def get_context_data(self, **kwargs):
        context = super(RelationView, self).get_context_data(**kwargs)

        user = self.request.user

        # 내가 팔로우하는 사람들
        try:
            followers = FollowRelation.objects.get(
                follower=user).followee.all()
            context['followees'] = followers
            context['followees_ids'] = list(
                followers.values_list('id', flat=True))

        except FollowRelation.DoesNotExist:
            pass

        context['followers'] = FollowRelation.objects.select_related(
            'follower').filter(followee__in=[user])

        return context
