from django.shortcuts import render
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('nama')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username == '' or email == '' or password == '':
            messages.error(request, 'Semua kolom harus diisi.')
            return render(request, 'login.html')
        user = auth.authenticate(
            request, username=username, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Akun tidak ditemukan.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
