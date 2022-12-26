from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from customer.models import Product

# Create your views here.
def about(request):
    html = '''
    About Myself
    '''
    return HttpResponse(html)


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="/static/style.css">
    <title>顧客列表</title>
    </head>
    <body>
    <section>
    <div class="block">
        <div class="text">
    <h2>以下是目前訂購中的電腦主機顧客列表</h2>
     </div>
    <hr>
    <div class="tabl">
    <table>
        {}
    </table>
        </div>
    </div>
    </section>
    </body>
    </html>
    '''
    products = Product.objects.all()
    tags ='<tr><td>顧客姓名</td><td>編號</td><td>售價</td><td>訂購量</td></tr>'
    for p in products:
        tags= tags + "<tr><td>{}</td>".format(p.name)
        tags= tags + "<td>{}號</td>".format(p.sku)
        tags= tags + "<td>{}元</td>".format(p.price)
        tags= tags + "<td>{}個</td></tr>".format(p.qty)
    return HttpResponse(html.format(tags))

import random
def about(request):
    quote = ['今日事,今日畢',
    '要怎麼收穫,先怎麼栽',
    '知識就是力量',
    '一個人的個性就是他的命運']
    quote = random.choice(quote)
    return render(request,'about.html',locals())

from django.http import Http404
# from django.http import HttpResponseNotFound
def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    
    # return HttpResponse('找不到指定的品項編號')
    # return HttpResponseNotFound('<h1>not found</h1>')

    return render(request, 'disp.html',locals())


