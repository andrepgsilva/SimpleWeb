import simpleweb as sw

def soma(x, y):
    return x + y

sw.int_input("Numero 1: ")
sw.int_input("Numero 2: ")
sw.web_button(soma)

sw.web_run()
