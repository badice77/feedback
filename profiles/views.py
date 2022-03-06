from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"




# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submittedform = ProfileForm(request.POST, request.FILES)

#         if submittedform.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             # user_image car le fichier HTML instancie la class ProfileForm
#             # et le nom de la variable est user_image
#             profile.save()
#             return HttpResponseRedirect("/profiles/")

#         return render(request, "profiles/create_profile.html", {"form": submittedform})