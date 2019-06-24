from rest_framework import generics
from .models import download
from .serializers import downloadSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import urllib.request
from flask import Flask, jsonify, request
from django.shortcuts import render
import requests
import json
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth.views import login_required
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper
from mimetypes import guess_type
import base64

@api_view(['GET','POST'])
def downloadList(request):
	print(request.data)
	if "owner" in request.data.keys():
		a = request.data['owner']
	else:
		return Response({"bad request"},status=400)
	print(a)
	archives = []
	posibles_archives = requests.get('http://file-controller-ms:2870/list')
	#posibles_archives=requests.get('http://35.227.21.88:2870/list')
	archive = posibles_archives.json()
	keys = archive.keys()
		
	if keys:
		newjson=encontrarowner(keys,archive,a)
		print("newjson es ")
		print(newjson)
		try:
			new_keys=newjson.keys()
		except:
			newjson = {}
			new_keys = []
		encontrarpath(new_keys, newjson, archives)
		x = {"list": archives}
		return Response(newjson, status=200)
	else:
		return Response({"error"}, status=404)


@api_view(['GET','POST'])
def downloadfile(request):
	#archives = []
	print(request.data)
	if "path" in request.data.keys():
		a = request.data['path']
	else:
		return Response({"bad request"},status=400)
	print(a)

	filepath = a
	z=list(filepath)
	namefilepath=""
	for x in range(len(z)-1,0,-1):
		if z[x]=="/":
			break
		namefilepath+=z[x]

	namefilepath=namefilepath[::-1]
	print(namefilepath)
	final_filepath = os.path.join(filepath)
	with open(final_filepath, 'rb') as f:
		encoded_string = base64.b64encode(f.read())
		jsondownload={"base64":encoded_string,"name":namefilepath}
		return Response(jsondownload,status=200)


	'''posibles_archives = requests.get('http://192.168.99.101:2870/list')
	# posibles_archives=requests.get('http://34.73.22.196:2870/list')
	archive = posibles_archives.json()
	keys = archive.keys()
	if keys:
		encontrarpath(keys, archive, archives)
	else:
		return Response({"error"}, status=404)'''

	'''#filepath = 'C:/Users/El Brayo/Documents/pdf-sample.pdf'
	filepath = a
	z=list(filepath)
	namefilepath=""
	for x in range(len(z)-1,0,-1):
		if z[x]=="/":
			break
		namefilepath+=z[x]

	namefilepath=namefilepath[::-1]
	print(namefilepath)
	final_filepath = os.path.join(filepath)
	with open(final_filepath, 'rb') as f:
		wrapper = FileWrapper(f)
		mimetype= 'application/force-download'
		gussed_mimetype = guess_type(filepath)[0]
		if gussed_mimetype:
			mimetype = gussed_mimetype
		response = HttpResponse(wrapper,content_type=mimetype)
		response['Content-Disposition'] = "attachement;filename="+namefilepath
		response["X-sendFile"]= "SomeText.txt"
		return response'''


@api_view(['GET','POST'])
def soap(request):
	print(request.data)
	if "owner" in request.data.keys():
		a = request.data['owner']
	else:
		return Response({"bad request"},status=400)
	print(a)
	archives = []
	posibles_archives = requests.get('http://file-controller-ms:2870/list')
	#posibles_archives=requests.get('http://35.227.21.88:2870/list')
	archive = posibles_archives.json()
	keys = archive.keys()
		
	if keys:
		newjson=encontrarowner(keys,archive,a)
		print("newjson es ")
		print(newjson)
		try:
			new_keys=newjson.keys()
		except:
			newjson = {}
			new_keys = []
		encontrarpath(new_keys, newjson, archives)
		number=newjson.keys()
		return Response(len(number), status=200)
	else:
		return Response({"error"}, status=404)

def encontrarowner(keys,json,owner):
	for i in keys:
		if i == owner:
			return json[i]

def encontrarpath(keys,json,array):
	if "path" in keys:
		array.append((json["path"]))
	for i in keys:
		if not isinstance(json[i], str):
			encontrarpath(json[i].keys(),json[i],array)

