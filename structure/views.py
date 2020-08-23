from django.shortcuts import render
from .models import NavBar, MotionImage, News, Question, Adds, Success


def homepage(request):
    nav = NavBar.objects.all()
    motion = MotionImage.objects.all()
    all_news = News.objects.all()
    news = all_news[::-1]
    if len(news) > 3:
        news_list = news[:3]
    else:
        news_list = news[:]

    all_advert = Adds.objects.all()
    advert = all_advert[::-1]
    if len(advert) > 3:
        advert_list = advert[:3]
    else:
        advert_list = advert[:]

    short = []
    for item in news:
        if item.NShort != "":
            short.append(item.NShort)
    news_short = short[:5]
    success = Success.objects.all()

    question = Question.objects.all()
    context = {'nav': nav, 'motion': motion, 'news_list': news_list, 'success': success, 'news_short': news_short,
               'advert_list': advert_list, 'question': question}
    return render(request, 'structure/Main.html', context)


def nav_detail(request, slug):
    all_news = News.objects.all()
    news = all_news[::-1]
    short = []
    for item in news:
        if item.NShort != "":
            short.append(item.NShort)
    news_short = short[:5]

    nav_detail = NavBar.objects.get(NAVSlug=slug)
    nav = NavBar.objects.all()
    motion = MotionImage.objects.all()
    smotion = MotionImage.objects.filter(MIRelation=nav_detail)
    context = {'nav_detail': nav_detail, 'nav': nav, 'motion': motion, 'news_short': news_short, 'smotion': smotion}
    return render(request, 'structure/nav_detail.html', context)


def news_list_Page(request):
    news = News.objects.all()
    nav = NavBar.objects.all()
    news_list = news[::-1]
    context = {'nav': nav, 'news_list': news_list}
    return render(request, 'structure/News_List.html', context)


def news_detail_page(request, id):
    nav = NavBar.objects.all()
    num = 1
    news = News.objects.get(id=id)
    context = {'nav': nav, 'num': num, 'news': news}
    return render(request, 'structure/News_Details.html', context)


def advert_page(request, id):
    nav = NavBar.objects.all()
    num = 2
    advert = Adds.objects.get(id=id)
    context = {'nav': nav, 'num': num, 'advert': advert}
    return render(request, 'structure/News_Details.html', context)