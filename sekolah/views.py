from django.http import HttpResponse, JsonResponse

from sekolah.models import Guru


def daftar_guru(request):

    html = ''
    for guru in Guru.objects.all():
        html += '<li>{}</li>'.format(guru)

    return HttpResponse(html)


def api_daftar_guru(request):

    json = []  # python instance of type list, check with type(json)
    for guru in Guru.objects.all():
        # data is python instance of type dictionary, check with type(data)
        data = {
            'nama': guru.nama,
            'jeniskelamin': guru.jeniskelamin,
        }
        json.append(data)

    return JsonResponse(json, safe=False)  # safe True only for JSON Object
