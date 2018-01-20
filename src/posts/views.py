from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_create(request): #create a post
	return HttpResponse("<h1>Create</h1>")

def posts_detail(request): #retrieve a data
	return HttpResponse("<h1>Detail</h1>")

def posts_list(request): #list an item
	return HttpResponse("<h1>List</h1>")

def posts_update(request): #update the post
	return HttpResponse("<h1>Update</h1>")

def posts_delete(request): #delete the post
	return HttpResponse("<h1>Delete</h1>")

