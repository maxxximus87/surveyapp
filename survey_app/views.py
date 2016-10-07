from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Question, Freetext, Ip_addr, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'survey_app/index.html', context)

def detail(request):
    ip = get_client_ip(request)

    if Ip_addr.objects.filter(ip_addr=ip).exists():
        return render(request, 'survey_app/exist.html')

    else:



        questions = Question.objects.get(pk=1)
        questions2 = Question.objects.get(pk=2)
        questions3 = Question.objects.get(pk=3)
        questions4 = Question.objects.get(pk=4)
        questions5 = Question.objects.get(pk=5)
        #radio_checker = False
        context = {'questions': questions,
                   'questions2': questions2,
                   'questions3': questions3,
                   'questions4': questions4,
                   'questions5': questions5,
                   'ip': ip,
                   #'radio_checker': radio_checker
                   }
        return render(request, 'survey_app/detail.html', context)

def submit(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'survey_app/submit.html', context)

'''
def vote(request):
    #question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'survey_app/detail.html', {

            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('survey_app:submit'))
'''

def vote(request):
    if request.method == 'POST':
        questions = Question.objects.get(pk=1)
        questions2 = Question.objects.get(pk=2)
        questions3 = Question.objects.get(pk=3)
        questions4 = Question.objects.get(pk=4)
        questions5 = Question.objects.get(pk=5)
        radio_checker1 = False
        radio_checker2 = False
        radio_checker3 = False
        radio_checker4 = False
        radio_checker5 = False
        context_checker = ''
        ip = get_client_ip(request)

        try:
            selected_choice = Choice.objects.get(pk=request.POST['question1'])
            radio_checker1 = selected_choice.choice_text


            selected_choice2 = Choice.objects.get(pk=request.POST['question2'])
            radio_checker2 = selected_choice2.choice_text


            selected_choice3 = Choice.objects.get(pk=request.POST['question3'])
            radio_checker3 = selected_choice3.choice_text

            selected_choice4 = Choice.objects.get(pk=request.POST['question4'])
            radio_checker4 = selected_choice4.choice_text

            content = request.POST["content"]



        except (KeyError, Choice.DoesNotExist, ):

            if 'question2' in request.POST:
                selected_choice2 = Choice.objects.get(pk=request.POST['question2'])
                radio_checker2 = selected_choice2.choice_text
            else:
                pass

            if 'question3' in request.POST:
                selected_choice3 = Choice.objects.get(pk=request.POST['question3'])
                radio_checker3 = selected_choice3.choice_text
            else:
                pass

            if 'question4' in request.POST:
                selected_choice4 = Choice.objects.get(pk=request.POST['question4'])
                radio_checker4 = selected_choice4.choice_text
            else:
                pass

            if 'content' in request.POST:
                content_checker = request.POST["content"]
            else:
                pass

            return render(request, 'survey_app/detail.html', {
            'questions': questions,
            'questions2': questions2,
            'questions3': questions3,
            'questions4': questions4,
            'questions5': questions5,
            'radio_checker1': radio_checker1,
            'radio_checker2': radio_checker2,
            'radio_checker3': radio_checker3,
            'radio_checker4': radio_checker4,
            'content_checker': content_checker,
            'error_message': "You didn't select a choice.",
            })
        else:
            if Ip_addr.objects.filter(ip_addr=ip).exists():
                return render(request, 'survey_app/exist.html')

            else:
                selected_choice.votes += 1
                selected_choice.save()
                selected_choice2.votes += 1
                selected_choice2.save()
                selected_choice3.votes += 1
                selected_choice3.save()
                selected_choice4.votes += 1
                selected_choice4.save()

                content = request.POST["content"]
                a = Freetext(free_text=content)
                a.save()
                reg_ip = Ip_addr.objects.create(ip_addr=ip)
                reg_ip.save()

                return HttpResponseRedirect(reverse('survey_app:submit'))







