import os,sys

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from . import  forms
import subprocess
from .models import Choice, Question,Report_master
from .py_scripts import audit_zscore

import pandas as pd
from sqlalchemy import  create_engine
from py_scripts import *
# import polls/models

dbList=["raj"]
server="DESKTOP-FO3VN7C"
engine = create_engine('mssql+pymssql://' + server + '/' + dbList[0])
db_name = engine.execute("select name from sys.databases where has_dbaccess(name)=1").fetchall()

def a(request):
    repo=['r1','r2']
    dic={'first_name': 'John', 'last_name': 'Doe'}
    db_list=[]
    engine = create_engine('mssql+pymssql://' + server + '/master')
    for i in db_name:
        db_list.append(i[0])
    if request.method!='POST':
        return render(request, "polls/mytest.html", context={"ques": db_list})
    else:
        fdate = request.GET['fdate']
        tdate = request.GET['tdate']
        db=request.GET['db']
        report1=request.GET['report1']
        engine = create_engine('mssql+pymssql://' + server + '/' + db)
        data=engine.execute("select * from ums_bill where bill_date >'"+fdate+"' and bill_date <'"+tdate+"' ").fetchall()
        if data.__len__()<1:
            return HttpResponse("<h>No records Found</H>")
        else:
            pd.DataFrame(data).to_csv("aaaa.csv")
            a=open("aaaa.csv")
            response = HttpResponse(a)
            response['Content-Disposition'] = 'attachment; filename=' + "sds"
            return response

def form1(request):
    form= forms.Formname()
    if request.method=='POST':
        form= forms.Formname(request.POST)
        if form.is_valid():
            print("Validation Success")
            print("cleaned: "+form.cleaned_data['name'])
            return HttpResponse('Thnaks')
    return render(request,'polls/form1Page.html',{'form':form})





class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    x=Choice.objects.all()
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def report_master(request):
    x=Report_master.objects.all()
    db_name = engine.execute("select name from sys.databases where has_dbaccess(name)=1").fetchall()
    if request.method != 'POST':
        return render(request, "polls/report_master.html", context={"report_list": x,"db_name":db_name})
    else:
        try:
            subprocess(sys.executable,request.POST[''])
            return HttpResponse("File generated in "+os.getcwd())
        except:
            return HttpResponse("Error!")
        # subprocess.run([request.POST['']])


    # return render(request,'polls/report_master.html')

