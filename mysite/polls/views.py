from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list': latest_question_list
# 	}
#     return HttpResponse(template.render(context, request))

    ##NOTE: WE have seperated the templates, so above the 
    ##code loads the template called /polls/index.html and passes it a context
 
 ##WE CAN REWRITE THE ABOVE CODE WITH A SHORTCUT IN Django using render


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

   ##render returns a HttpResponse object of the given template     

##simplest view possible in Django
##Now, to call this view, it needs to be mapped to a url(for an url we need a
## URLconf)

##Hence to create a URLconf in the polls directory, we create the file urls.py

##MORE VIEWS. views taking arguments
## details view: Displays a question text, with no results but with form to vote

##RAISING A 404 ERROR:

# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk = question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, '/polls/detail.html', {'question:'})


##EASIER and a SHORTCUT TO RAISE 404 ERROR:

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})


##Results view page: Displays results for a particular question

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

## vote action view: handles voting for a particular question
def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

##NOTE: the page's design was hardcoded here. This needs to be seperated,
##because otherwise we need to edit the python code. Hence we create the
##DIRECTORY templates in the polls directory.