# Copyright 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, exceptions

class CountryStateCity(models.Model):
    """
    Model added to manipulate separately the cities on Partner address.
    """
    _description = 'Model to manipulate Cities'
    _name = 'res.country.state.city'

    code = fields.Char('City Code', size=5, help='Code DANE - 5 digits-',)
    name = fields.Char('City Name', size=64, )
    state_id = fields.Many2one('res.country.state', 'State')
    country_id = fields.Many2one('res.country', 'Country', default='Colombia')
    _order = 'code'


class Lead(models.Model):
    _inherit = "crm.lead"

    x_nombre = fields.Char(
    	related ="name",
        string="2. Nombre del Propietario",
        help="Ingrese el nombre del propietario",
        readonly=False
    )

    x_nombre_negocio = fields.Char(
        string="1. Nombre del Negocio",
        help="Ingrese el nombre del negocio",
        readonly=False
    )

    x_vereda = fields.Char(
        string="10. Barrio/Vereda",
        help="Tax Identification Number. The first 2 characters are the "
        "country code.",
    )

    x_datos1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )

    doctype = fields.Selection(
        [
            ('1', 'Sin identificación'),
            ('2', 'Cédula'),
            ('3', 'Cédula de extranjería'),
            ('4', 'Pasaporte'),
            ('5', 'Permiso especial de permanencia (PEP)'),

        ], "3. Tipo de identificación", default='2'
    )

    x_identification = fields.Integer(
        string="4. Número de identificación",
        help="Ingrese el tipo de identificación ",
        store=True,
    )

    _sql_constraints = [
        ('x_identification',
         'UNIQUE (x_identification)',
         "El número de documento debe ser único!"),
    ]

    x_sexo = fields.Selection(
        #string="Sexo",
        [
            ('10', 'Masculino'),
            ('11', 'Femenino'),

        ], "5. Sexo", 
    )

    x_etnia = fields.Selection(
        #string="¿Pertenece a algún tipo de etnia?",
        [
            ('20', 'NARP'),
            ('21', 'Gitano ROM'),
            ('22', 'Indígena'),
            ('23', 'No pertenezco'),

        ], "6. ¿Pertenece a algún tipo de etnia?", 
    )

    x_edad = fields.Integer(
        string="7. Edad",
        help="Escriba su edad", 
    )

    x_limitacion = fields.Char(
        string="13. ¿Usted tiene algún tipo de diversidad funcional?",
        help="Describa sus limitaciones físicas", 
    )

    x_escolaridad = fields.Selection(
        [
            ('30', 'Primaria incompleta'),
            ('31', 'Primaria completa'),
            ('32', 'Secundaria incompleta'),
            ('33', 'Secundaria completa'),
            ('34', 'Técnico'),
            ('35', 'Tecnólogo'),
            ('36', 'Educación No formal: Cursos libres, diplomados,seminarios.'),
            ('37', 'Tecnólogo'),
            ('38', 'Pregrado'),
            ('39', 'Especialización'),
            ('40', 'Maestría'),
            ('41', 'Ninguno'),

        ], "14. Ultimo año de escolaridad", 
    )

    #x_cual = fields.Char(
        #string="Cual?",
        #help="Escriba los detalles",
    #)

    x_grupos = fields.Selection(
    	[
            ('40', 'Si'),
            ('41', 'No'),

        ], "15. ¿Pertenece a alguna organización:  asociación, corporación, cooperativa, grupo?",

        help="Escriba el tipo de organización a la cual pertenece",
    )

    x_grupos_cual = fields.Char(
        string="¿Cuál?",
        help="16. ¿A qué tipo de organización, asociación, corporación, cooperativa, grupo pertenece?",
    )

    x_estrato = fields.Selection(
        [
            ('40', '1'),
            ('41', '2'),
            ('42', '3'),
            ('43', '4'),
            ('44', '5'),
            ('45', '6'),
        ], "17. Estrato socioeconómico de residencia ",
    )

    x_situacion = fields.Selection(
        [
            ('40', 'Cuenta propia'),
            ('41', 'Empleador'),
        ], "18. Actualmente usted es"
    )

    x_actcomer = fields.Selection(
    	[
            ('40', 'Peluquería, salón de belleza, barbería, arreglo de uñas'),
            ('41', 'Cafetería o  salón de onces'),
            ('42', 'Elaboración de productos de panadería, tortas, pasteles, pudin, ponques'),
            ('43', 'Comidas rápidas '),
            ('44', 'Bar, taberna, estanco, licorera, discoteca, rumbeadero'),
            ('45', 'Tienda'),
            ('46', 'Billares, juegos de mesa, rana, gallera'),
            ('47', 'Comercio  de colchones, muebles'),
            ('48', 'Comercio de elementos deportivos, implementos, balones, tienda de bicicletas'),
            ('49', 'Veterinaria, venta de alimento o enseres para mascotas o animales, perros, gatos, peces.'),
            ('50', 'Comercio de productos de tecnología, celulares, computadores'),
            ('51', 'Productos asociados al arte, cuadros, pintura, joyería, relojería, actividades de fotografía'),
            ('52', 'Comercio de regalos, variedades, adornos, tajetas, articulos diversos.'),
            ('53', 'Heladería o frutería '),
            ('54', 'Carnicería, pescadería, charcutería, quesos, lácteos, salsamentaria'),
            ('55', 'Cerrajería, ferretería, ferreléctricos, vidriería'),
            ('56', 'Servicios de salud, óptica, odontología, consultorio médico, ortodoncia, tienda naturista'),
            ('57', 'Droguería'),
            ('58', 'Envíos, giros, recargas, chance, apuestas, servicios financieros, banco, corresponsal'),
            ('59', 'Café internet, telecomunicaciones, videojuegos, venta de películas, mantenimiento computadores, telefonía, informática'),
            ('60', 'Floristería, abono, venta de gallinas, actividad pecuaria'),
            ('61', 'Retaurante, fondo paisa, corrientazo, asadero'),
            ('62', 'Papelería, fotocopias, impresiones, miscelanea'),
            ('63', 'Casa comercial, monte de piedad, compraventa, prestamista'),
            ('64', 'Eventos, refrigerios, casa de banquetes'),
            ('65', 'Gimnasio, academia de baile, establecimiento para deportes'),
            ('66', 'Academia de idiomas, lectura rápida'),
            ('67', 'Inmobiliaria'),
            ('68', 'Asesoría comercial, publicidad, mercadeo imagen corporativa, asesoría jurídica, tributaria'),
            ('69', 'Mantenimiento de bicicletas, automóviles, despinche, vulcanizadora, taller automotriz, mecánica general'),
            ('70', 'Lavandería'),
            ('71', 'Supermercado, minimercado, mercado, venta de elementos de aseo, venta de frutas y verduras'),
            ('72', 'Venta de ropa, zapatos, calzado, modestería, uniformes, accesorios, prendas y elementos de vestir, remontadora de calzado'),
            ('73', 'Parqueadero de carros, motos, bicicletas'),
            ('74', 'Productos de belleza, spa, tatuajes'),
            ('75', 'Fábrica de manufacturas textiles ropa calzado balones deportivos cueros marroquinería'),
            ('76', 'Venta y comercio de autopartes, carros, vehículos, motos, partes de motocicleta, cascos, automotores'),
            ('77', 'Fábrica y venta de productos metálicos hierro acero maquinaria y otras aplicaciones industriales'),
            ('78', 'Jardín infantil, salacuna, educación'),
            ('79', 'Transporte de pasajeros'),
        ], "20. ¿Cuál es la actividad comercial de su negocio?",
        help="Escriba la actividad comercial de su negocio",
    )

    x_sector = fields.Selection(
        [
            ('40', 'Agropecuario'),
            ('41', 'Comercio'),
            ('42', 'Servicios'),
            ('43', 'Industrial'),
        ], "19. ¿En qué sector económico se encuentra su negocio?",
        help="Escriba el sector económico de su negocio ",
    )

    x_ubic = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Zona Urbana'),
            ('51', 'Zona rural'),

        ], "23. Ubicación del negocio",
    )

    x_com_cuenta = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Establecimiento'),
            ('51', 'Sin establecimiento'),

        ], "24. Su actividad comercial cuenta con",
    )

    x_cont1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "Una vez comprendido el programa de acompañamiento, ¿usted desea continuar?",
    )

    x_datos3 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "ACEPTA ENTREGARLE A UNIMINUTO LOS DATOS GENERALES SUYOS Y DEL MICRONEGOCIO CON FINES ACADÉMICOS",
    )

    x_microneg = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Formalizado'),
            ('51', 'Informal'),

        ], "25. ¿Su micronegocio está?",
    )

    x_sisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "26. ¿Usted pertenece al Sisben?",
    )

    x_tsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Urbano'),
            ('51', 'Rural'),

        ], "27. ¿Su Sisben es?",
    )

    x_nsisben = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Nivel 1 '),
            ('51', 'Nivel 2 '),
            ('52', 'Nivel 3 '),

        ], "28. ¿Cuál es el nivel de Sisben que usted tiene?",
    )

    x_estrato_neg = fields.Selection(
        [
            ('40', '1'),
            ('41', '2'),
            ('42', '3'),
            ('43', '4'),
            ('44', '5'),
            ('45', '6'),
        ], "29. Estrato socioeconómico de donde se encuentra el negocio ",
    )

    x_tactiv = fields.Integer(
    	string="30. ¿Cuánto tiempo lleva su negocio en funcionamiento? (Meses)",
    )

    x_dias_sem_inf = fields.Integer(
        string="31. ¿Cuántas horas de trabajo diario dedica para el funcionamiento del negocio?",
    )

    x_dias_sem_for = fields.Integer(
        string="31. ¿Cuántos días a la semana opera su negocio? ",
    )

    x_dias_sem_for2 = fields.Integer(
        string="32. ¿Cuántos días a la semana dedica a su negocio?",
    )

    x_horas_trab_inf = fields.Integer(
        string="32. ¿Cuántas horas de trabajo diario dedica para el funcionamiento del negocio?",
    )

    x_horas_trab_form = fields.Integer(
        string="33. ¿Cuántas horas de trabajo diario dedica para el funcionamiento del negocio?",
    )

    x_trabajadores_inf = fields.Integer(
        string="33. ¿Cuántos trabajadores tiene su negocio?",
    )

    x_trabajadores_form = fields.Integer(
        string="34. ¿Cuántos trabajadores tiene su negocio?",
    )

    x_cotiza_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Salud'),
            ('51', 'Pensión'),
            ('52', 'ARL'),
            ('53', 'Caja de compensación'),
            ('53', 'ICBF'),
            ('53', 'SENA'),
            ('53', 'Todas'),

        ], "35. ¿Cuáles son los aportes que realiza para sus trabajadores?",
    )

    x_cotiza_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Salud'),
            ('51', 'Pensión'),
            ('52', 'ARL'),
            ('53', 'Ninguna'),

        ], "34. ¿Cuáles son los aportes que realiza su negocio?",
    )

    x_motivo_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Por necesidad de generar ingresos'),
            ('51', 'Oportunidad de negocio en el mercado'),
            ('52', 'Por tradición familiar o herencia'),
            ('53', 'Complementar el ingreso familiar o mejorar el ingreso'),
            ('54', 'Para ejercer su oficio, carrera o profesión'),
            ('55', 'Pocas oportunidades de empleo'),
            ('56', 'Otro (administrar horario, gusto, desplazamiento, búsqueda de independencia)'),

        ], "37. ¿Cuál fue el motivo principal para la creación del negocio?",
    )

    x_motivo_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Por necesidad de generar ingresos'),
            ('51', 'Oportunidad de negocio en el mercado'),
            ('52', 'Por tradición familiar o herencia '),
            ('53', 'Complementar el ingreso familiar o mejorar el ingreso'),
            ('54', 'Para ejercer su oficio, carrera o profesión'),
            ('55', 'Pocas oportunidades de empleo'),
            ('56', 'Para generar oportunidad de empleo'),
            ('57', 'Otro (administrar horario, gusto, desplazamiento, búsqueda de independencia)'),

        ], "38. ¿Cuál fue el motivo principal para la creación del negocio?",
    )

    x_motivo_cual_inf = fields.Char('38. ¿Cual?')

    x_motivo_cual_form = fields.Char('39. ¿Cual?')

    x_recursos_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Ahorros personales'),
            ('51', 'Prestamos familiares '),
            ('52', 'Prestamos bancarios'),
            ('53', 'Prestamistas '),
            ('54', 'Capital semilla'),
            ('55', 'Programas del Gobierno'),
            ('56', 'Otras'),

        ], "35. ¿Cuál fue la principal fuente de recursos para la creación o constitución del negocio?",
    )


    x_recursos_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Ahorros personales'),
            ('51', 'Prestamos familiares '),
            ('52', 'Prestamos bancarios'),
            ('53', 'Prestamistas '),
            ('54', 'Capital semilla'),
            ('55', 'Programas del Gobierno'),
            ('56', 'Otras'),

        ], "36. ¿Cuál fue la principal fuente de recursos para la creación o constitución del negocio?",
    )

    x_recursos_cual_inf = fields.Char('36. ¿Cuál?')

    x_recursos_cual_form = fields.Char('37. ¿Cuál?')

    x_sitio_ubi_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'En la vivienda'),
            ('51', 'Local, tienda, taller, fábrica, oficina, consultorio'),
            ('52', 'De puerta a puerta o a domicilio'),
            ('53', 'Ambulante - sitio al descubierto'),
            ('54', 'Vehículo con o sin motor'),
            ('54', 'Obra o construcción'),
            ('54', 'Finca'),
            ('55', 'Otro'),

        ], "39. ¿Cuál es el sitio o ubicación del negocio?",
    )

    x_sitio_ubi_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'En la vivienda'),
            ('51', 'Local, tienda, taller, fábrica, oficina, consultorio'),
            ('52', 'Obra o construcción'),
            ('53', 'Finca'),
            ('54', 'Otro'),

        ], "40. ¿Cuál es el sitio, lugar o ubicación del negocio?",
    )

    x_sitio_ubi_cual_form = fields.Char('41. ¿Cuál?')
    x_sitio_ubi_cual_inf = fields.Char('40. ¿Cuál?')

    x_desc_act_form = fields.Char('42. Describa la actividad comercial de su negocio' )
    x_desc_act_inf = fields.Char('41. Describa la actividad comercial de su negocio' )

    x_desc_act_sec_form = fields.Char('43. ¿Cuál es la actividad secundaria de su negocio? (si la tiene)')
    x_desc_act_sec_inf = fields.Char('42. ¿Cuál es la actividad secundaria de su negocio? (si la tiene)')

    x_merca = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "¿Adquiere mercancía y comercializa con ella?",
    )

    x_ambula_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Móvil'),
            ('51', 'Estacionario'),
            ('52', 'No aplica'),

        ], "43. Si el negocio es ambulante - sitio al descubierto, ¿cuál es su forma de funcionamiento? ",
    )

    x_ambula_2_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Llega muy temprano'),
            ('51', 'Paga vigilancia'),
            ('52', 'Paga una cuota'),
            ('53', 'Le respetan el puesto'),
            ('54', 'Agrupado con otros vendedores'),
            ('55', 'Tiene carné'),
            ('56', 'No aplica'),
            ('57', 'Otro'),

        ], "44. Si el negocio es ambulante - sitio al descubierto, ¿cómo hace para conservar diariamente el mismo sitio de trabajo?",
    )

    x_mprima_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Diariamente'),
            ('51', 'Semanalmente'),
            ('52', 'Quincenalmente'),
            ('53', 'Mensualmente'),

        ], "45. ¿Con qué frecuencia adquiere materia prima o mercancía para su negocio?",
    )

    x_mprima_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Diariamente'),
            ('51', 'Semanalmente'),
            ('52', 'Quincenalmente'),
            ('53', 'Mensualmente'),

        ], "44. ¿Con qué frecuencia adquiere materia prima o mercancía para su negocio?",
    )

    x_merca_tipo = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Ropa y calzado'),
            ('52', 'Artículos para empresas u oficinas'),
            ('53', 'Artículos para uso industrial'),
            ('54', 'Materias primas para fábricas o industrias'),
            ('55', 'Artículos para construcción'),
            ('56', 'Alimentos o bebidas de consumo humano'),
            ('57', 'Artículos para salud humana'),
            ('58', 'Artículos para consumo animal'),
            ('69', 'Artículos veterinarios'),
            ('60', 'Artículos religiosos'),
            ('61', 'Frutas '),
            ('62', 'Artículos para carros'),
            ('63', 'Otros'),

        ], "¿Qué tipo de mercancías?",
    )

    x_fabric = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Sí, nosotros los fabricamos'),
            ('51', 'No, nosotros no los fabricamos'),

        ], "Los productos que comercializa, ¿son fabricados por usted o por sus empleados?",
    )

    x_fabric_si = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Ropa y calzado'),
            ('52', 'Artículos para empresas u oficinas'),
            ('53', 'Artículos para uso industrial'),
            ('54', 'Materias primas para fábricas o industrias'),
            ('55', 'Artículos para construcción'),
            ('56', 'Alimentos o bebidas de consumo humano'),
            ('57', 'Artículos para salud humana'),
            ('58', 'Artículos para consumo animal'),
            ('59', 'Artículos veterinarios'),
            ('60', 'Artículos religiosos'),
            ('61', 'Frutas '),
            ('62', 'Otros'),

        ], "¿Qué tipo de mercancías?",
    )

    x_servicios = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Artículos de uso doméstico'),
            ('51', 'Culturales o creativos'),
            ('52', 'Transporte'),
            ('53', 'Almacenamiento'),
            ('54', 'Alojamiento'),
            ('55', 'Turismo'),
            ('56', 'Inmobiliario o finca raíz'),
            ('57', 'Actividades Financieras'),
            ('58', 'Servicios administrativos o de apoyo'),
            ('59', 'Actividades Profesionales'),
            ('60', 'Actividades Técnicas'),
            ('61', 'Suministro de servicios para hogares'),
            ('62', 'Suministro de servicios empresariales'),
            ('63', 'Suministro de servicios para fábrica o industria'),
            ('64', 'Otros'),

        ], "Si presta servicios o realiza consultorías, ¿De qué tipo son?",
    )

    x_clientes_form = fields.Integer(
        string="45. ¿Cuántos clientes atiende diariamente?",
        help="Ingrese un número entre 1 y 100",
    )

    x_clientes_inf = fields.Integer(
        string="46. ¿Cuántos clientes atiende diariamente?",
        help="Ingrese un número entre 1 y 100",
    )

    x_problema_inf = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Dificultad en obtener créditos'),
            ('51', 'Competencia excesiva'),
            ('52', 'Problemas de comercialización de productos'),
            ('53', 'Problemas con las autoridades'),
            ('54', 'No cuenta con las condiciones de bioseguridad que se requieren'),
            ('55', 'Aumento en el precio de los insumos'),
            ('56', 'Desconfianza de los clientes para adquirir productos de consumo'),
            ('57', 'Dificultad en la producción del producto'),
            ('58', 'No se encuentra virtualizado'),
            ('59', 'Falta de capacitación'),
            ('60', 'Falta de tecnología y conexión'),
            ('61', 'Normatividad, acreditación o certificación de su producto o servicio'),
            ('62', 'Otro'),

        ], "47. Seleccione el principal problema que usted tiene actualmente con su negocio?",
    )

    x_problema_form = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Dificultad en obtener creditos'),
            ('51', 'Competencia excesiva'),
            ('52', 'Problemas de comercialización de productos'),
            ('53', 'Problemas con las autoridades'),
            ('54', 'No cuenta con las condiciones de bioseguridad que se requieren'),
            ('55', 'Aumento en el precio de los insumos'),
            ('56', 'Desconfianza de los clientes para adquirir productos de consumo'),
            ('57', 'Dificultad en la producción del producto'),
            ('58', 'No se encuentra virtualizado'),
            ('59', 'Falta de capacitación'),
            ('60', 'Falta de tecnología y conexión'),
            ('61', 'Normatividad, acreditación o certificación de su producto o servicio'),
            ('62', 'Otro'),

        ], "46. Seleccione el principal problema que usted tiene actualmente con su negocio",
    )

    x_prob_desc_form = fields.Char(
        string="47. Una vez seleccionado el principal problema del micronegocio, descríbalo en una frase",
    )

    x_prob_desc_inf = fields.Char(
        string="48. Una vez seleccionado el principal problema del micronegocio, descríbalo en una frase",
    )

    x_reinvierte_inf = fields.Integer(
        string="49. ¿Qúé porcentaje de las ventas reinvierte nuevamente en mercancía (1-100)?",
        help="Ingrese un número entre 1 y 100",
    )

    x_reinvierte_form = fields.Integer(
        string="48. ¿Qúé porcentaje de las ventas reinvierte nuevamente en mercancía (1-100)?",
        help="Ingrese un número entre 1 y 100",
    )

    #MÓDULO 3-PROTOCOLOS DE BIOSEGURIDAD
    x_dcont1 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_proto1 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "1. ¿Usted conoce los protocolos de bioseguridad para su negocio??",
    )

    x_proto2 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "2. ¿En su negocio implementa los protocolos de bioseguridad?",
    )

    x_proto3 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "3. ¿Dispone de puntos de alcohol con una concentracion no inferior al 70% para la higiene de las manos de los clientes y los trabajadores del negocio?",
    )

    x_proto4 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "4. Dispone de la adecuada provision de tapabocas y elementos de proteccion para quienes laboran en el negocio?",
    )

    x_proto5 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "5. ¿Se realiza cambio de tapabocas durante la jornada laboral?",
    )

    x_proto6 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),
            ('52', 'No Aplica'),

        ], "6. ¿Atiende a un cliente a la vez y mantiene el distanciamiento social?",
    )

    x_proto7 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),
            ('52', 'No Aplica'),

        ], "7. ¿Atiende de manera prioritaria a la poblacion con riesgo del COVID19, para disminuir el tiempo que permenecen en el lugar?",
    )

    x_proto8 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),
            ('52', 'No Aplica'),

        ], "8. ¿Realiza la proteccion permanente de los alimentos en exhibicion, con el uso de peliculas plasticas, tapas, vitrinas, etc?",
    )

    x_proto9 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "9. ¿Dispone de superficies faciles de limpiar y desinfectar para ubicar los productos?",
    )

    x_proto10 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "10. ¿Desinfecta los objetos del local cuando son prestados a los clientes o proveedores (esferos, grapadora, etc.), antes y después de su uso?",
    )

    x_proto11 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "11. ¿Coloca avisos o alertas para mantener las medidas de prevencion?",
    )

    x_proto12 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),
            ('52', 'No Aplica'),

        ], "12. ¿Realiza la entrega de productos o alimentos para llevar o consumir fuera del local?",
    )

    x_proto13 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "13. ¿Limpia y desinfecta las herramientas de trabajo una vez finalice la jornada?",
    )

    x_proto14 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "14. ¿Asegura que los colaboradores y los clientes usen tapabocas?",
    )

    x_proto15 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "15. Realiza la limpieza del espacio de trabajo al menos dos vez al dia?",
    )

    x_proto16 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "16. ¿Entrega los productos sobre una superficie, sin tener contacto con el cliente?",
    )

    x_proto17 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Si'),
            ('51', 'No'),

        ], "17. ¿Ha recibido o recibe algun apoyo o beneficio economico por parte del Gobierno en la emergencia para usted?",
    )

    x_proto18 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Subsidios'),
            ('51', 'Mercados'),
            ('52', 'Bonos'),
            ('53', 'Implementos de bioseguridad'),

        ], "18. ¿Que tipo de beneficios?",
    )

    #INNOVACION DEL MODELO DE NEGOCIO
    x_dcont2 = fields.Boolean(
        string="¿Desea continuar con el Formulario?",
    )

    x_innova19 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "19. ¿Ha recibido o recibe algun apoyo o beneficio economico por parte del Gobierno en la emergencia para usted?",
    )

    x_innova20 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "20. ¿Se ha capacitado en la formacion de modelos de negocio?",
    )

    x_innova21 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "21. ¿Conoce los canales de distribucion para su producto?",
    )

    x_innova22 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Canal directo: Productor-Consumidor'),
            ('51', 'Canal Detallista: Productor-Minorista-Consumidor'),
            ('52', 'Canal Distribuidor:  Productor-Distribuidor-Minorista-Consumidor'),
            ('53', 'Canal Broker: Productor-Mayorista-Distribuidor-Minorista-Consumidor'),

        ], "22. ¿Que tipo de beneficios?",
    )

    x_innova23 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Totalmente de acuerdo'),
            ('51', 'De acuerdo'),
            ('52', 'Ni de acuerdo, ni en desacuerdo'),
            ('53', 'En desacuerdo'),
            ('54', 'Totalmente en desacuerdo'),

        ], "23. ¿Considera que para la produccion o manipulacion del producto debe contar con personal capacitado?",
    )

    x_innova24 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "24. ¿Cuenta con personal capacitado para la produccion o manipulacion del producto?",
    )

    x_innova25 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "25. ¿Cuenta con un espacio adecuado para la produccion y almacenamiento del producto, teniendo en cuenta medidas de higiene y de seguridad?",
    )

    x_innova26 = fields.Selection(
        #string="Sexo",
        [
            ('50', 'Totalmente de acuerdo'),
            ('51', 'De acuerdo'),
            ('52', 'Ni de acuerdo, ni en desacuerdo'),
            ('53', 'En desacuerdo'),
            ('54', 'Totalmente en desacuerdo'),

        ], "26. ¿Usted considera importante que el uso de buenas practicas  manipulacion y produccion de la materia prima debe estar sujeta a estandares de calidad certificada  ¿Esto garantizara o generara confianza a los clientes para aumentar la demanda de consumo o uso de los productos  o servicios que ofrece?",
    )

    x_innova27 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "27. ¿Para la obtencion de la materia prima o mercancia depende de un solo proveedor? ",
    )

    x_innova28 = fields.Selection(
        #string="Sexo",
        [('50', 'De contado'),
         ('51', 'A credito'),
         ('52', 'A plazos'),

        ], "28. El pago de la materia prima la realiza ",
    )

    x_innova29 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "29. ¿Ha representado retrasos en la entrega de su producto por falta de materia prima o mercancia?",
    )

    x_innova30 = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "30. ¿Considera que la estandarizacion de procesos para la produccion o manipulacion del producto permiten agilizar los tiempos de entrega?",
    )

    x_innova31 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "31. ¿Cuenta con un proceso estandarizado para la produccion o manipulacion del producto?",
    )

    x_innova32 = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "32. ¿Considera que en el inventario se llevan los registros de las entradas y salidas del producto?",
    )

    x_innova33 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "33. ¿Cuenta con un inventario donde registre las entradas y salidas del producto?",
    )

    x_innova34 = fields.Integer(
        string="34. ¿Cuantas lineas de producto tiene su negocio?",
    )

    x_innova35 = fields.Char(
        string="35. Describa las lineas de producto que tiene su negocio",
    )

    x_innova36 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "36. ¿Sabe lo que le cuesta a su negocio la produccion y comercializacion del producto o servicio?",
    )

    x_innova37 = fields.Selection(
        #string="Sexo",
        [('50', 'Por el mercado'),
         ('51', 'Por el punto de equilibrio'),
         ('52', 'Costos fijos + variables + costos de utilidad'),

        ], "37. ¿Sabe lo que le cuesta a su negocio la produccion y comercializacion del producto o servicio?",
    )

    x_innova38 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "38. ¿Conoce que es el punto de equilibrio?",
    )

    x_innova39 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "39. ¿Sabe cual es el punto de equilibrio de su negocio?",
    )

    x_innova40 = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "40. ¿En el ultimo año ha realizado actividades de innovacion para su negocio?",
    )

    x_innova41_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "41. ¿Realiza actividades con los trabajadores para crear innovaciones en su negocio?",
    )

    x_innova41_form = fields.Selection(
        #string="Sexo",
        [('50', 'Totalmente de acuerdo'),
         ('51', 'De acuerdo'),
         ('52', 'Ni de acuerdo, ni en desacuerdo'),
         ('53', 'En desacuerdo'),
         ('54', 'Totalmente en desacuerdo'),

        ], "41. ¿Cree que capacitar a sus trabajadores puede aumentar los resultados de su negocio?",
    )

    x_innova42_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "42. ¿Ha recibido formacion en creatividad e innovacion? ",
    )

    x_innova42_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "42. ¿Realiza actividades con los trabajadores para crear innovaciones en su negocio?",
    )

    x_innova43_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "43. ¿Ofrece con frecuencia productos o servicios nuevos a partir de sugerencias de sus clientes?",
    )

    x_innova43_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "43. ¿Ha recibido formacion en creatividad e innovacion? ",
    )

    x_innova44_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "44. ¿Desarrolla o paga para innovar la forma en la que vende sus producto o servicios? (Diseño, envase, promocion, forma de cotizar, etc.)",
    )

    x_innova44_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "44. ¿Ofrece con frecuencia productos o servicios nuevos a partir de sugerencias de sus clientes?",
    )

    x_innova45_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "45. ¿Desarrolla o paga para innovar la forma en la que vende sus producto o servicios? (Diseño, envase, promocion, forma de cotizar, etc.)",
    )
    #gavii

    
#FORMALIZACION SECCION 3: ADMINISTRACION
    x_dcont3 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_forma45_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "45. ¿Considera que al realizar un analisis interno y externo de su negocio, permitira la identificacion de debilidades, oportunidades,fortalezas y amenazas?",
    )

    x_forma46_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "46. ¿Considera que al realizar un analisis interno y externo de su negocio, permitira la identificacion de debilidades, oportunidades,fortalezas y amenazas?",
    )

    x_forma46_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "46. ¿Sabe como realizar un analisis interno de su negocio?",
    )

    x_forma47_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "47. ¿Sabe como realizar un analisis interno de su negocio?",
    )

    x_forma47_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "47. ¿Sabe como realizar un analisis externo de su negocio?",
    )

    x_forma48_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "48. ¿Sabe como realizar un analisis externo de su negocio?",
    )

    x_forma48_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "48. ¿Ha pensado en formalizar su negocio?",
    )

    x_forma49_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "49. ¿Tiene claro la proyección de su negocio a corto, mediano y largo plazo?",
    )

    x_forma49_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "49. ¿Para usted es importante la formalizacion de su negocio?",
    )

    x_forma50_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "50. ¿Toma medidas para desarrollar una cultura de la organización?",
    )

    x_forma50_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "50. ¿Tiene su negocio un registro mercantil?",
    )

    x_forma51_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "51. ¿Conoce las normas y estándares de calidad para productos y servicios?",
    )

    x_forma51_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "51. ¿se encuentra actualizado?",
    )

    x_forma52_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "52. ¿Cuenta con alguna norma o estandar que certifique la calidad del producto o servicio que usted ofrece?",
    )

    x_forma52_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "52. ¿Tiene este negocio RUT(Registro Único Tributario)?",
    )

    x_forma53_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "53. ¿Expedir factura permite que los clientes tengan mayor confianza y seguridad al momento de comprar sus productos o servicios?",
    )

    x_forma53_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "53. ¿se encuentra actualizado?",
    )

    x_forma54_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "54. ¿Expide factura?",
    )

    x_forma54_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "54. ¿Tiene este negocio NIT(Número de identificacion Tributaria?",
    )

    x_forma55_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "55. ¿Expide facturación electrónica?",
    )

    x_forma55_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "55. ¿Se encuentra actualizado?",
    )

    x_forma56_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "56. ¿Considera que se debe tener claridad de los impuestos presentados por su actividad económica y las frecuencias en que debe pagar?",
    )

    x_forma56_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "56. Para el funcionamiento del negocio: ¿Requiere algun permiso municipal/distrital adicional para funcionar?",
    )

    x_forma57_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "57. ¿Ha tenido que reducir la cantidad de sus trabajadores por consecuencias de la pandemia?",
    )

    x_forma57_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "57. ¿Cuenta actualmente con el permiso municipal/distrital adicional para funcionar?",
    )

    x_forma58_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "58. Antes de la pandemia COVID-19 ¿Cuantas personas de su familia trabajaban con usted en el negocio?",
    )

    x_forma58_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "58. ¿Expedir factura permite que los clientes tengan mayor confianza y seguridad al momento de comprar sus productos o servicios?",
    )

    x_forma59_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "59. Antes de la pandemia COVID-19 ¿Cuantas personas QUE NO SON de su familia trabajaban con usted en el negocio?",
    )

    x_forma59_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "59. ¿Expide factura?",
    )

    x_forma60_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "60. ¿Cuantas personas de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma60_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "60. ¿Considera que se debe tener claridad de los impuestos presentados por su actividad económica y las frecuencias en que debe pagar?",
    )

    x_forma61_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "61. ¿Cuantas personas QUE NO SON de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma61_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "61. ¿Ha tenido que reducir la cantidad de sus trabajadores por consecuencias de la pandemia?",
    )

    x_forma62_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "62. ¿Que tipo de contrato aplica más para los trabajadores de su negocio?",
    )

    x_forma62_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "62. Antes de la pandemia COVID-19 ¿Cuantas personas de su familia trabajaban con usted en el negocio?",
    )

    x_forma63_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "63. ¿Si tiene trabajadores como es el sistema de remuneración?  ",
    )

    x_forma63_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "63. Antes de la pandemia COVID-19 ¿Cuantas personas QUE NO SON de su familia trabajaban con usted en el negocio?",
    )

    x_forma64_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "64. ¿Considera importante para su negocio conocer y aplicar las obligaciones correspondientes para los trabajadores que laboran en su negocio? ",
    )

    x_forma64_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "64. ¿Cuantas personas de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma65_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "65. ¿Cuantas personas QUE NO SON de su familia trabajan actualmente con usted en el negocio?",
    )

    x_forma66_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "66. ¿Si tiene trabajadores como es el sistema de remuneracion?  ",
    )

    x_forma67_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "67. ¿Considera importante para su negocio conocer y aplicar las obligaciones correspondientes para los trabajadores que laboran en su negocio?",
    )

    x_dcont4 = fields.Boolean(
        string="Continuar con el Formulario",
    )

    x_merc65_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "65. ¿Utiliza alguna estrategia para comercializar sus productos?",
    )

    x_merc68_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "68. ¿Utiliza alguna estrategia para comercializar sus productos?",
    )

    

    x_merc66_form = fields.Char(
        string="66. ¿Cuál es la estrategia que utiliza para comercializar sus productos o servicios?",
        help="Escriba su estrategia", 
    )

    

    x_merc69_inf = fields.Char(
        string="69. ¿Cuál es la estrategia que utiliza para comercializar sus productos o servicios?",
        help="Escriba su estrategia", 
    )

    x_merc67_form = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "67. ¿Utiliza alguna estrategia para la visibilizacion de sus productos?",
    )

    x_merc70_inf = fields.Selection(
        #string="Sexo",
        [('50', 'Si'),
         ('51', 'No'),

        ], "70. ¿Utiliza alguna estrategia para la visibilizacion de sus productos?",
    )

    x_merc68_form = fields.Char(
        string="68. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios?",
        help="Escriba su respuesta", 
    )

    

    x_merc71_inf = fields.Char(
        string="71. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios?",
        help="Escriba su respuesta", 
    )

    x_merc69_form = fields.Selection(
        #string="Sexo",
        [('1', 'Teléfono celular no Smart'),
         ('2', 'Smartphone'),
         ('3', 'Computador de escritorio'),
         ('4', 'Computador portátil'),
         ('5', 'Tablet'),
         ('6', 'Todas las anteriores'),
         ('7', 'Todas las anteriores'),

        ], "69. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios? ",
    )

    x_merc72_inf = fields.Selection(
        #string="Sexo",
        [('1', 'Teléfono celular no Smart'),
         ('2', 'Smartphone'),
         ('3', 'Computador de escritorio'),
         ('4', 'Computador portátil'),
         ('5', 'Tablet'),
         ('6', 'Todas las anteriores'),
         ('7', 'Todas las anteriores'),

        ], "72. ¿Cuál es la estrategia que utiliza para la visibilización de sus productos o servicios? ",
    )




   

    country_id = fields.Many2one('res.country', "Country")
    xcity = fields.Many2one('res.country.state.city', "9. Municipio de Residencia")
    city = fields.Char(related="xcity.name")


    x_state_id = fields.Many2one('res.country.state', '21. Departamento donde se ubica su negocio')
    x_city_id = fields.Many2one('res.country.state.city', '22. Municipio donde se ubica su negocio')

    @api.onchange('country_id', 'state_id')
    def onchange_location(self):
        """
        This functions is a great helper when you enter the customer's
        location. It solves the problem of various cities with the same name in
        a country
        @param country_id: Country Id (ISO)
        @param state_id: State Id (ISO)
        @return: object
        """

        if self.state_id:
            mymodel = 'res.country.state.city'
            filter_column = 'state_id'
            check_value = self.state_id.id
            domain = 'xcity'
        else:
            return {}

        obj = self.env[mymodel]
        ids = obj.search([(filter_column, '=', check_value)])
        id_domain = []
        for id in ids:
            id_domain.append(id.id)
        
        return {
            'domain': {domain: [('id', 'in', id_domain)]},
            'value': {domain: ''}
        }

