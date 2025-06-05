from django.shortcuts import render,redirect
from .models import Profile
from .forms import *
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
from django.conf import settings


def accept(request):
    if request.method=="POST":
        name=request.POST.get("Name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        institute=request.POST.get("institute","")
        degree=request.POST.get("degree","")
        marks=request.POST.get("marks","")
        project=request.POST.get("project","")
        skills=request.POST.get("skills","")
        about=request.POST.get("about","")

        profile=Profile(name=name,phone=phone,email=email,institute=institute,degree=degree,marks=marks,project=project,skills=skills,about=about)
        profile.save()
    return render(request,"accept.html")

def resume(request, id):
    try:
        user_profile = Profile.objects.get(pk=id)
        template = loader.get_template('resume.html')
        html = template.render({'user_profile': user_profile}, request)
        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)
        options = {
            'page-size': 'A4',
            'encoding': 'UTF-8',
            'enable-local-file-access': True,  
        }
        pdf = pdfkit.from_string(html, False, options=options, configuration=config)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response

    except Profile.DoesNotExist:
        return HttpResponse("Profile not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error generating PDF: {str(e)}", status=500)
