# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http	import HttpResponse
from basic.forms import MainForm
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def main(request):
	adult_num = [
	{"label": "0", "value": "value0"},
	{"label": "1", "value": "value1"},
	{"label": "2", "value": "value2"},
	{"label": "3", "value": "value3"},
	{"label": "4", "value": "value4"},
	{"label": "5", "value": "value5"},
	{"label": "6", "value": "value6"},
	{"label": "7", "value": "value7"},
	{"label": "8", "value": "value8"},
	{"label": "9", "value": "value9"}
	]
	selected_value = "value1"

	kid_num = [
	{"label": "0", "value": "value0"},
	{"label": "1", "value": "value1"},
	{"label": "2", "value": "value2"},
	{"label": "3", "value": "value3"},
	{"label": "4", "value": "value4"},
	{"label": "5", "value": "value5"},
	{"label": "6", "value": "value6"},
	{"label": "7", "value": "value7"},
	{"label": "8", "value": "value8"},
	{"label": "9", "value": "value9"}
	]
	selected_value_kids = "value0"

	return render(request, 'pages/main.html',  {"adult_num": adult_num,
												"selected_value": selected_value,
												"kid_num": kid_num,
												"selected_value_kids": selected_value_kids,
												})

def result(request):
	# POST 방식이면, 데이터가 담긴 제출된 폼으로 간주.
	if request.method == 'POST':
	#request에 담긴 데이터로, 클래스폼을 생성.
		form = MainForm(request.POST)
		adult_num = request.POST.get('adult_num')
	else:
		form = MainForm()

	return render(request, 'pages/result.html', {'form':form})

def list(request):
    return render(request, 'pages/list.html')

def detail(request):
    return render(request, 'pages/detail.html')

def geo(request):
    return render(request, 'pages/geo.html')

def logo(request):
	return render(request, 'pages/logo.html')
