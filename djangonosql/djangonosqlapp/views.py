from bson import ObjectId
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from djangonosqlapp.models import dataset

# Create your views here.
@csrf_exempt
def add_data(request):
    data_title=request.POST.get("data_title").split(",")
    tags=request.POST.get("tags").split(",")
    post_title=request.POST.get("post_title")
    user_details={"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
    post=dataset(data_title=data_title,tags=tags,user_details=user_details,post_title=post_title)
    post.save()
    return HttpResponse("Inserted")

@csrf_exempt
def update_data(request,id):
    post =dataset.objects.get(_id=ObjectId(id))
    post.user_details['first_name']=request.POST.get('first_name')
    post.save()
    return HttpResponse("Post Updated")

@csrf_exempt
def delete_data(request,id):
    post =dataset.objects.get(_id=ObjectId(id))
    post.delete()

    return HttpResponse("Post Deleted Successfully")


@csrf_exempt

def read_data(request,id):
    post =dataset.objects.get(_id=ObjectId(id))
    stringval = "First Name : " + post.user_details['first_name'] + "Last name: " + post.user_details[
        'last_name'] + "Post Title" + post.post_title
    return HttpResponse(stringval)


@csrf_exempt

def read_data_all(request):
    posts =dataset.objects.all()
    stringval=""
    for post in posts:
        stringval +="First Name : " + post.user_details['first_name'] + "Last name: " + post.user_details[
        'last_name'] + "Post Title" + post.post_title + " <br> "
    return HttpResponse(stringval)


