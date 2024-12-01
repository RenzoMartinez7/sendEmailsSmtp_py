# Librerías
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'tucorreo@gmail.com'
SMTP_PASSWORD = 'tuContraseñaSMTP'

# Lista de inscritos
inscritos = [
    {'nombre': 'nombre', 'correo': 'xxxxxx@gmail.com'},
    {'nombre': 'nombre', 'correo': 'xxxxxx@gmail.com'}
    # Agregar más ...
]

# Función para el envío de correos
def enviar_correo(inscrito):
    # Creando el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = SMTP_USER
    mensaje['To'] = inscrito['correo']
    mensaje['Subject'] = 'Asunto'

    # Contenido del correo
    contenido = f"""
    Estimado/a {inscrito['nombre']},

    Mensaje......................................
    
    """
    mensaje.attach(MIMEText(contenido, 'plain'))

    # Envío del correo
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(SMTP_USER, SMTP_PASSWORD)
            servidor.sendmail(SMTP_USER, inscrito['correo'], mensaje.as_string())
        print(f"Correo enviado a {inscrito['nombre']} ({inscrito['correo']})")
    except Exception as e:
        print(f"Error al enviar a {inscrito['correo']}: {e}")

# Enviar los correos a todos los destinatarios (inscritos)
for inscrito in inscritos:
    enviar_correo(inscrito)
