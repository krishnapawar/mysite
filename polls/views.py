
from django.http import HttpResponse
from django.shortcuts import render
import operator
def index(request):
    ##return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
    return render(request,'index.html')

def count(request):
	tex= request.GET['textareaf']
	txlist=tex.split()
	textl=len(txlist)
	wordd={}
	for word in txlist:
		if word in wordd :
			wordd[word] += 1
		else:
			wordd[word] = 1

	sortlist = sorted(wordd.items(),key =operator.itemgetter(1),reverse=True)


	return render(request,'count.html',{'textf':tex,'wordlenth':textl,'listt':txlist,'wordd1':sortlist})


def main(request):
	return render(request,'polls/home.html')