import bleach

def clean_user_input(data):
    for values in data.item():
        bleach.clean(values)