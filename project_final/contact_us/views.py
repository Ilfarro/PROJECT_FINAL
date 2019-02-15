from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib import messages

def contact_us(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Terima kasih atas komentar anda.. :)")
            return redirect('contact_us')
    else:
        form = PostForm()
    return render(request, 'contact_us/contact_us.html', {'form':form})