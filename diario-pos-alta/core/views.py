from django.shortcuts import render, redirect
from .models import Paciente, RegistroDiario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/home.html')

@login_required
def listar_pacientes(request):
    pacientes = Paciente.objects.filter(usuario=request.user)

    contexto = {
        'pacientes': pacientes
    }

    return render(request, 'core/pacientes.html', contexto)

@login_required
def cadastrar_paciente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        diagnostico = request.POST.get('diagnostico')
        data_alta = request.POST.get('data_alta')

        paciente = Paciente(
            usuario=request.user,
            nome=nome,
            idade=idade,
            diagnostico=diagnostico,
            data_alta=data_alta
        )

        paciente.save()

        return redirect('pacientes')

    return render(request, 'core/cadastrar_paciente.html')

@login_required
def detalhe_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    registros = RegistroDiario.objects.filter(paciente=paciente).order_by('-data_registro')

    contexto = {
        'paciente': paciente,
        'registros': registros
    }

    return render(request, 'core/detalhe_paciente.html', contexto)

@login_required
def cadastrar_registro(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if request.method == 'POST':
        temperatura = request.POST.get('temperatura')
        pressao_arterial = request.POST.get('pressao_arterial')
        horas_sono = request.POST.get('horas_sono')
        frequencia_cardiaca = request.POST.get('frequencia_cardiaca') or None
        frequencia_respiratoria = request.POST.get('frequencia_respiratoria') or None
        glicemia = request.POST.get('glicemia') or None

        alimentacao = request.POST.get('alimentacao')
        locomocao = request.POST.get('locomocao')
        transferencia = request.POST.get('transferencia')
        banho = request.POST.get('banho')
        vestir_se = request.POST.get('vestir_se')
        observacoes = request.POST.get('observacoes')

        registro = RegistroDiario(
            paciente=paciente,
            temperatura=temperatura,
            pressao_arterial=pressao_arterial,
            horas_sono=horas_sono,
            frequencia_cardiaca=frequencia_cardiaca,
            frequencia_respiratoria=frequencia_respiratoria,
            glicemia=glicemia,
            alimentacao=alimentacao,
            locomocao=locomocao,
            transferencia=transferencia,
            banho=banho,
            vestir_se=vestir_se,
            observacoes=observacoes
        )

        registro.save()

        return redirect('detalhe_paciente', paciente_id=paciente.id)

    contexto = {
        'paciente': paciente
    }

    return render(request, 'core/cadastrar_registro.html', contexto)

@login_required
def detalhe_registro(request, registro_id):
    registro = RegistroDiario.objects.get(id=registro_id)

    contexto = {
        'registro': registro
    }

    return render(request, 'core/detalhe_registro.html', contexto)

@login_required
def editar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.idade = request.POST.get('idade')
        paciente.diagnostico = request.POST.get('diagnostico')
        paciente.data_alta = request.POST.get('data_alta')

        paciente.save()

        return redirect('detalhe_paciente', paciente_id=paciente.id)

    contexto = {
        'paciente': paciente
    }

    return render(request, 'core/editar_paciente.html', contexto)

@login_required
def excluir_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')

    contexto = {
        'paciente': paciente
    }

    return render(request, 'core/excluir_paciente.html', contexto)

@login_required
def editar_registro(request, registro_id):
    registro = RegistroDiario.objects.get(id=registro_id)

    if request.method == 'POST':
        registro.temperatura = request.POST.get('temperatura')
        registro.pressao_arterial = request.POST.get('pressao_arterial')
        registro.horas_sono = request.POST.get('horas_sono')
        registro.frequencia_cardiaca = request.POST.get('frequencia_cardiaca') or None
        registro.frequencia_respiratoria = request.POST.get('frequencia_respiratoria') or None
        registro.glicemia = request.POST.get('glicemia') or None

        registro.alimentacao = request.POST.get('alimentacao')
        registro.locomocao = request.POST.get('locomocao')
        registro.transferencia = request.POST.get('transferencia')
        registro.banho = request.POST.get('banho')
        registro.vestir_se = request.POST.get('vestir_se')
        registro.observacoes = request.POST.get('observacoes')

        registro.save()

        return redirect('detalhe_registro', registro_id=registro.id)

    contexto = {
        'registro': registro
    }

    return render(request, 'core/editar_registro.html', contexto)

@login_required
def excluir_registro(request, registro_id):
    registro = RegistroDiario.objects.get(id=registro_id)

    paciente_id = registro.paciente.id

    if request.method == 'POST':
        registro.delete()

        return redirect('detalhe_paciente', paciente_id=paciente_id)

    contexto = {
        'registro': registro
    }

    return render(request, 'core/excluir_registro.html', contexto)

def login_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('pacientes')
        else:
            contexto = {
                'erro': 'Usuário ou senha inválidos.'
            }
            return render(request, 'core/login.html', contexto)

    return render(request, 'core/login.html')


def logout_usuario(request):
    logout(request)
    return redirect('login')

