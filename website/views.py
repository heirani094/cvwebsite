#views.py
from django.shortcuts import render, redirect
from website.forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'website/index.html')


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
           # messages.success(request,messages.SUCCESS, 'your ticket submited successfuly!')
            return redirect('/contact')
        else:
            # اضافه کردن خطاهای فرم به پیام‌ها
            for field, errors in form.errors.items():
                for error in errors:
                    if field == 'email' and error == 'This field is required.':
                        messages.error(request, '** فیلد ایمیل خالی می‌باشد لطفا آن را پر کنید **')
                    elif field == 'name' and error == 'This field is required.':
                        messages.error(request,'** فیلد نام خالی می‌باشد لطفا آن را پر کنید **')
                    elif field == 'subject' and error == 'This field is required.':
                        messages.error(request,'** فیلد موضوع خالی می‌باشد لطفا آن را پر کنید **')
                    elif field == 'message' and error == 'This field is required.':
                        messages.error(request,'** فیلد پیغام خالی می‌باشد لطفا آن را پر کنید **')
                    else:
                        messages.error(request, f"خطا در فیلد {field}: {error}")
        return redirect('/contact')

    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})


def about_view(request):
    return render(request, 'website/about.html')


def elements_view(request):
    return render(request, 'website/elements.html')


def portfolio_view(request):
    return render(request, 'website/portfolio.html')
