from . import auth

@auth.route('/login', methods=['GET' , 'POST'])
def login():
    return "metodo login con Blueprint funcional"