from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from datetime import datetime, timedelta

db = SQLAlchemy()  # Instancia de SQLAlchemy

def create_app():
    # Inicializamos la aplicación: name hace referencia al nombre de main.py
    app = Flask(__name__)
    # Inicializar bootstrap para que funcione en nuestra app
    Bootstrap(app) 
    app.config.from_object(Config)

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    with app.app_context():
        db.create_all()


    return app



def crear_alojamientos():
    # Crear instancias de Alojamiento
    from app.models import Alojamiento, InformacionExtra, GaleriaImagen, Salon, Cocina, Bano, Dormitorio, Terraza, Piscina
    from app.models import Comentario

    # Eliminar todos los alojamientos existentes
    Alojamiento.query.delete()
    Comentario.query.delete()
    InformacionExtra.query.delete()
    GaleriaImagen.query.delete()
    Salon.query.delete()
    Cocina.query.delete()
    Bano.query.delete()
    Dormitorio.query.delete()
    Terraza.query.delete()
    Piscina.query.delete()

    fecha_actual = datetime.now().date()
    fecha_check_out = fecha_actual + timedelta(days=7)


    alojamiento1 = Alojamiento(nombre="Desmais", urlImg="https://api.net2rent.com/pfiles/145/16864/339605-o-m.jpg", 
                               descripcion="¡Bienvenido a los apartamentos Desmais que lo tienen todo! Disfrute del confort y la relajación en estos espacios que le ofrecen una experiencia inolvidable. Sumérjase en el frescor de la piscina comunitaria y relájese en su terraza privada, donde podrá disfrutar del sol mediterráneo a su ritmo. Manténgase conectado con el mundo gracias al aire acondicionado y a la conexión wifi disponible en todo momento. La decoración sencilla y funcional crea un ambiente acogedor y moderno, complementado con un equipamiento de última generación que te hará sentir como en casa desde el primer momento. En el interior, encontrarás una pequeña cocina americana equipada con todo lo necesario para preparar tus comidas favoritas, mientras que el salón-comedor con un gran sofá te invita a relajarte y disfrutar de momentos inolvidables. El dormitorio con cama de matrimonio le garantiza un descanso reparador, y el cuarto de baño privado con ducha, toallas y ropa de cama completa la experiencia de confort. La cocina está totalmente equipada con microondas, hervidor de agua y vitrocerámica, dándole la libertad de preparar sus propias delicias culinarias. Descubra la sencillez y el confort en estos apartamentos, donde cada detalle está pensado para que su estancia sea inolvidable.", tipo="Apartamento",
                            direccion="Passeig del Riu, 60, 07750 Cala Galdana, Illes Balears", ciudad="Cala Galdana, Menorca", pais="España",
                            precio_por_noche=100.0, numero_habitaciones=1, calificacion=8.2,
                            cama_matrimonio=2, baño=1, capacidad=4, distancia_playa="200m", restaurante="500m",
                            compra="200m", url_ubi = "https://www.google.com/maps/search/Passeig+del+Riu,+60,+07750+Cala+Galdana,+Illes+Balears/@39.9429833,3.9604141,17z/data=!3m1!4b1?entry=ttu", 
                            nuevo = False, descuento = True, precio_descuento = 5,
                            latitud = 39.942963, longitud = 3.962961,
                            descripcionUbicacion="¡Bienvenidos a nuestro alojamiento en Cala Galdana! Situado a solo unos pasos del centro y la playa, este encantador lugar ofrece la combinación perfecta de comodidad y conveniencia. Ubicado en una zona muy tranquila, es ideal tanto para parejas como para familias. Disfruta de la serenidad de este hermoso enclave mientras creas recuerdos inolvidables con tus seres queridos. ¡Te esperamos para una experiencia inolvidable en Cala Galdana!")
    
    
    alojamiento1.agregar_comentario("David Febrer", "Apartamento increible", 10)
    alojamiento1.agregarInformacionExtra("Piscina", "Comunitaria", 25)
    alojamiento1.agregarImagenes("https://api.net2rent.com/pfiles/145/16864/339611-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/339609-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/339608-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/348771-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/421532-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/421539-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/421540-o-m.jpg",
                                 "https://api.net2rent.com/pfiles/145/16864/421541-o-m.jpg")
    
    alojamiento1.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "4 sillas", "Aire acondicionado", "Sofa-Cama")
    alojamiento1.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento1.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento1.caracteristicaDormitorio("Cama doble", "Aire Acondicionado", "Ropero")
    alojamiento1.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento1.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 9m x 5m", "Profundidad: 1m - 2m")



    
    alojamiento2 = Alojamiento(nombre="Annabel's", urlImg="https://api.net2rent.com/pfiles/145/20522/464504-m.jpg", 
                            descripcion="Bienvenidos a Annabel's Apartments, un magnífico complejo turístico situado en la tranquila urbanización de Cala Galdana, en la costa sur de Menorca. A tan sólo 800 metros de la playa, este alojamiento le invita a disfrutar de la tranquilidad y el confort en un entorno excepcional. Sumérjase en la esencia mediterránea con las amplias zonas ajardinadas, la refrescante piscina y el relajante solarium que le ofrece el complejo. La atención y el confort son primordiales, por eso disponemos de lavandería, parking privado y WiFi gratuito en todo el complejo. Annabel's Apartments le da la bienvenida con un encantador espacio de estar que incluye un cómodo sofá y un televisor de pantalla plana. La zona de comedor es perfecta para disfrutar de las comidas. La cocina, totalmente equipada, dispone de microondas, placa eléctrica y frigorífico, lo que le dará libertad para preparar sus propias delicias. Con un acogedor dormitorio, un baño completo y una terraza privada, cada rincón de estos apartamentos ha sido diseñado para ofrecerle una experiencia inolvidable. Descubra la serenidad de Cala Galdana desde Annabel's Apartments y experimente la auténtica belleza de Menorca.", tipo="Apartamento",
                            direccion="Avenida XYZ", ciudad="Cala Galdana, Menorca", pais="España",
                            precio_por_noche=60.0, numero_habitaciones=1, calificacion=7.3,
                            cama_matrimonio=1, baño=1, capacidad=2, distancia_playa="800m", restaurante="600m",
                            compra="450m", url_ubi="https://www.google.com/maps/place//@39.9424502,3.9605098,18.25z?entry=ttu", 
                            nuevo = False, descuento = True, precio_descuento = 10,
                            latitud = 39.942001, longitud = 3.9607)
    

    alojamiento2.agregar_comentario("Juan Miranda", "Apartamento con todo lo necesario", 9)
    alojamiento2.agregarInformacionExtra("Piscina", "Comunitaria", 30)
    alojamiento2.agregarImagenes("https://api.net2rent.com/pfiles/145/12457/285371-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285375-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285374-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285372-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285378-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285376-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285370-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12457/285377-o-l.jpg")
    
    alojamiento2.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "2 sillas", "Ventilador", "Sofa")
    alojamiento2.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento2.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento2.caracteristicaDormitorio("Cama doble", "Ropero", "Mesita noche")
    alojamiento2.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento2.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 15m x 8m", "Profundidad: 1m - 2m")




    
    alojamiento3 = Alojamiento(nombre="Gama", urlImg="https://api.net2rent.com/pfiles/145/12444/201509-o-m.jpg", descripcion="Bienvenido a este precioso apartamento en un complejo con encanto, a sólo cinco minutos a pie de la playa de Cala Galdana. Prepárese para sumergirse en el confort y la serenidad en este rincón del paraíso. Con dos dormitorios, cada uno con su propio cuarto de baño con ducha, este apartamento ofrece privacidad y elegancia. La cocina abierta al comedor y al salón ha sido diseñada con muebles modernos y funcionales, asegurando que cada momento sea una delicia. Imagine despertarse y disfrutar de la brisa marina desde la terraza del salón, con impresionantes vistas a la piscina y al solarium de los apartamentos. Este espacio se convierte en su propio oasis de tranquilidad y belleza. Además, el confort se completa con un toque especial: tu propio parking privado, para que tu escapada sea aún más relajada y despreocupada. ¡Prepárese para vivir momentos inolvidables en este precioso apartamento, cuyo encanto se encuentra a pocos pasos de la playa de Cala Galdana!", tipo="Apartamento",
                            direccion="Calle 456", ciudad="Cala Galdana, Menorca", pais="España",
                            precio_por_noche=90.0, numero_habitaciones=2, calificacion=8.0,
                            cama_matrimonio=2, baño=2, capacidad=4, distancia_playa="100m", restaurante="80m",
                            compra="100m", url_ubi="https://www.google.com/maps/place/Apartamento+Gama/@39.9380992,3.9632939,17.75z/data=!4m9!3m8!1s0x12be1daf842ddc65:0x25af107a7774e16c!5m2!4m1!1i2!8m2!3d39.9386304!4d3.964843!16s%2Fg%2F11k5xfnkl2?entry=ttu", 
                            nuevo = False, descuento = True, precio_descuento = 15, precio_total = 630.0,
                            latitud = 39.938599, longitud = 3.9648)


    alojamiento3.agregar_comentario("Lola Pons", "Magníficas vistas", 10)
    alojamiento3.agregarInformacionExtra("Piscina", "Comunitaria", 15)
    alojamiento3.agregarImagenes("https://api.net2rent.com/pfiles/145/12444/202043-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12444/202041-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12444/201509-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12445/202036-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12445/202037-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12445/202034-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12444/202043-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12444/202041-o-l.jpg"
                                 )
    
    alojamiento3.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "4 sillas", "Ventilador", "Sofa")
    alojamiento3.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento3.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento3.caracteristicaDormitorio("Cama doble", "Ropero", "Mesita noche")
    alojamiento3.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento3.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 15m x 8m", "Profundidad: 1m - 2m")
    
    
    
    alojamiento4 = Alojamiento(nombre="Villa Verano", urlImg="https://api.net2rent.com/pfiles/145/12439/491404-l.jpg", descripcion="Sumérjase en el lujo y la serenidad con esta impresionante casa de 4 dormitorios y 3 baños, situada en un entorno privilegiado con impresionantes vistas al mar. Desde el momento en que entra por la puerta, le espera una experiencia única. La cocina, totalmente equipada, se funde a la perfección con un espacioso salón diseñado para maximizar tanto el confort como la funcionalidad. Cada rincón ha sido cuidadosamente pensado para ofrecerle un estilo de vida elegante y relajado. Sin embargo, la verdadera joya de esta propiedad reside en su amplia terraza. Una zona de barbacoa perfectamente ubicada y, a sólo unos pasos, sumergirse en la impresionante piscina infinita que se funde armoniosamente con el horizonte oceánico. Esta residencia redefine la elegancia y el lujo en cada detalle, proporcionando un hogar perfecto para aquellos que buscan disfrutar de la belleza del mar desde la privacidad y la comodidad de su propio espacio. En Villa Panorama, cada día es una experiencia única. Descubra el placer de vivir en un hogar donde el lujo y la naturaleza se encuentran en perfecta armonía. ¡Bienvenido a su paraíso frente al mar!", tipo="Villa",
                            direccion="Calle 456", ciudad="Son Bou, Menorca", pais="España",
                            precio_por_noche=310.00, numero_habitaciones=4, calificacion=9.0,
                            cama_matrimonio=4, baño=2, capacidad=8, distancia_playa="100m", restaurante="80m",
                            compra="100m", url_ubi="https://www.google.com/maps/place/Apartamento+Gama/@39.9380992,3.9632939,17.75z/data=!4m9!3m8!1s0x12be1daf842ddc65:0x25af107a7774e16c!5m2!4m1!1i2!8m2!3d39.9386304!4d3.964843!16s%2Fg%2F11k5xfnkl2?entry=ttu",
                            nuevo = True, descuento = False, precio_total = 2170.0,
                            latitud = 39.904911, longitud = 4.07421)
    

    alojamiento4.agregar_comentario("Jorge Moll", "Villa explendida, con todo lo necesario para pasar un agradble tiempo en familia", 10)
    alojamiento4.agregarInformacionExtra("Piscina", "Privada", 50)
    alojamiento4.agregarImagenes("https://api.net2rent.com/pfiles/145/12439/491404-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/201616-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/201626-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/201621-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/491401-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/491402-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/491405-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/12439/491408-l.jpg")
    
    alojamiento4.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "8 sillas", "Aire Acondicionado", "Sofa")
    alojamiento4.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento4.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento4.caracteristicaDormitorio("Cama doble", "Ropero", "Mesita noche")
    alojamiento4.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento4.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 15m x 8m", "Profundidad: 1m - 2m")



    
    alojamiento5 = Alojamiento(nombre="Villa Etxe", urlImg="https://api.net2rent.com/pfiles/145/17939/495902-l.jpg", descripcion="Descubra su paraíso junto al mar en esta encantadora casa de 4 dormitorios y 3 baños, con un toque exclusivo gracias a su aseo adicional. Las vistas al mar desde cada ventana te harán sentir como en un sueño. La cocina y el amplio salón se unen para crear un espacio acogedor y funcional, diseñado para su máximo confort. La verdadera joya de la propiedad es la amplia terraza: una zona de barbacoa le espera para los momentos al aire libre, mientras que la piscina infinita redefine la elegancia y el lujo con su perfecta fusión con el horizonte oceánico. Esta residencia es mucho más que un hogar; es una experiencia de vida única para aquellos que buscan disfrutar del mar con privacidad y comodidad. ¡Bienvenido a su nuevo hogar frente al mar!", tipo="Villa",
                            direccion="Calle 456", ciudad="Son Bou, Menorca", pais="España",
                            precio_por_noche=340.00, numero_habitaciones=4, calificacion=9.2,
                            cama_matrimonio=4, baño=2, capacidad=8, distancia_playa="100m", restaurante="80m",
                            compra="100m", url_ubi="https://www.google.com/maps/place/Apartamento+Gama/@39.9380992,3.9632939,17.75z/data=!4m9!3m8!1s0x12be1daf842ddc65:0x25af107a7774e16c!5m2!4m1!1i2!8m2!3d39.9386304!4d3.964843!16s%2Fg%2F11k5xfnkl2?entry=ttu",
                            nuevo = True, descuento = False, precio_total = 2380.0,
                            latitud = 39.90498, longitud = 4.073971)
    

    alojamiento5.agregar_comentario("Antonio Jose", "Estancia mejorable", 7)
    alojamiento5.agregarInformacionExtra("Piscina", "Privada", 30)
    alojamiento5.agregarImagenes("https://api.net2rent.com/pfiles/145/17939/384434-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/384436-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/384435-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/495903-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/384432-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/495901-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/384438-o-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/17939/384440-o-l.jpg")
    
    alojamiento5.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "8 sillas", "Aire Acondicionado", "Sofa")
    alojamiento5.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento5.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento5.caracteristicaDormitorio("Cama doble", "Ropero", "Mesita noche")
    alojamiento5.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento5.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 15m x 8m", "Profundidad: 1m - 2m")




    alojamiento6 = Alojamiento(nombre="Villa Úrsula", urlImg="https://api.net2rent.com/pfiles/145/20036/444409-m.jpg", descripcion="¡Bienvenido a esta hermosa casa con impresionantes vistas al mar! Disfrute de la serenidad y el confort en este oasis que ofrece una hermosa piscina privada, una barbacoa para disfrutar de deliciosas comidas al aire libre, wifi gratuito y calefacción para hacer su estancia aún más agradable. Con 4 dormitorios y 3 baños, esta casa es ideal para familias y grupos de amigos que deseen pasar unas vacaciones inolvidables. Dormitorio 1: Cama de matrimonio, baño privado y aire acondicionado. Dormitorio 2: Dos camas individuales y aire acondicionado. Dormitorio 3: Dos camas individuales y aire acondicionado. Dormitorio 4: Cama doble, baño privado y aire acondicionado. La casa está situada en Santo Tomas, una zona tranquila con todos los servicios y opciones de ocio que pueda desear, como restaurantes, bares, supermercados y tiendas. ¡Esperamos que disfrute de una estancia agradable y muy placentera durante sus vacaciones en esta encantadora casa en Santo Tomas!", tipo="Villa",
                            direccion="Calle 456", ciudad="Sonto Tomás, Menorca", pais="España",
                            precio_por_noche=280.00, numero_habitaciones=4, calificacion=7.3,
                            cama_matrimonio=4, baño=2, capacidad=8, distancia_playa="100m", restaurante="80m",
                            compra="100m", url_ubi="https://www.google.com/maps/place/Apartamento+Gama/@39.9380992,3.9632939,17.75z/data=!4m9!3m8!1s0x12be1daf842ddc65:0x25af107a7774e16c!5m2!4m1!1i2!8m2!3d39.9386304!4d3.964843!16s%2Fg%2F11k5xfnkl2?entry=ttu",
                            nuevo = True, descuento = False, precio_total = 1960.0,
                            latitud = 39.919659, longitud = 4.03909)



    alojamiento6.agregar_comentario("Harry Kane", "Villa con vistas al mar", 10)
    alojamiento6.agregarInformacionExtra("Piscina", "Privada", 30)
    alojamiento6.agregarImagenes("https://api.net2rent.com/pfiles/145/20036/444410-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20036/444411-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20036/444412-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20036/444413-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20036/444414-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20036/444415-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20040/444421-l.jpg",
                                 "https://api.net2rent.com/pfiles/145/20040/444422-l.jpg")
    
    alojamiento6.caracteristicaSalon("TV pantalla plana", "TV conexión por satélite", "Comedor", "8 sillas", "Aire Acondicionado", "Sofa")
    alojamiento6.caracteristicaCocina("Horno", "Microondas", "Vitro eléctica", "Lavaplatos", "Nevera", "Congelador")
    alojamiento6.caracteristicaBano("Vater", "Bidet", "Secador", "Espejo", "Ducha", "Bañera")
    alojamiento6.caracteristicaDormitorio("Cama doble", "Ropero", "Mesita noche")
    alojamiento6.caracteristicaTerraza("Mesa", "Sillas", "Toldo", "Barbacoa", "Muebles exterior")
    alojamiento6.caracteristicaPiscina("Muebles exterior", "Piscina comunitaria", "Tamaño: 15m x 8m", "Profundidad: 1m - 2m")



    # Agregar los alojamientos a la sesión y confirmar los cambios en la base de datos
    db.session.add_all([alojamiento1, alojamiento2, alojamiento3, alojamiento4, alojamiento5, alojamiento6])
    db.session.commit()
