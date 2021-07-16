from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index (request):
    question_list = Question.objects.order_by('-create_date')   # create_date = 정방향, -create_date = 역방향
    context = {'question_list' : question_list} # render 함수가 템플릿을 HTML로 변환하는 과정에서 사용되는 데이터
    return HttpResponse("Pybo에 오신것을 환영합니다!")
