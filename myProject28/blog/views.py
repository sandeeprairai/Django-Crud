from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username']='Sandeep'
    request.session['course']='Python DSMP'
    return HttpResponse("Session data saved successfully.")

def get_session(request):
    username=request.session.get('username','Guest')
    course=request.session.get('course','not enrolled')
    return HttpResponse(f"Welcome:{username},You are learning :{course}")

def delete_session(request):
    request.session.flush()
    return HttpResponse("All session data deletd successfully.")