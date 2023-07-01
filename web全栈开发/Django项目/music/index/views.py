from django.shortcuts import render
from .models import *

# Create your views here.


# 进入首页的视图函数
def indexView(request):
    songDynamic = Dynamic.objects.select_related('song')

    # 热搜歌曲
    searchs = songDynamic.order_by('-search').all()[:8]
    # 音乐分类
    labels = Label.objects.all()
    # 热门歌曲
    popular = songDynamic.order_by('-plays').all()[:10]
    # 新歌推荐
    recommend = Song.objects.order_by('-release').all()[:3]
    # 热门下载
    downloads = songDynamic.order_by('-download').all()[:6]

    tabs = [searchs[:6], downloads]
    return render(request, 'index.html', locals())
