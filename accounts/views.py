from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from soroco.settings import EMAIL_HOST_USER


# from django.core.mail import EmailMessage
# from django.template.loader import get_template
# from django.core.mail import EmailMessage

# Create your views here.
def password_reset_request(request):
    passs
	# if request.method == "POST":
	# 	password_reset_form = PasswordResetForm(request.POST)
	# 	if password_reset_form.is_valid():
	# 		data = password_reset_form.cleaned_data['email']
	# 		associated_users = User.objects.filter(Q(email=data))
	# 		if associated_users.exists():
				# for user in associated_users:
				# 	subject = "Password Reset Requested"
				# 	email_template_name = "main/password/password_reset_email.txt"
				# 	c = {
				# 	"email":user.email,
				# 	'domain':'127.0.0.1:8000',
				# 	'site_name': 'Website',
				# 	"uid": urlsafe_base64_encode(force_bytes(user.pk)),
				# 	"user": user,
				# 	'token': default_token_generator.make_token(user),
				# 	'protocol': 'http',
				# 	}
				# 	email = render_to_string(email_template_name, c)
				# 	try:
				# 		send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
				# 	except BadHeaderError:
				# 		return HttpResponse('Invalid header found.')
				# 	return redirect ("/password_reset/done/")
	# password_reset_form = PasswordResetForm()
	# return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

def newpassword(request):
    
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
     

        if password==confirmpassword:
            messages.info(request,'Login with new password to continue')
            return render(request,'login.html') 
        
        else :
            messages.info(request,'Password and confirm password not matching,Retry..')
    
              

def Passwordreset(request):
       
    if request.method=='POST' :
        
        email=request.POST['email']
        # print(email)
        # try:
        
        if  User.objects.filter(email=email).exists():
            # messages.info(request,'Login with new password to continue')
            # return render(request,'login.html') 
            # 
            #     
            # pass
            # subject = "Password Reset Requested"
            # email_template_name = "email.txt"
            # c = {
            # "email":email,
            # 'domain':'127.0.0.1:8000',
            # 'site_name': 'Traveloo',
            # "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            # "user": user,
            # 'token': default_token_generator.make_token(user),
            # 'protocol': 'http',
            # }
            # email = render_to_string(email_template_name, c)
            # try:
            #     send_mail(subject, email, 'admin@example.com' , [email], fail_silently=False)
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            # return redirect ("/password_reset/done/")
        # if request.method == 'POST':
        #     sub = forms.Subscribe(request.POST)
            subject = 'PASSWORD RESET'
            message = 'Reset your password using the bwlow link'
            recepient = email #str(sub['email'].value())
            send_mail(subject, 
                message, EMAIL_HOST_USER, [recepient], fail_silently = False)

            print("Email success")                              

        else :
            messages.info(request,"No account available with the Email provided,Try with different email")
            return render(request,'passwordreset.html')  

        # except:
        #     if(ConnectionRefusedError):
        #         print("Email success") 
        #         return render(request,'newpassword.html')


					
            
            
    else:
        return render(request,'passwordreset.html')
    

# def Passwordreset_done(request):
        ctx = {
        'subject': subjectin,
        'userMsg': messagein,
    }

        heading =''

        messageContent = get_template('yourTemplate.html').render(ctx) #sending value on HTML page through context
        msg = EmailMessage(heading, messageContent, settings.EMAIL_HOST_USER,
                        [])
        msg.content_subtype = 'html'
        msg.send()
    
   

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return render(request,'login.html')



    else:
        return render(request,'login.html')


def register(request):

    if request.method =="POST":
        first_name=request.POST['First_name']
        last_name=request.POST['Last_name']
        username=request.POST['Username']
        password=request.POST['Password']
        confirmpassword=request.POST['ConfirmPassword']
        email=request.POST['Email']
        

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken ,,try another username")
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"This email id is already registered")
                 return redirect('register')
                 

            else:  
                print('User is gonna be entered')                              
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('User created')
                return render(request,'login.html')
            return redirect('/')
        
        else :
            messages.info(request,'Password not matching')
            return redirect('register')

    else:
        return render(request,'register.html')