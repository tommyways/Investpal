from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

# from .forms import UserUpdateForm, ProfileUpdateForm
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm


from currency.models import Category, Package

# Create your views here.
from .forms import SignupForm


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "core/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Investpalfund",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="core/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )


def index(request):
    return render(request, "core/index.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("/user/")

    else:
        return render(request, "core/login.html", "recaptcha_site_key")


@login_required
def user(request):
    packages = Package.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        "core/user.html",
        {
            "categories": categories,
            "packages": packages,
        },
    )


@login_required
def transactions(request):
    return render(request, "core/transactions.html")


@login_required
def deposit(request):
    return render(request, "core/deposit.html")


@login_required
def packages(request):
    packages = Package.objects.all()
    return render(request, "core/packages.html", {"packages": packages})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(
                "/login/",
            )
    else:
        form = SignupForm()

    return render(
        request,
        "core/signup.html",
        {
            "form": form,
            "recaptcha_site_key": settings.GOOGLE_RECAPTCHA_SITE_KEY,
        },
    )


@login_required
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # try:
            #     send_mail(pc.amount, pc.receiver_wallet, pc.cryptocurrency, ["admin@example.com"])
            # except BadHeaderError:
            #     return HttpResponse("Invalid header found.")
            return redirect("/success/")
    return render(request, "core/withdraw.html", {"form": form})


def successView(request):
    return HttpResponse("Your Withdrawal is being Processed.")


def inbox(request):
    return render(request, "core/inbox.html")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("/profile/")
    else:
        user_form = UpdateUserForm(instance=request.user)
        # profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(
        request,
        "core/profile.html",
        {
            "user_form": user_form,
        },
    )


@login_required
def userhome(request):
    packages = Package.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        "core/userhome.html",
        {
            "categories": categories,
            "packages": packages,
        },
    )


# @login_required
# def withdraw(request):
#     if request.method == "GET":
#         form = WithdrawalForm()
#     else:
#         form = WithdrawalForm(request.POST)
#         if form.is_valid():
#             # cd = form.cleaned_data
#             pc = WithdrawalForm(
#                 amount = form.cleaned_data['amount'],
#                 receiver_wallet = form.cleaned_data['receiver_wallet'],
#                 cryptocurrency = form.cleaned_data['cryptocurrency']


#             )
#             pc.save()
#             try:
#                 send_mail(pc.amount, pc.receiver_wallet, pc.cryptocurrency, ["admin@example.com"])
#             except BadHeaderError:
#                 return HttpResponse("Invalid header found.")
#             return redirect("/success/")
#     return render(request, "core/withdraw.html", {"form": form})
