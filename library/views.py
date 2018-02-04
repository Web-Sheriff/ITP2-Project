from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def books(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = LoginForm()
    return render(request, 'library/libsystem.html', {'form': form})