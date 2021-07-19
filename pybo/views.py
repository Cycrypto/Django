from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
# Create your views here.
def index (request):
    question_list = Question.objects.order_by('-create_date')   # create_date = 정방향, -create_date = 역방향
    context = {'question_list' : question_list} # render 함수가 템플릿을 HTML로 변환하는 과정에서 사용되는 데이터
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  #pk에 해당하는 건이 없으면 404 페이지 출력
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

#제네릭 뷰라는 개념 공부하기.-

def answer_create(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)


