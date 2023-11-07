from django.shortcuts import render
from rest_framework.views import APIView
from api.models import sesion
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

# Create your views here.
class Home(APIView):
    template_name="index.html"
    def get(self, request):
        return render(request,self.template_name)
    
class About(APIView):
    template_name="about.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Login(APIView):
    template_name="login_dul.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Signin(APIView):
    template_name="signin.html"
    def get(self, request):
        return render(request, self.template_name)
    

def form(request):
    if request.method=='POST':
        nombre=request.POST['name']
        email=request.POST['email']
        pswd=request.POST['pass1'] 
        sesion(name=nombre,email=email,pas=pswd).save()
        messages.success(request,'USUARIO REGISTRADO')
        return render(request,'signin.html')
    else:
        return render(request,'signin.html')
    
def form_verificacion(request):
    if request.method=='POST':
        nombre=request.POST['name']
        email=request.POST['email']
        pswd=request.POST['pass1'] 
        sesion(name=nombre,email=email,pas=pswd).save()
        subjet = 'Verificacion de correo'
        message = f'Gracias por registrart'
        from_mail = 'cesaradair2105.2105@gmail.com'
        
        send_mail(subjet, message, from_mail, [email])
        
        messages.success(request,'USUARIO REGISTRADO')
        return render(request,'signin.html')
    else:
        return render(request,'signin.html')
    
def inicio_ses(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')  # Utiliza get() para evitar KeyError
        password = request.POST.get('password')

        try:
            user = sesion.objects.get(email=email1, pas=password)
            request.session['email'] = user.email
        
            return render(request,'index.html')
        except sesion.DoesNotExist:
            messages.error(request, 'Usuario inexistente')
        except sesion.MultipleObjectsReturned:
            messages.error(request, 'Existen demasiados usuarios con la misma información')
    
   
    return render(request,'login_dul.html')