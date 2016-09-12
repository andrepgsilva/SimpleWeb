campos = []
form = False

def webinput(nome_campo):
    campos.append(nome_campo)
    if len(campos) > 1:
        form = True
        return form

def webstart():
    return {"campos":campos, "form":form}

webinput("Nome: ")
