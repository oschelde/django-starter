from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserPageView(LoginRequiredMixin, TemplateView):
    template_name = "users/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "user"
        return context


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "profile"
        return context
