from django.http import HttpResponse
from django.template import loader  # 导入loader方法
from django.shortcuts import render  # 导入reder方法
from data_base.models import book  # 导入相关model类


# Create your views here.
def book_add(request):
    try:
        book.objects.raw("""insert into data_base_book (name, sellingPrice, purchasingPrice, count) values
                            ('红楼梦',80,60,20)""")
        # book = books(name="红楼梦", sellingPrice="80", purchasingPrice="60", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="老人与海", sellingPrice="100", purchasingPrice="60", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="蒋王", sellingPrice="80", purchasingPrice="50", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="我与你", sellingPrice="30", purchasingPrice="20", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="易经", sellingPrice="100", purchasingPrice="50", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="简爱", sellingPrice="50", purchasingPrice="40", count=20)
        # book.save()  # 调用save方法进行保存
        # book = book(name="父亲", sellingPrice="60", purchasingPrice="30", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="你的背影", sellingPrice="60", purchasingPrice="40", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="影子", sellingPrice="30", purchasingPrice="15", count=20)
        # book.save()  # 调用save方法进行保存
        # book = books(name="白天与黑夜", sellingPrice="80", purchasingPrice="60", count=20)
        # book.save()  # 调用save方法进行保存
        return render(request, 'index/book_add.html', {'result': '添加成功'})
    except:
        return render(request, 'index/book_add.html', {'result': '添加失败'})


def book_select(request):
    """书籍查询"""
    try:
        books = book.objects.raw("select * from book")  # 书写sql语句
        print(books)
        return render(request, "index/book_select.html", locals())
    except:
        return render(request, 'index/book_select.html', {'result': '添加失败'})


