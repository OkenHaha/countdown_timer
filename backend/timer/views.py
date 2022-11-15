from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
x = datetime.datetime.now()
def index(request):
	html = '''
	<html>
	<head>
	<style>
	div{
	display:flex;
	justify-content: center;
	align-items: center;
	}
	</style>
	</head>
	<body>
		<div>
			<h1>Hello World</h1>
		</div>
	</body>
	</html>
	'''
	return HttpResponse(html + str(x))