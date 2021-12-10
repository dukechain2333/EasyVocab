from django.shortcuts import render, redirect
from EasyVocab import settings
import requests
from Dictionary import models as dic_models


# Create your views here.

def get_data(word):
    dic_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + settings.DIC_KEY
    thes_url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/' + word + '?key=' + settings.THES_KEY
    dic_data = requests.post(url=dic_url, headers=settings.HEADERS).json()

    if len(dic_data) != 0:
        if isinstance(dic_data[0], str):
            dic_data = ['Not a valid word']
            thes_data = ['Not a valid word']
            return dic_data, thes_data, 0
    else:
        dic_data = ['Not a valid word']
        thes_data = ['Not a valid word']
        return dic_data, thes_data, 0

    thes_data = requests.post(url=thes_url, headers=settings.HEADERS).json()

    return dic_data, thes_data


def store_history(word, request):
    new_history = dic_models.History.objects.create()
    new_history.userId = request.session['user_id']
    new_history.username = request.session['user_name']
    new_history.history = word
    new_history.save()


def get_dic(data):
    dic_sorted = []
    for d in data:
        try:
            meaning = {
                'pron': d['hwi']['prs'][0]['mw'],
                'fl': d['fl'],
                'offensive': d['meta']['offensive'],
                'stems': d['meta']['stems'],
                'usage': d['def'][0]['sseq'][0][0][1]['dt'][0][1],
                'def': d['shortdef']
            }
            dic_sorted.append(meaning)
        except:
            meaning = {
                'pron': '',
                'fl': '',
                'offensive': d['meta']['offensive'],
                'stems': d['meta']['stems'],
                'usage': '',
                'def': d['shortdef']
            }
            dic_sorted.append(meaning)

    return dic_sorted


def get_thes(data):
    thes_sorted = []
    for d in data:
        try:
            meaning = {
                'stems': d['meta']['stems'],
                'syns': d['meta']['syns'],
                'offensive': d['meta']['offensive'],
                'fl': d['fl'],
                'usage': d['def'][0]['sseq'][0][0][1]['dt'][1][1][0]['t'],
                'def': d['shortdef']
            }
            thes_sorted.append(meaning)
        except:
            return thes_sorted

    return thes_sorted


def dictionary(request):
    if request.method == "POST":
        if request.session.get('is_login', None):
            search = request.POST.get('search')
            if search:
                store_history(search, request)
                try:
                    dic_data, thes_data = get_data(search)
                except:
                    dic_data, thes_data, false_flag = get_data(search)
                    return render(request, 'Dictionary/Dictionary.html',
                                  {"normalDic": dic_data, "proDic": thes_data,
                                   "words": search})
                dic_data = get_dic(dic_data)
                thes_data = get_thes(thes_data)
                return render(request, 'Dictionary/Dictionary.html',
                              {"normalDic": dic_data, "proDic": thes_data,
                               "words": search})
            else:
                return render(request, 'Home/Home.html')
        else:
            return redirect('/login')

    return render(request, 'Dictionary/Dictionary.html')
