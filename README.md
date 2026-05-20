# Proyecto Radios

Sistema web para la gestión de órdenes de trabajo (OT) de radios. Permite registrar, visualizar y hacer seguimiento de actividades de programación, mantenimiento y baja de equipos de radio.

## Demo en vivo

**[Ver demo → proyectoradios-275888564441.us-central1.run.app](https://proyectoradios-275888564441.us-central1.run.app/)**

> Desplegado en Google Cloud Run — proyecto `tylerrv25@gmail.com`

## Tecnologías

- **Backend:** Python, Flask
- **Base de datos:** MySQL (via PyMySQL)
- **Frontend:** HTML, Bootstrap 5
- **Autenticación:** Flask-Bcrypt
- **Variables de entorno:** python-dotenv

## Funcionalidades

- Registro de órdenes de trabajo con datos como:
  - Número de OT y fecha de recepción
  - Personal receptor y programador
  - Tipo de servicio: Programación, Mantenimiento, Dar de baja, Agregar Frecuencia
  - Modelo y cantidad de radios
  - Fecha de entrega
- Tabla de OT's pendientes con acciones de ver, editar y eliminar
- Exportación a Excel *(en desarrollo)*

## Requisitos

- Python 3.10+
- MySQL
- Pipenv

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Tyler0125/proyectoradios.git
cd proyectoradios

# 2. Instalar dependencias
pipenv install

# 3. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de base de datos

# 4. Ejecutar la aplicación
pipenv run python server.py
```

La aplicación estará disponible en `http://localhost:5000`

## Estructura del proyecto

```
proyectoradios/
├── flask_app/
│   ├── config/
│   │   └── mysqlconnection.py   # Conexión reutilizable a MySQL
│   ├── controllers/
│   │   └── root_controller.py   # Rutas de la aplicación
│   ├── models/
│   │   └── default_model.py     # Modelos de datos
│   └── templates/
│       └── root/
│           └── index.html       # Vista principal
├── server.py                    # Punto de entrada
├── Pipfile                      # Dependencias
└── .env.example                 # Plantilla de variables de entorno
```

## Variables de entorno

Copia `.env.example` a `.env` y completa con tus datos:

```
APP_SECRET_KEY=tu-clave-secreta
DB_NAME=nombre_base_de_datos
DB_HOSTNAME=localhost
DB_USERNAME=root
DB_PASSWORD=tu_contraseña
```

## Autor

**Tyler Rojas** — [GitHub](https://github.com/Tyler0125)
