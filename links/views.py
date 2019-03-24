from django.views.generic import ListView, View,TemplateView
from .models import Link, Vote
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm



class LinkListView(ListView):
    model = Link
    template_name = 'home.html'
    queryset = Link.with_votes.all()
    paginate_by = 5

    #def get_queryset(self):
        #name = Link.objects.get()
        #return name.submitter


class UserFormView(View):
    form_class= UserForm
    template_name = 'registration_form.html'

    #display the blank request
    def get(self,request):
        form = self.form_class(None)
        return render (request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned up the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user objects if credintials are correct
            user = authenticate(username= username, password= password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('links: home')
        return render(request, self.template_name, {'form': form})


class Login(TemplateView):
    template_name = 'login.html'

    def get(self, request):
        form = self.get_template_names(None)
        return render(request, self.template_name,{'form': form})



