from flask_app import app,bcrypt
from flask import redirect, session , render_template, request


# Routes
@app.route('/')
def vista_index():
    return render_template('/root/index.html')

# @app.route('/register', methods=["POST"])
# def registrar():
#     data = {
#         "nombre": request.form.get("INNombre"),
#         "apellido": request.form.get("INApellido"),
#         "email": request.form.get("INEmail"),
#         "contrasena": request.form.get("INContraseña"),
#         "contrasena_conf": request.form.get("INContraseña2")
#     }
#     if(Usuario.validate(data) == True):
#         data_save = {
#         "nombre": data.get("nombre"),
#         "apellido": data.get("apellido"),
#         "email": data.get("email"),
#         "contrasena": data.get("contrasena")
#         }
#         usuario_registrado = Usuario.save(data_save)
#         session["usuario"] = usuario_registrado
#         return redirect("/dashboard")
#     else:
#         return redirect("/")
    



@app.errorhandler(404)
def page_not_found(e):
    return "Pagina no encontrada"