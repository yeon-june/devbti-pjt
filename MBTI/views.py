from django.shortcuts import (render, redirect, get_object_or_404)

from .models import Mbti, BaseInfo, Howto, Question

# Create your views here.


def main_page(request):
    # 비정상적인 접근 막기! (초기값 다르게,, 전체 문항 안고르면 메인으로 돌려버리기)
    mbties = Mbti.objects.all()
    viewers = 0
    max_viewers = 0
    min_viewers = 10e6

    for mbti in mbties:
        viewers += mbti.view_cnt

        if max_viewers < mbti.view_cnt:
            max_viewers = mbti.view_cnt
            max_mbti = mbti.mbti_name
            max_mbti_type = mbti.mbti_type
        
        if min_viewers > mbti.view_cnt:
            min_viewers = mbti.view_cnt
            min_mbti = mbti.mbti_name
            min_mbti_type = mbti.mbti_type
    
    context = {
        'mbties' : mbties,
        'viewers' : viewers,
        'max_viewers' : max_viewers,
        'min_viewers' : min_viewers,
        'max_mbti' : max_mbti,
        'min_mbti' : min_mbti,
        'max_mbti_type' : max_mbti_type,
        'min_mbti_type' : min_mbti_type,
    }

    return render(request, 'MBTI/main_page.html', context)


def question_page(request, question_pk):
    global flag
    if question_pk == 12:
        flag = 1

    questions = get_object_or_404(Question, pk = question_pk)

    context = {
        'questions' : questions,
        'progress': (question_pk/12)*100
    }

    return render(request, 'MBTI/question_page.html', context)


def result_page(request, mbti):
    global flag
    mbti_names = Mbti.objects.filter(mbti_name = mbti)[0]
    base_infos = BaseInfo.objects.filter(mbti_id = mbti_names.pk)
    how_tos = Howto.objects.filter(mbti_id = mbti_names.pk)

    best_mbti = Mbti.objects.filter(pk = mbti_names.best_mbti)[0]
    worst_mbti = Mbti.objects.filter(pk = mbti_names.worst_mbti)[0]

    if flag:
        mbti_names.view_cnt += 1
        mbti_names.save()
        flag = 0

    context = {
        'title' : mbti_names.title,
        'mbti_type': mbti_names.mbti_type,
        'mbti_name' : mbti_names.mbti_name,
        'top_image': mbti_names.top_image,
        'best_mbti' : best_mbti,
        'worst_mbti' : worst_mbti,
        'base_infos' : base_infos,
        'how_tos' : how_tos,
    }

    return render(request, 'MBTI/result_page.html', context)


def share_result_page(request, mbti):
    mbti_names = Mbti.objects.filter(mbti_name = mbti)[0]
    base_infos = BaseInfo.objects.filter(mbti_id = mbti_names.pk)
    how_tos = Howto.objects.filter(mbti_id = mbti_names.pk)

    best_mbti = Mbti.objects.filter(pk = mbti_names.best_mbti)[0]
    worst_mbti = Mbti.objects.filter(pk = mbti_names.worst_mbti)[0]
    
    context = {
        'title' : mbti_names.title,
        'mbti_type': mbti_names.mbti_type,
        'mbti_name' : mbti_names.mbti_name,
        'top_image': mbti_names.top_image,
        'best_mbti' : best_mbti,
        'worst_mbti' : worst_mbti,
        'base_infos' : base_infos,
        'how_tos' : how_tos,
    }

    return render(request, 'MBTI/result_share.html', context)