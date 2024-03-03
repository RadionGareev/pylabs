

def hi(lang,name):
    if lang=="en":
        print("hello, ",name)
    elif lang=='ro':
        print("Salut,", name)
    elif lang=='ru':
        print('privet, ',name)

hi("en", 'Jony')
hi("ro", "petru")
hi("ru", 'Ivan')