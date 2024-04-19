from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    #params = {'name' : 'manoj'}
    #return render(request,'index.html',params)
    #return HttpResponse("Hello")
def analyse(request):
    djtext= request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    count = request.POST.get('count','off')

    # analysed= djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if(fullcaps=='on'):
        analysed = ""
        for char in djtext:
                analysed = analysed + char.upper()
        params = {'purpose': 'Capitalise the Text', 'analyzed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', prams)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyse.html', params)
    # if (spaceremover == 'on'):
    #     analysed = ""
    #     for index, char in enumerate (djtext):
    #         if not(djtext[index] ==" " and djtext[index+1] ==" "):
    #             analysed = analysed + char
    #     prams = {'purpose': 'Space Remover', 'analyzed_text': analysed}
    #     djtext = analysed
    #     return render(request, 'analyse.html', prams)
    # if (count == 'on'):
    #     analysed = ""
    #     count = 0;
    #     # Counts each character except space
    #     for char in range(0, len(djtext)):
    #         if (djtext[char] != ' '):
    #             count = count + 1;
    #             analysed = str(count)
    #     prams = {'purpose': 'Count', 'analyzed_text': analysed}
    #     djtext = analysed
    # return render(request, 'analyse.html', prams)
    #




# def capfirst(request):
#     return HttpResponse("captializefirst")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")