import sympy as sp

def determinar_orden(ecuacion):
    y = sp.Function('y')
    x = sp.symbols('x')

    # Convertimos la ecuación a una expresión de sympy manejando correctamente las derivadas
    try:
        # Sustituimos las derivadas en la forma común por la notación de sympy
        # Manejamos derivadas hasta el quinto orden
        ecuacion = (ecuacion.replace("y'''''", "y(x).diff(x, 5)")
                    .replace("y''''", "y(x).diff(x, 4)")
                    .replace("y'''", "y(x).diff(x, 3)")
                    .replace("y''", "y(x).diff(x, 2)")
                    .replace("y'", "y(x).diff(x)"))
        expr = sp.sympify(ecuacion)
    except Exception as e:
        return f"Error al interpretar la ecuación: {e}"

    # Calculamos el orden de la ecuación diferencial
    derivadas = expr.atoms(sp.Derivative)
    orden = max((derivativa.derivative_count for derivativa in derivadas), default=0)

    return f"La ecuación es de orden {orden}."

ecuacion = "y''''' + y'''' + y''' + sqrt(y) + 2*y - exp(x)"
resultado = determinar_orden(ecuacion)
print("Resultado de la ecuación de prueba:", resultado)

