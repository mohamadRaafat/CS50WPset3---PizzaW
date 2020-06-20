from .models import Pizza, Sub, Pasta, Salad, DinnerPlatter

def get_price(request):
    size = request.POST.get('size')
    if size == "small":
        try:
            price = float(Pizza.objects.filter(
                    description=request.POST.get('name'))[0].small_price)
        except Pizza.DoesNotExist:
            try:
                price = float(Sub.objects.get(
                        name=request.POST.get('name')).small_price)
            except Sub.DoesNotExist:
                try:
                    price = float(Pasta.objects.get(
                            name=request.POST.get('name')).price)
                except Pasta.DoesNotExist:
                    try:
                        price = float(Salad.objects.get(
                                name=request.POST.get('name')).price)
                    except Salad.DoesNotExist:
                        try:
                            price = float(DinnerPlatter.objects.get(
                                    name=request.POST.get('name')).small_price)
                        except:
                            pass
    elif size == "large":
        try:
            price = float(Pizza.objects.filter(
                description=request.POST.get('name'))[0].large_price)
        except Pizza.DoesNotExist:
            try:
                price = float(Sub.objects.get(
                    name=request.POST.get('name')).large_price)
            except Sub.DoesNotExist:
                try:
                    price = float(Pasta.objects.get(
                        name=request.POST.get('name')).price)
                except Pasta.DoesNotExist:
                    try:
                        price = float(Salad.objects.get(
                            name=request.POST.get('name')).price)
                    except Salad.DoesNotExist:
                        try:
                            price = float(DinnerPlatter.objects.get(
                                name=request.POST.get('name')).large_price)
                        except:
                            pass
    else:
        try:
            price = float(Pasta.objects.get(
                name=request.POST.get('name')).price)
        except Pasta.DoesNotExist:
            try:
                price = float(Salad.objects.get(
                    name=request.POST.get('name')).price)
            except Salad.DoesNotExist:
                pass
    return price
