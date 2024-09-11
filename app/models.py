from app import db
from datetime import datetime, timedelta
from sqlalchemy import Sequence

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(1000))
    puntuacion = db.Column(db.Integer)
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class InformacionExtra (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vista = db.Column(db.String(100), nullable=False)
    piscina = db.Column(db.String(100), nullable=False)
    superficie = db.Column(db.Float, default=0)
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class GaleriaImagen (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagen1 = db.Column(db.String(100))
    imagen2 = db.Column(db.String(100))
    imagen3 = db.Column(db.String(100))
    imagen4 = db.Column(db.String(100))
    imagen5 = db.Column(db.String(100))
    imagen6 = db.Column(db.String(100))
    imagen7 = db.Column(db.String(100))
    imagen8 = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class Salon (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tele = db.Column(db.String(100))
    conexion = db.Column(db.String(100))
    comedor = db.Column(db.String(100))
    sillas = db.Column(db.String(100))
    ac = db.Column(db.String(100))
    sofa = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class Cocina (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horno = db.Column(db.String(100))
    microondas = db.Column(db.String(100))
    nevera = db.Column(db.String(100))
    vitro = db.Column(db.String(100))
    lavaplatos = db.Column(db.String(100))
    congelador = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))


class Bano (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vater = db.Column(db.String(100))
    bidet = db.Column(db.String(100))
    secador = db.Column(db.String(100))
    espejo = db.Column(db.String(100))
    ducha = db.Column(db.String(100))
    banera = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))


class Dormitorio (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cama = db.Column(db.String(100))
    aire = db.Column(db.String(100))
    ropero = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))


class Terraza (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mesa = db.Column(db.String(100))
    sillas = db.Column(db.String(100))
    toldo = db.Column(db.String(100))
    barbacoa = db.Column(db.String(100))
    muebles = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class Piscina (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    muebles = db.Column(db.String(100))
    tipo = db.Column(db.String(100))
    tamano = db.Column(db.String(100))
    profundidad = db.Column(db.String(100))
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class Reserva (db.Model):
    id = db.Column(db.Integer, Sequence('reserva_id_seq'), primary_key=True)
    precio_total = db.Column(db.Float)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    codigo_postal = db.Column(db.Integer, nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.Text, nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.Date, nullable = False)
    check_out = db.Column(db.Date, nullable = False)
    alojamiento_id = db.Column(db.Integer, db.ForeignKey('alojamiento.id'))

class Alojamiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    urlImg = db.Column(db.String(200), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    tipo = db.Column(db.String(50), nullable=False) 
    numero_habitaciones = db.Column(db.Integer, nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)
    precio_por_noche = db.Column(db.Float, nullable=False)
    numero_habitaciones = db.Column(db.Integer, nullable=False)
    calificacion = db.Column(db.Float)
    cama_matrimonio = db.Column(db.Integer, nullable=False)
    baño = db.Column(db.Integer, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    distancia_playa = db.Column(db.String(10), nullable=False)
    restaurante = db.Column(db.String(10), nullable=False)
    compra = db.Column(db.String(10), nullable=False)
    url_ubi = db.Column(db.String(500), nullable=False)
    nuevo = db.Column(db.Boolean) 
    descuento = db.Column(db.Boolean) 
    precio_descuento = db.Column(db.Integer, default=0)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    precio_total = db.Column(db.Float)
    check_in = db.Column(db.Date, default=datetime.today)
    check_out = db.Column(db.Date, default=lambda: datetime.today() + timedelta(days=7))
    
    descripcionUbicacion = db.Column(db.String(500)) 

    
    informacionExtras = db.relationship('InformacionExtra', backref='alojamiento', lazy=True)
    comentarios = db.relationship('Comentario', backref='alojamiento', lazy=True)
    galeriaImagenes = db.relationship('GaleriaImagen', backref='alojamiento', lazy=True)
    carateristicasSalon = db.relationship('Salon', backref='alojamiento', lazy=True)
    caracteristicasCocina = db.relationship('Cocina', backref='alojamiento', lazy=True)
    caracteristicasBano = db.relationship('Bano', backref='alojamiento', lazy=True)
    caracteristicasDormitorio = db.relationship('Dormitorio', backref='alojamiento', lazy=True)
    caracteristicasTerraza = db.relationship('Terraza', backref='alojamiento', lazy=True)
    caracteristicasPiscina = db.relationship('Piscina', backref='alojamiento', lazy=True)
    informacionReservas = db.relationship('Reserva', backref='alojamiento', lazy=True)
    
    
    def __repr__(self):
        return f"Alojamiento(id={self.id}, nombre='{self.nombre}')"
    

    def calcular_media_puntuacion(self):
        if self.comentarios:
            puntuaciones = [comentario.puntuacion for comentario in self.comentarios]
            media = sum(puntuaciones) / len(puntuaciones)
            return round(media, 2)
        else:
            return None



    def informacionReserva (self, precio_total, nombre, apellidos, email, pais, codigo_postal,
                            ciudad, direccion, telefono):
        informacionReserva = Reserva(precio_total = precio_total, nombre = nombre, apellidos = apellidos,
                                     email = email, pais = pais, codigo_postal = codigo_postal,
                                     ciudad = ciudad, direccion = direccion, telefono = telefono)
        self.informacionReservas.append(informacionReserva)
        


    def caracteristicaPiscina (self, muebles, tipo, tamano, profundidad):
        caracteristicaPiscina = Piscina(muebles = muebles, tipo = tipo, tamano = tamano, profundidad = profundidad)
        self.caracteristicasPiscina.append(caracteristicaPiscina)


    def caracteristicaTerraza (self, mesa, sillas, toldo, barbacoa, muebles):
        caracteristicaTerraza = Terraza (mesa = mesa, sillas = sillas, toldo = toldo, barbacoa=barbacoa, muebles = muebles)
        self.caracteristicasTerraza.append(caracteristicaTerraza)



    def caracteristicaDormitorio (self, cama, aire, ropero):
            caracteristicaDormitorio = Dormitorio(cama= cama, aire = aire, ropero = ropero)
            self.caracteristicasDormitorio.append(caracteristicaDormitorio)
        
    
    def caracteristicaBano(self, vater, bidet, secador, espejo, ducha, banera):
        caracteristicaBano = Bano(vater = vater, bidet = bidet, secador = secador, espejo = espejo, ducha = ducha,
                                  banera = banera)
        self.caracteristicasBano.append(caracteristicaBano)


    def caracteristicaSalon(self, tele, conexion, comedor, sillas, ac, sofa):
        caracteristicaSalon = Salon(tele=tele, conexion = conexion, comedor = comedor,
                                    sillas= sillas, ac = ac, sofa = sofa)
        self.carateristicasSalon.append(caracteristicaSalon)


    def caracteristicaCocina(self, horno, microondas, nevera, vitro, lavaplatos, congelador):
        caracteristicaCocina = Cocina(horno = horno, microondas = microondas, nevera = nevera, vitro = vitro, 
                                      lavaplatos = lavaplatos, congelador = congelador)
        self.caracteristicasCocina.append(caracteristicaCocina)
        


    def agregarImagenes(self, imagen1, imagen2, imagen3, imagen4, imagen5, imagen6, imagen7, imagen8):
        agregarImagen = GaleriaImagen (imagen1 = imagen1, imagen2 = imagen2, imagen3 = imagen3,
                                        imagen4 = imagen4, imagen5 = imagen5, imagen6 = imagen6,
                                        imagen7 = imagen7, imagen8 = imagen8)
        self.galeriaImagenes.append(agregarImagen)
    
    def agregarInformacionExtra (self, vista, piscina, superficie):
        informacionExtra = InformacionExtra(vista=vista, piscina=piscina, superficie=superficie)
        self.informacionExtras.append(informacionExtra)

    def agregarInformacionExtra (self, vista, piscina, superficie):
        informacionExtra = InformacionExtra(vista=vista, piscina=piscina, superficie=superficie)
        self.informacionExtras.append(informacionExtra)


    def agregar_comentario(self, nombre, descripcion, puntuacion):
        comentario = Comentario(nombre=nombre, descripcion=descripcion, puntuacion=puntuacion)
        self.comentarios.append(comentario)

    def agregar_caracteristicas_salon(self, salon):
        if self.salon is None:
            self.salon = salon
        else:
            self.salon += ',' + salon

    def agregar_caracteristicas_cocina(self, cocina):
        if self.cocina is None:
            self.cocina = cocina
        else:
            self.cocina += ',' + cocina

    def agregar_caracteristicas_bano2(self, bano2):
        if self.bano2 is None:
            self.bano2 = bano2
        else:
            self.bano2 += ',' + bano2

    def agregar_caracteristicas_dormitorio(self, dormitorio):
        if self.dormitorio is None:
            self.dormitorio = dormitorio
        else:
            self.dormitorio += ',' + dormitorio

    def agregar_caracteristicas_terraza(self, terraza):
        if self.terraza is None:
            self.terraza = terraza
        else:
            self.terraza += ',' + terraza

    def agregar_caracteristicas_piscina(self, piscina2):
        if self.piscina2 is None:
            self.piscina2 = piscina2
        else:
            self.piscina2 += ',' + piscina2