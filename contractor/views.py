from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.models import User
from contractor.models import Profile, Employee
# PDF Config
# import cStringIO as StringIO
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# from cgi import escape
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import View
# Mail Config
# from django.core.mail import send_mail

# PDF Render Config


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        employee = Employee.objects.all()
        context = {
            'employee': employee,
        }
        pdf = render_to_pdf('contractor/report.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        if password == rpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(
                    first_name=firstname, username=username, last_name=lastname, email=email, password=password)
                auth.login(request, user)
                messages.success(request, 'You are successfully logged In')
                return redirect('contractorform')
                user.save()
                messages.success(request, 'Your Successfuly Register')
                return redirect('login')
        else:
            messages.error(request, 'Password Do Not Match')
            return redirect('registration')
    return render(request, 'contractor/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('home')
            url = request.META.get('HTTP_REFERER')
        else:
            messages.error(request, 'Invalid login crisidals')
            return redirect('login')
    return render(request, 'contractor/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successfull')
    return redirect('login')


@login_required(login_url='login')
def profile(request, username):
    # user = get_object_or_404(User, username=username)
    profile = Profile.objects.filter(user__username=username)
    context = {
        'profile': profile,
        # 'user': user
    }
    return render(request, 'contractor/profile.html', context)


@login_required(login_url='login')
def contractorform(request):
    current_user = request.user
    # user = User.objects.filter(
    #     instance=request.user.profile)
    # instance=request.user.profile
    if request.method == 'POST':
        user = current_user
        mobile = request.POST['mobile']
        address = request.POST['address']
        post_code = request.POST['post_code']
        business_size = request.POST['business_size']
        business_name = request.POST['business_name']
        abn_number = request.POST['abn_number']
        vehicle = request.POST['vehicle']
        driver_license = request.POST['driver_license']
        image = request.POST['image']
        insurence = request.POST['insurence']
        bank_name = request.POST['bank_name']
        bsb_number = request.POST['bsb_number']
        account_number = request.POST['account_number']
        account_name = request.POST['account_name']

        profile = Profile.objects.create(user=user, mobile=mobile, address=address,
                                         post_code=post_code, business_size=business_size, business_name=business_name, abn_number=abn_number, vehicle=vehicle, driver_license=driver_license, image=image, insurence=insurence, bank_name=bank_name, bsb_number=bsb_number, account_number=account_number, account_name=account_name)
        messages.success(request, 'Your information sent successfully')
        return redirect('home')
        profile.save()
    return render(request, 'contractor/contractorform.html')


@login_required(login_url='login')
def addemployee(request):
    current_user = request.user
    if request.method == 'POST':
        user = current_user
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        occupation = request.POST['occupation']
        apprentice = request.POST['apprentice']
        experience = request.POST['experience']
        phone_number = request.POST['phone_number']
        mobile = request.POST['mobile']
        email = request.POST['email']
        dob = request.POST['dob']
        address = request.POST['address']
        legall_in_au = request.POST['legall_in_au']
        work_in_ct = request.POST['work_in_ct']
        experience_ct = request.POST['experience_ct']
        aboriginal = request.POST['aboriginal']
        islander = request.POST['islander']
        medical = request.POST['medical']
        english = request.POST['english']
        interpreter = request.POST['interpreter']
        em_name = request.POST['em_name']
        em_phone = request.POST['em_phone']
        em_relation = request.POST['em_relation']

        employee = Employee.objects.create(user=user, firstname=firstname, lastname=lastname, occupation=occupation, apprentice=apprentice, experience=experience, phone_number=phone_number, mobile=mobile, email=email, dob=dob, address=address,
                                           legall_in_au=legall_in_au, work_in_ct=work_in_ct, experience_ct=experience_ct, aboriginal=aboriginal, islander=islander, medical=medical, english=english, interpreter=interpreter, em_name=em_name, em_phone=em_phone, em_relation=em_relation)
        messages.success(request, 'Employee Added Successfully')
        return redirect('employee')
        # pdf = render_to_pdf('invoice.html', context)
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Invoice_%s.pdf" % ("12341231")
        #     content = "inline; filename='%s'" % (filename)
        #     download = request.GET.get("download")
        #     if download:
        #         content = "attachment; filename='%s'" % (filename)
        #     response['Content-Disposition'] = content
        #     return response
        # send_mail(
        #     'Employ Information',
        #     'Here is the message.'+pdf,
        #     'mksifat101@gmail.com',
        #     ['mksifat101@gmail.com'],
        #     fail_silently=False,
        # )
        employee.save()
    return render(request, 'contractor/addemployee.html')


@login_required(login_url='login')
def employee(request):
    employee = Employee.objects.all()
    context = {
        'employee': employee
    }
    return render(request, 'contractor/employee.html', context)
