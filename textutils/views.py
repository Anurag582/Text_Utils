#Creadted by Anurag Singh
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    #return HttpResponse("HELLO")
    return render(request,'index.html')
    
def about(request):
    return HttpResponse("<h1>My Anurag Singh</h1><br> Links to my profile <a href='/'>Back</a> ")

def removepunc(request):
    #get the text 
    djtext = request.POST.get('Text','default')

    removepunc=request.POST.get('removepunc','off')

    UpperCase=request.POST.get('UpperCase','off')

    newlinereomver=request.POST.get('newlinereomver','off')

    spaceremover=request.POST.get('spaceremover','off')

    charcount=request.POST.get('charcount','off')



   
    
    if removepunc=="on":
    # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed punctutions','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)

    if(UpperCase=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'purpose':'Changed to Upper case','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)
    
    if(newlinereomver=='on'):
          analyzed=""
          for char in djtext:
              if char !="\n" and char!="\r":
                analyzed=analyzed + char
          params={'purpose':'Remove new Lines','analyzed_text':analyzed}
          djtext=analyzed
          #return render(request,'Analyze.html',params)
        
    if(charcount=='on'):
          analyzed=""
          count=0
          for char in djtext:
              count=count+1
              
          params={'purpose':'Total number of Character','analyzed_text':count}
          djtext=analyzed
          return render(request,'Analyze.html',params)
    
    if(spaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
              if djtext[index] ==" " and djtext[index+1]==" ":
                  pass
              else:
                  analyzed=analyzed + char
        params={'purpose':'Remove new Lines','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)

    else:
        return HttpResponse("error")
    return render(request,'Analyze.html',params)

def spaceremover(request):
    return HttpResponse("spaceremover <a href='/'>Back</a>")
def charcount(request):
    return HttpResponse("charcount <a href='/'>Back</a>")

