from django.shortcuts import render

posts = [
    {
        'author':'Srinidhi Kannan',
        'title':'Travelling around the world',
        'content':'First blog post',
        'date_posted':'October 1, 2019'
    },
    {
        'author':'Akshara Ramesh',
        'title':'Netflix shows to watch',
        'content':'Second blog post',
        'date_posted':'September 13, 2020'
    }
]

# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
