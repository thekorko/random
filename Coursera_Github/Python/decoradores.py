def smart_division(div_func):
    def div[a, b]:
        if b == 0:
            print["No se puede dividir por cero!"]
            return
        return div_func(a, b)

    return div

@smart_division
def division(a, b):
    return a / b

division(1, 2)
division(2, 0)

def log(f):
    def wrap(*args, **kwargs):
        print("Ejecutando la funcion", f.__name__,
                "con los argumenots", ', '.join([str(arg) for arg in args]))
        return f(*args, **kwargs)
    return wrap
