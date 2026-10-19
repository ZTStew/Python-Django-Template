from django.shortcuts import render, redirect
from apps.Login_Register.models import User
from django.contrib import messages

# Create your views here.
def dashboard(request):

  # Tracks if the user is in a logged in state or not
  logged_in = False
  if "user_id" in request.session:
    logged_in = True

  # results = User.objects.log(request.POST)
  # test = User.report

  # print(User.objects.get(pk=request.session["user_id"]).user_name)


  # prints values in session
  for key, value in request.session.items():
    print('{} => {}'.format(key, value))

  # for key in request.session.keys():
  #   print("key:=>" + request.session[key])

  # Render list page with the users and the form
  context = {
  'users': User.objects.all(),
  'logged_in': logged_in
  }

  # print(context)

  return render(request, "DjangoTemplate/dashboard.html", context)
  # return render(request, "DjangoTemplate/dashboard.html")
