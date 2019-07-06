from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    # want to seperate http with html
    fulltext = request.GET['fulltext']
    # print(fulltext)
    # printed in cmd
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            # Increase
            worddict[word] += 1
        else:
            #add to dict
            worddict[word] = 1
    sortedWords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    #sort based on count in descending order
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'dict':sortedWords})

def about(request):
    return render(request, 'about.html')