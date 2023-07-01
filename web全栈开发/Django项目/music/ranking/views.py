from django.shortcuts import render

# Create your views here.
from index.models import *

# 歌曲排行榜
def rankingView(request):
    # 热搜歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    # 歌曲分类表
    labels = Label.objects.all()

    # 歌曲排行信息
    # 或者GET请求的type参数值
    t = request.GET.get('type', '')

    if t:  # 1 2 3 4 5 6 7
        # filter条件
        dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:10]
    else:
        dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:10]
    return render(request, 'ranking.html', locals())




