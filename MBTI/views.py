from django.shortcuts import (render, redirect, get_object_or_404)

from .models import Mbti, BaseInfo, AnotherInfo, Howto, Question

# Create your views here.

def main_page(request):
    global mbti_dict
    mbti_dict = {'EI':0, 'NS':0, 'TF':0, 'PJ':0}

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
    questions = get_object_or_404(Question, pk = question_pk)
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'MBTI/question_page.html', context)


def choice_right(request, question_pk):
    if question_pk == 12:
        mbti_string = ''

        for key, value in mbti_dict.items():
            if value >= 2:
                mbti_string += key[0]
            else:
                mbti_string += key[1]

        return redirect('MBTI:result_page', mbti_string)

    new_pk = question_pk + 1
    return redirect('mbti:question_page', new_pk)


def choice_left(request, question_pk):
    questions = get_object_or_404(Question, pk = question_pk)
    category = questions.question_category
    
    mbti_dict[category] += 1

    if question_pk == 12:
        mbti_string = ''

        for key, value in mbti_dict.items():
            if value >= 2:
                mbti_string += key[0]
            else:
                mbti_string += key[1]

        return redirect('MBTI:result_page', mbti_string)

    new_pk = question_pk + 1
    return redirect('mbti:question_page', new_pk)


def result_page(request, mbti):
    mbti_names = Mbti.objects.filter(mbti_name = mbti)[0]
    base_infos = BaseInfo.objects.filter(mbti_id = mbti_names.pk)
    another_infos = AnotherInfo.objects.filter(mbti_id = mbti_names.pk)
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
        'another_infos' : another_infos,
        'how_tos' : how_tos,
    }

    return render(request, 'MBTI/result_page.html', context)

def share_result_page(request, mbti):
    mbti_names = Mbti.objects.filter(mbti_name = mbti)[0]
    base_infos = BaseInfo.objects.filter(mbti_id = mbti_names.pk)
    another_infos = AnotherInfo.objects.filter(mbti_id = mbti_names.pk)
    how_tos = Howto.objects.filter(mbti_id = mbti_names.pk)
    
    context = {
        'title' : mbti_names.title,
        'mbti_type': mbti_names.mbti_type,
        'mbti_name' : mbti_names.mbti_name,
        'top_image': mbti_names.top_image,
        'base_infos' : base_infos,
        'another_infos' : another_infos,
        'how_tos' : how_tos,
    }

    return render(request, 'MBTI/share_result_page.html', context)