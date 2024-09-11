from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from app import create_app
from app.forms import Form
from app.models import Alojamiento, Comentario
# Importar la función crear_alojamientos de init.py
from app import crear_alojamientos
from app import db
from flask import jsonify, request
from datetime import datetime
from app.models import Reserva
from sqlalchemy import desc




# Importamos desde __init__ crear la aplicacion
app = create_app()

# Llamar a la función para crear los alojamientos
with app.app_context():
    crear_alojamientos()


# Cuando hay un error de conexión, de página no encontrada
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error = error)


# Creamos la función para la readirección
# Añadimos los metodos get y post
@app.route("/", methods=["GET", "POST"])
def inicio():
    form = Form()


    # Filtrar los alojamientos basados en los parámetros (esto es solo un ejemplo básico)
    query = Alojamiento.query


    # Ejecutar la consulta
    alojamientos = query.all()

    # Contexto para la plantilla
    context = {
        "form": form,
        "alojamientos": alojamientos
    }

    return render_template("inicio.html", **context)


@app.route("/buscar-alojamiento/", methods=["GET"])
def buscarAlojamiento():
    # Obtener los filtros de la solicitud GET
    tipo_inmueble = request.args.get('tipoInmueble', type=str)
    check_in = request.args.get('check_in', type=str)
    check_out = request.args.get('check_out', type=str)
    capacidad = request.args.get('capacidad', type=str)
    orden = request.args.get('orden', type=str)

    # Obtener todos los alojamientos sin filtrar
    alojamientos = Alojamiento.query

    # Aplicar los filtros según los parámetros recibidos
    if tipo_inmueble and tipo_inmueble != 'normal':
        alojamientos = alojamientos.filter_by(tipo=tipo_inmueble)
    
    
    if capacidad and capacidad != 'normal':
        alojamientos = alojamientos.filter(Alojamiento.capacidad >= int(capacidad))

    # Aplicar el orden según el parámetro recibido
    if orden == 'mayorMenor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.desc())
    elif orden == 'menorMayor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.asc())

    # Ejecutar la consulta y obtener los resultados filtrados
    alojamientos_filtrados = alojamientos.all()

    form = Form()

    # Crear un diccionario de datos que contiene todos los datos necesarios
    context = {
        "form": form,
        "alojamientos": alojamientos_filtrados  # Pasar los alojamientos filtrados al template
    }

    
    # Renderizar la plantilla completa con los datos filtrados
    return render_template("buscar_alojamiento.html", **context)


@app.route("/alojamientos/", methods=["GET"])
def listaAlojamientos():
    # Obtener el parámetro de orden de la URL
    orden = request.args.get('orden')

    # Obtener todos los alojamientos sin filtrar
    alojamientos = Alojamiento.query

    # Obtener los filtros de la solicitud GET
    ciudad = request.args.get('ciudad', default='normal', type=str)
    tipo_inmueble = request.args.get('tipo_inmueble', default='normal', type=str)
    capacidad = request.args.get('capacidad', default='normal', type=str)


    # Aplicar los filtros según los parámetros recibidos
    if ciudad != 'normal':
        alojamientos = alojamientos.filter_by(ciudad=ciudad)
    if tipo_inmueble != 'normal':
        alojamientos = alojamientos.filter_by(tipo=tipo_inmueble)
    if capacidad != 'normal':
        alojamientos = alojamientos.filter(Alojamiento.capacidad >= int(capacidad))
    

    # Ordenar los alojamientos según el parámetro de orden
    if orden == 'mayor-menor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.desc())
    elif orden == 'menor-mayor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.asc())

    # Ejecutar la consulta y obtener los resultados
    alojamientos_filtrados = alojamientos.all()

    form = Form()

    # Crear un diccionario de datos que contiene todos los datos necesarios
    context = {
        "form": form,
        "alojamientos": alojamientos_filtrados  # Pasar los alojamientos filtrados al template
    }

    # Renderizar la plantilla con los datos
    return render_template("alojamientos.html", **context)



@app.route("/alojamientos_desc/", methods=["GET"])
def listaAlojamientos2():
    # Obtener el parámetro de orden de la URL
    orden = request.args.get('orden')

    # Obtener todos los alojamientos sin filtrar
    alojamientos = Alojamiento.query

    # Obtener los filtros de la solicitud GET
    ciudad = request.args.get('ciudad', default='normal', type=str)
    tipo_inmueble = request.args.get('tipo_inmueble', default='normal', type=str)
    capacidad = request.args.get('capacidad', default='normal', type=str)


    # Aplicar los filtros según los parámetros recibidos
    if ciudad != 'normal':
        alojamientos = alojamientos.filter_by(ciudad=ciudad)
    if tipo_inmueble != 'normal':
        alojamientos = alojamientos.filter_by(tipo=tipo_inmueble)
    if capacidad != 'normal':
        alojamientos = alojamientos.filter(Alojamiento.capacidad >= int(capacidad))
    

    # Ordenar los alojamientos según el parámetro de orden
    if orden == 'mayor-menor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.desc())
    elif orden == 'menor-mayor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.asc())

    # Ejecutar la consulta y obtener los resultados
    alojamientos_filtrados = alojamientos.all()

    form = Form()

    # Crear un diccionario de datos que contiene todos los datos necesarios
    context = {
        "form": form,
        "alojamientos": alojamientos_filtrados  # Pasar los alojamientos filtrados al template
    }

    # Renderizar la plantilla con los datos
    return render_template("alojamientos_desc.html", **context)


@app.route("/alojamientos_nuev/", methods=["GET"])
def listaAlojamientos3():
    # Obtener el parámetro de orden de la URL
    orden = request.args.get('orden')

    # Obtener todos los alojamientos sin filtrar
    alojamientos = Alojamiento.query

    # Obtener los filtros de la solicitud GET
    ciudad = request.args.get('ciudad', default='normal', type=str)
    tipo_inmueble = request.args.get('tipo_inmueble', default='normal', type=str)
    capacidad = request.args.get('capacidad', default='normal', type=str)


    # Aplicar los filtros según los parámetros recibidos
    if ciudad != 'normal':
        alojamientos = alojamientos.filter_by(ciudad=ciudad)
    if tipo_inmueble != 'normal':
        alojamientos = alojamientos.filter_by(tipo=tipo_inmueble)
    if capacidad != 'normal':
        alojamientos = alojamientos.filter(Alojamiento.capacidad >= int(capacidad))
    

    # Ordenar los alojamientos según el parámetro de orden
    if orden == 'mayor-menor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.desc())
    elif orden == 'menor-mayor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.asc())

    # Ejecutar la consulta y obtener los resultados
    alojamientos_filtrados = alojamientos.all()

    form = Form()

    # Crear un diccionario de datos que contiene todos los datos necesarios
    context = {
        "form": form,
        "alojamientos": alojamientos_filtrados  # Pasar los alojamientos filtrados al template
    }

    # Renderizar la plantilla con los datos
    return render_template("alojamientos_nuev.html", **context)



@app.route('/obtener_detalles_alojamiento/<int:alojamiento_id>/')
def obtener_alojamiento_por_id(alojamiento_id):
    print(alojamiento_id)  # Corregir el nombre de la variable aquí
    alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
    form = Form()
    reserva = Reserva()


    context = {
        "form": form,
        "alojamiento": alojamiento,
        "reserva":reserva
    }

    return render_template("detallesAlojamiento.html", **context)


@app.route('/alojamientos_ubicacion/')
def mostrar_alojamientos():
    # Obtener el parámetro de orden de la URL
    orden = request.args.get('orden')

    # Obtener todos los alojamientos sin filtrar
    alojamientos = Alojamiento.query

    # Obtener los filtros de la solicitud GET
    ciudad = request.args.get('ciudad', default='normal', type=str)
    tipo_inmueble = request.args.get('tipo_inmueble', default='normal', type=str)
    capacidad = request.args.get('capacidad', default='normal', type=str)


    # Aplicar los filtros según los parámetros recibidos
    if ciudad != 'normal':
        alojamientos = alojamientos.filter_by(ciudad=ciudad)
    if tipo_inmueble != 'normal':
        alojamientos = alojamientos.filter_by(tipo=tipo_inmueble)
    if capacidad != 'normal':
        alojamientos = alojamientos.filter(Alojamiento.capacidad >= int(capacidad))
    

    # Ordenar los alojamientos según el parámetro de orden
    if orden == 'mayor-menor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.desc())
    elif orden == 'menor-mayor':
        alojamientos = alojamientos.order_by(Alojamiento.precio_por_noche.asc())

    # Ejecutar la consulta y obtener los resultados
    alojamientos_filtrados = alojamientos.all()

    form = Form()

    # Crear un diccionario de datos que contiene todos los datos necesarios
    context = {
        "form": form,
        "alojamientos": alojamientos_filtrados  # Pasar los alojamientos filtrados al template
    }

    # Renderizar la plantilla con los datos
    return render_template("alojamientos_ubicacion.html", **context)

@app.route('/obtener_detalles_alojamiento2/<int:alojamiento_id>/')
def obtener_alojamiento_por_id2(alojamiento_id):
    print(alojamiento_id)  # Corregir el nombre de la variable aquí
    alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
    form = Form()
    reserva = Reserva()


    context = {
        "form": form,
        "alojamiento": alojamiento,
        "reserva":reserva
    }

    return render_template("detallesAlojamiento2.html", **context)


@app.route('/galeria_img/<int:alojamiento_id>/')
def obtenerImagenesAlojamiento(alojamiento_id):
    print(alojamiento_id)  # Corregir el nombre de la variable aquí
    alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
    form = Form()

    context = {
        "form": form,
        "alojamiento": alojamiento
    }

    return render_template("imagenes_alojamiento.html", **context)

def get_last_reserva_id_from_database():
    last_reserva = Reserva.query.order_by(desc(Reserva.id)).first()
    if last_reserva:
        return last_reserva.id
    else:
        return 0  # Si no hay reservas en la base de datos, retornar 0 como el último ID

@app.route('/reservar/<int:alojamiento_id>/', methods=['GET', 'POST'])
def reservar_alojamiento(alojamiento_id):
    
    reserva = Reserva()
    id_reserva = get_last_reserva_id_from_database()

    if request.method == 'POST':
        data = request.json
        precio_total = request.json.get('precioTotal')
        precio_total = data.get('precioTotal')
        check_in = datetime.strptime(data.get('check_in'), '%Y-%m-%d')
        check_out = datetime.strptime(data.get('check_out'), '%Y-%m-%d')

        
        alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
        alojamiento.precio_total = precio_total
        alojamiento.check_in = check_in
        alojamiento.check_out = check_out

        # Incrementa el valor de id_reserva en 1 para cada nueva reserva
        id_reserva += 1
        reserva.id = id_reserva

        db.session.add(reserva)
        db.session.commit()

        context = {
            "alojamiento": alojamiento,
            "reserva":reserva,
            "id_reserva":id_reserva
        }

        # Después de actualizar el precio en la base de datos, puedes redirigir al usuario a otra página
        return render_template("confirmar_reserva.html", **context)
    
    else:
        # Lógica para manejar solicitudes GET
        alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
        form = Form()
        context = {
            "form": form,
            "alojamiento": alojamiento,
            "reserva":reserva,
            "id_reserva":id_reserva
        }
        return render_template("confirmar_reserva.html", reserva_id=reserva.id, **context)




@app.route('/reserva_hecha/<int:reserva_id>/', methods=['GET', 'POST'])
def guardar_reserva(reserva_id):
    alojamiento = Alojamiento()
    reserva = None

    if request.method == 'POST':
        # Obtener los datos de la solicitud POST
        data = request.json
        nombre = data.get('nombre')
        apellidos = data.get('apellidos')
        email = data.get('email')
        pais = data.get('pais')
        codigo_postal = data.get('codigo_postal')
        ciudad = data.get('ciudad')
        direccion = data.get('direccion')
        telefono = data.get('telefono')
        check_in = datetime.strptime(data.get('check_in'), '%Y-%m-%d')
        check_out = datetime.strptime(data.get('check_out'), '%Y-%m-%d')
        precio_total = data.get('precio_total')
        alojamiento_id = data.get('alojamiento_id')

        # Crear la nueva reserva con los datos recibidos
        reserva = Reserva(
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            pais=pais,
            codigo_postal=codigo_postal,
            ciudad=ciudad,
            direccion=direccion,
            telefono=telefono,
            check_in=check_in,
            check_out=check_out,
            precio_total = precio_total,
            alojamiento_id=alojamiento_id
        )

        # Guardar la reserva en la base de datos
        db.session.add(reserva)
        db.session.commit()

        print(reserva)

    else:
        # Obtener la reserva recién creada desde la base de datos
        reserva = Reserva.query.get(reserva_id)

        if reserva is None:
            # Manejar el caso en el que la reserva no existe
            return "Reserva no encontrada", 404

    # Renderizar la plantilla con los detalles de la reserva
    return render_template("reserva_hecha.html", reserva_id=reserva_id, alojamiento=alojamiento, reserva=reserva)






       



@app.route('/carrusel/<int:alojamiento_id>/')
def galeria_por_id(alojamiento_id):
    url_imagen = request.args.get('imagen')
    alojamiento = Alojamiento.query.get_or_404(alojamiento_id)
    
    # Obtener la lista de imágenes del alojamiento
    urls_imagenes = alojamiento.galeriaImagenes
    
    # Verificar si la URL de la imagen activa está en la lista de imágenes del alojamiento
    if url_imagen and url_imagen in urls_imagenes:
        # Establecer la imagen activa en el carrusel
        index_imagen_activa = urls_imagenes.index(url_imagen)
        imagenes_carrusel = [(url, i == index_imagen_activa) for i, url in enumerate(urls_imagenes)]
    else:
        # Si la URL de la imagen no está en la lista de imágenes del alojamiento,
        # establecer la primera imagen como activa por defecto
        imagenes_carrusel = [(url, i == 0) for i, url in enumerate(urls_imagenes)]
    
    form = Form()
    
    context = {
        "form": form,
        "alojamiento": alojamiento,
        "imagenes_carrusel": imagenes_carrusel,
        "url_imagen": url_imagen  # Pasar la URL de la imagen activa al contexto
    }
    
    return render_template("carrusel.html", **context)


# Para correr  el servidor localmente
# Utilizando el debug True, se actualiza automáticamente cada vez que modificamos el código
app.run(host="0.0.0.0", port=3001, debug=True)
# Utilizamos el codigo python main.py




