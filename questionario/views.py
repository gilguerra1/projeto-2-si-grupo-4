from django.shortcuts import render
from .models import Question, QuestionnaireResponse, Choice
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def questionario_view(request):
    if request.method == 'POST':
        # Extrai as respostas da requisição POST
        try:
            respostas = {
                key.replace('question_', ''): int(value)  # Extrai apenas o ID da questão
                for key, value in request.POST.items()
                if key.startswith('question_')
            }
            feedback = request.POST.get('feedback', '')

            # Salva as respostas
            salvar_respostas(request, respostas, feedback)

            return JsonResponse({'message': 'Respostas salvas com sucesso!'}, status=200)
        except ValueError as e:
            return JsonResponse({'error': f'Erro ao processar respostas: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # Busca todas as questões e suas escolhas relacionadas
    questions = Question.objects.prefetch_related('choices').all()
    return render(request, 'questionario.html', {'questions': questions})


def salvar_respostas(request, respostas, feedback=None):
    """
    Função para salvar as respostas do questionário no banco de dados.
    """
    fake_class_group_id = 1  # Substitua pelo ID real do grupo de classe

    try:
        # Calcula a pontuação total com base nas respostas
        total_score = sum(
            Choice.objects.get(id=choice_id).value for choice_id in respostas.values()
        )

        # Cria o registro de respostas no banco de dados
        response = QuestionnaireResponse.objects.create(
            student_id=request.user.id,  # ID do usuário logado
            class_group_id=fake_class_group_id,
            answers=respostas,
            feedback=feedback,
            total_score=total_score,
        )
        print("Resposta salva com sucesso!")
        return response

    except Choice.DoesNotExist:
        print("Erro: Alguma das respostas fornecidas não é válida.")
        raise
    except Exception as e:
        print(f"Erro ao salvar o questionário: {str(e)}")
        raise
