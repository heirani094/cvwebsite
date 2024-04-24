from django.http import HttpResponse


def test_http(request):
    return HttpResponse("dali")
