from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index2.html')

def analyze(request):
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    newline = request.GET.get('newline','off')
    charcounter = request.GET.get('charcounter','off')
    analyzed = ""
    purpose = ""
    if removepunc == 'on':
        purpose += " Remove Punctuations"
        for char in request.GET.get('text'):
            if char not in punctuations:
                analyzed = analyzed + char
    if uppercase == 'on':
        if analyzed == "":
            analyzed = request.GET.get('text')
        purpose += " To UpperCase"
        analyzed = analyzed.upper()
    if newline == 'on':
        purpose += " New Line"
        for char in request.GET.get('text'):
            if char != '\n':
                analyzed = analyzed+char
    if charcounter == 'on':
        purpose += " Character Counter"
        counter = 0
        for char in analyzed:
            counter = counter+1
            analyzed =analyzed+char
        analyzed =analyzed +" "+ str(counter)
    return render(request,'analyze.html',{'purpose':purpose,'analyzed_text':analyzed})       
