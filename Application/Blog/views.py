from urllib import response
from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.urls import reverse
import logging
from django.http import Http404
from .models import Post,AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
#static demo data
#posts=[
        #{"id":1, "title":"post1","content":"content of post 1"},
        #{"id":2, "title":"post2","content":"content of post 2"},
        #{"id":3, "title":"post3","content":"content of post 3"},
        #{"id":4, "title":"post4","content":"content of post 4"},
        #]
def index(request):
    blog_title="Latest post"
    all_posts=Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get("page")
    page_object=paginator.get_page(page_number)
    return render(request,"blog/index.html",{'blog_title':blog_title,"page_object":page_object})

def detail(request,slug):
    #post=next(item for item in posts if (item["id"]==post_id,None))
    #logger=logging.getLogger("TESTING")
    try:
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not Exists!")
        
    
    #logger.debug(f"post variable is {post}")
    return render(request,"blog/detail.html",{"post":post,"related_posts":related_posts})

def old_url(request):
    return redirect(reverse("blog:new_name_url"))

def new_url(request):
    return HttpResponse("This is my New redirected URL")

def about_view(request):
     return render(request,"about")
     logger = logging.getLogger("TESTING")
     if request.method == "POST":
         form = ContactForm(request.POST)
         if form.is_valid():
            logger.debug(f"POST DATA is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
         else:
             logger.debug("Form validation Failure")
             return render(request, "contact.html", {"form": form})
     else:
         form = ContactForm()
         return render(request, "contact.html", {"form": form})
     

def about_view(request):
    about_us=AboutUs.objects.first().content
    return render(request,"blog/about.html",{"about_content":about_us})
    #return render(request,"blog/about.html")

def contact_view(request):
    return render(request,"blog/contact.html")