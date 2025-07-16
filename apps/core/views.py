from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    context = {}
    if request.method == 'POST':
        # Pega os dados do formulário
        username_form = request.POST.get('username')
        password_form = request.POST.get('password')

        # Autentica o usuário contra o banco de dados
        user = authenticate(request, username=username_form, password=password_form)

        if user is not None:
            # Se o usuário for válido, faz o login
            login(request, user)

            # Verifica a qual grupo o usuário pertence
            if user.groups.filter(name='Grupo1').exists():
                return redirect('pagina1')
            elif user.groups.filter(name='Grupo2').exists():
                return redirect('pagina2')
            else:
                # Se não pertencer a nenhum grupo, pode redirecionar para um painel padrão ou mostrar erro
                return redirect('login') # Por simplicidade, volta ao login
        else:
            # Se usuário ou senha forem inválidos
            context['error_message'] = 'Usuário ou senha inválidos.'
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)

@login_required
def pagina1_view(request):
    # O decorator @login_required protege esta página
    return render(request, 'pagina1.html')

@login_required
def pagina2_view(request):
    # O decorator @login_required protege esta página
    return render(request, 'pagina2.html')

# A view de logout não é mais necessária aqui, usaremos a do próprio Django
