from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) ref ao sistema


def index(request):
    return render(request, 'sistema/index.html')




# REQUEST é um objeto que contém todas as informações sobre a requisição HTTP que disparou a view.
 
# RESPONSE é um objeto que contém todas as informações sobre a resposta HTTP que será enviada ao cliente.