from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406417790',
        'name': 'Rafalah Izak',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
