from __future__ import unicode_literals

import datetime

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

## Question and choice models creation
## Question has a Question and publication date
##Each Choice is assoicated with a question

class Question(models.Model):
	question_text = models.CharField(max_length = 200) # Field is necessary field
	pub_date = models.DateTimeField('date published')

##Notice how the <Question: Question object> was an unhelpful representation
##of the object, when we used 
## Question.objects.all(). We fix it by adding __str__() method
	def __str__(self):
		return self.question_text

	##CUSTOM method for publish date(NOT A PYTHON METHOD like __str__()) 
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


##Choice model

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeigKey used to tell Django each choice is associated with a single Question
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice_text

