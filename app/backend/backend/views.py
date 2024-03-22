from django.http import HttpResponse

def get_authors(request):
    return HttpResponse("Filip Szweda, Jakub Grzybowski, Julia Żęgota, Kamil Czepiel, Krzysztof Kulpiński, Michał Wrzosek, Mikołaj Nowak")
