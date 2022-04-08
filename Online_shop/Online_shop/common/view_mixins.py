from django.shortcuts import redirect


class RedirectToIndexPage:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)
