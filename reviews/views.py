import imp
from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect

import reviews
from .forms import ReviewForm
from .forms import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


    # def get(self, request):
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})

    # def post(self, request):
    #     form = ReviewForm(request.POST)
        
    #     if form.is_valid():               
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {"form": form})


# def review(request):
#     if request.method == "POST":
#         existing_data = Review.objects.get(pk=1)
#         form = ReviewForm(request.POST, instance=existing_data)
        
#         if form.is_valid():               
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {"form": form})

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")


# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works well!'
        return context

class ReviewsListViews(ListView):
    template_name = "reviews/review_list.html"
    model= Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context