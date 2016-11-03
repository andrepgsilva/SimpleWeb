import simpleweb as sw

def soma(x, y):
    return x + y

sw.web_input("Numero 1: ")
sw.web_input("Numero 2: ")
sw.web_button(soma)

sw.web_run()
