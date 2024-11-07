import random
from django.shortcuts import render, redirect

PALABRAS = ["javascript", "django", "pinto", "python", "virtualenv", "ahorcamela", "manage"]

def ocultar_palabra(palabra):
    num_letras_a_ocultar = max(1, int(len(palabra) * 0.6))
    indices_a_ocultar = random.sample(range(len(palabra)), num_letras_a_ocultar)
    palabra_oculta = ''.join('_' if i in indices_a_ocultar else letra for i, letra in enumerate(palabra))
    return palabra_oculta

def juego_view(request):
    if request.GET.get('reiniciar') == 'true':
        request.session.flush()
        return redirect('juego')

    if 'palabra' not in request.session:
        palabra = random.choice(PALABRAS).lower()
        palabra_oculta = ocultar_palabra(palabra)
        request.session['palabra'] = palabra
        request.session['palabra_oculta'] = palabra_oculta
        request.session['intentos'] = 5
    else:
        palabra = request.session['palabra']
        palabra_oculta = request.session['palabra_oculta']
        intentos = request.session['intentos']

    if request.method == "POST":
        intento_usuario = request.POST.get("intento", "").lower().strip()

        if not intento_usuario:
            return render(request, "juego/juego.html", {
                "error": "Entrada vacía. Intenta con una letra o la palabra completa.",
                "palabra_oculta": palabra_oculta,
                "intentos": request.session['intentos']
            })

        if len(intento_usuario) == len(palabra):
            if intento_usuario == palabra:
                request.session.flush()
                return render(request, "juego/victoria.html", {"palabra": palabra})
            else:
                request.session['intentos'] -= 1

        elif len(intento_usuario) == 1:
            if intento_usuario in palabra:
                nueva_oculta = ''.join(
                    intento_usuario if palabra[i] == intento_usuario else palabra_oculta[i]
                    for i in range(len(palabra))
                )
                request.session['palabra_oculta'] = nueva_oculta
                palabra_oculta = nueva_oculta

                if nueva_oculta == palabra:
                    request.session.flush()
                    return render(request, "juego/victoria.html", {"palabra": palabra})
            else:
                request.session['intentos'] -= 1

        else:
            return render(request, "juego/juego.html", {
                "error": "Entrada inválida. Intenta con una letra o la palabra completa.",
                "palabra_oculta": palabra_oculta,
                "intentos": request.session['intentos']
            })

        if request.session['intentos'] <= 0:
            request.session.flush()
            return render(request, "juego/derrota.html", {"palabra": palabra})

    return render(request, "juego/juego.html", {
        "palabra_oculta": palabra_oculta,
        "intentos": request.session['intentos']
    })
