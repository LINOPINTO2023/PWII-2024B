import random
from django.shortcuts import render

PALABRAS = ["javascript", "Django", "PINTO", "Python", "virtualenv", "ahorcamela", "manage"]

def ocultar_palabra(palabra):
    num_letras_a_ocultar = max(1, int(len(palabra) * 0.6))
    indices_a_ocultar = random.sample(range(len(palabra)), num_letras_a_ocultar)
    palabra_oculta = ''.join('_' if i in indices_a_ocultar else letra for i, letra in enumerate(palabra))
    return palabra_oculta

def juego_view(request):
    palabra = request.session.get('palabra')
    palabra_oculta = request.session.get('palabra_oculta')
    intentos = request.session.get('intentos')

    if request.method == "POST":
        intento_usuario = request.POST.get("intento", "").lower().strip()

        if not intento_usuario:
            return render(request, "juego/juego.html", {
                "error": "Entrada vacía. Intenta con una letra o la palabra completa.",
                "palabra_oculta": palabra_oculta,
                "intentos": intentos
            })

        if len(intento_usuario) == len(palabra):
            # El usuario intenta adivinar la palabra completa
            if intento_usuario == palabra.lower():
                return render(request, "juego/victoria.html", {"palabra": palabra})
            else:
                request.session['intentos'] -= 1
        elif len(intento_usuario) == 1:
            # El usuario intenta adivinar una letra
            if intento_usuario in palabra.lower():
                nueva_oculta = ''.join(
                    intento_usuario if palabra[i].lower() == intento_usuario else palabra_oculta[i]
                    for i in range(len(palabra))
                )
                request.session['palabra_oculta'] = nueva_oculta
                palabra_oculta = nueva_oculta
                if nueva_oculta.lower() == palabra.lower():
                    return render(request, "juego/victoria.html", {"palabra": palabra})
            else:
                request.session['intentos'] -= 1
        else:
            return render(request, "juego/juego.html", {
                "error": "Entrada inválida. Intenta con una letra o la palabra completa.",
                "palabra_oculta": palabra_oculta,
                "intentos": intentos
            })

        # Verificar si se han agotado los intentos
        if request.session['intentos'] <= 0:
            return render(request, "juego/derrota.html", {"palabra": palabra})

    # Renderizar la vista del juego
    return render(request, "juego/juego.html", {
        "palabra_oculta": palabra_oculta,
        "intentos": intentos
    })
