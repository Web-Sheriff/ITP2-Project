from django.shortcuts import render
from .forms import LoginForm, SignUpForm

# Create your views here.
"""
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
"""
def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = SignUpForm()
	return render(request, 'users/signup.html', {'form': form})

