from django.shortcuts import render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def contact(request):
    messages.success(request, 'Welcome to the contacts section')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']


        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=  Contact(name=name, email=email,phone=phone, content=content)
            contact.save()    
            messages.success(request, 'Your messages is sucessfully saved')


    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def search(request):  
    query = request.GET['query']
    if len(query)>78:
        allPosts = []
    else:
        
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)   
        allPosts = allPostsTitle.union(allPostsContent)
    
    if allPosts.count() == 0:
        messages.warning(request, "No search result found .Please refine your data")
    params = {'allPosts': allPosts,'query' : query}
    return render(request, "home/search.html", params)


def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['uername']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        state= request.POST['state']
        inputcity=request.POST['inputcity']
        inputZip=request.POST['inputZip']
        #check for erroreous input

        myuser = User.objects.create_user(username, email, password1)
        myuser.firstname = firstname
        myuser.lastname = lastname 
        myuser.state = state 
        myuser.inputcity = inputcity 
        myuser.inputZip = inputZip 
        myuser.save()
        messages.success(request,"Your account is successfully created")
    else:
        return HttpResponse("404 not Found")