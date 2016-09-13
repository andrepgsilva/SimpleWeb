campos = []
form = False

def webinput(nome_campo):
    campos.append(nome_campo)
    form = True if len(campos) > 1 : False
    return form

def webstart():
    return {"campos":campos, "form":form}

webinput("Nome: ")
