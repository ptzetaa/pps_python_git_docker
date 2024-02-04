# La Bayeta Mágica

La Bayeta Mágica es una aplicación web simple que brinda frases de buen augurio de manera aleatoria cada vez que se accede al sitio.

# Características Destacadas

    Desarrollo de una interfaz web fácil de usar.
    Acceso a la fortuna al visitar la ruta principal (/).
    Recopilación de frases auspiciosas en formato JSON mediante la ruta /frotar/<n_frases>.
    Almacenamiento de las frases positivas en una base de datos MongoDB.
    Implementación del despliegue de la aplicación en un contenedor Docker mediante docker-compose.

## Guía de Uso con Docker

Sigue estos pasos para ejecutar la aplicación en un contenedor Docker:

### 1. Clonar el Repositorio

    git clone https://github.com/ptzetaa/pps_python_git_docker.git
    cd pps_python_git_docker

### 2. Iniciar el Contenedor

    docker-compose up -d

   La aplicación estará disponible en http://localhost:5000/

### 3. Detener el Contenedor

    docker-compose down

## Instrucciones de Uso

La aplicación ofrece dos rutas principales:

    /: Muestra una frase positiva al azar.
    /frotar/<n_frases>: Devuelve n_frases frases positivas en formato JSON.

Para agregar frases a la base de datos:

    Puedes añadir frases desde /frotar/add/<frase> utilizando tu cliente REST favorito.

### Ejemplo de Uso



    curl http://localhost:5000/
    curl http://localhost:5000/frotar/3
    curl -X POST -H "Content-Type: application/json" -d '{"frases": ["Nueva frase 1", "Nueva frase 2"]}' http://localhost:5000/frotar/add

## Requisitos

    Es necesario tener instalados Docker y Docker-compose en el sistema. Si no los tienes, sigue las instrucciones en la documentación oficial de Docker.

## Licencia

Este proyecto está bajo la Licencia GPL-3.0 - consulta el archivo LICENSE para obtener más detalles.