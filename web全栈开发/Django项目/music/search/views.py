from django.shortcuts import render, redirect
from index.models import *
from django.shortcuts import reverse
from django.db.models import Q, F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


# 歌曲搜索
def searchView(request, page):
    if request.method == 'GET':
        # 歌曲搜索
        searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:6]
        # 获取搜索内容，如果kword为空，就查询全部歌曲
        kword = request.session.get('kword', '')
        if kword:  # 说明有关键字
            songs = Song.objects.filter(Q(name__icontains=kword) | Q(singer=kword)).order_by('-release').all()

        else:  # 没有关键字
            # 以发行时间查询所有的歌曲（取20首歌）
            songs = Song.objects.order_by('-release').all()[:20]
        # 分页功能
        # paginator 分页列表 [1, 2, 3]
        paginator = Paginator(songs, 5)
        try:
            pages = paginator.page(page)  #
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            # 当输入的页面超出分页列表的范围，返回最后一页数据
            pages = paginator.page(paginator.num_pages)
        # 添加歌曲搜索次数
        if kword:
            idList = Song.objects.filter(name__icontains=kword)
            for i in idList:
                dynamics = Dynamic.objects.filter(song_id=i.id)
                if dynamics:  # 有记录
                    dynamics.update(search=F('search') + 1)
                else:  # 没有记录（就需要新增一条记录）
                    dynamic = Dynamic(plays=0, search=1, download=0, song_id=i.id)
                    dynamic.save()
        return render(request, 'search.html', locals())

    else:
        # POST请求
        request.session['kword'] = request.POST.get('kword', '')
        return redirect(reverse('search', kwargs={'page': 1}))


