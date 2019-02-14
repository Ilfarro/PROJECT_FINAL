from django.shortcuts import render, redirect
from .forms import PostForm

def contact_us(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form = PostForm()
    return render(request, 'contact_us/contact_us.html', {'form':form})