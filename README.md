# Proyecto 6: Computer Vision

Descripción

El proyecto consiste en un sistema de inicio de sesión facial desarrollado con Python y OpenCV. El software utiliza la cámara web para detectar rostros en tiempo real y permitir o denegar el acceso según la presencia de un rostro frente a la cámara. Su objetivo es demostrar el uso de técnicas de visión por computadora aplicadas a sistemas básicos de autenticación biométrica.

Uso
El sistema abrirá automáticamente la cámara web.
Si detecta un rostro, mostrará: ACCESO AUTORIZADO
Si no detecta ningún rostro, mostrará: ACCESO DENEGADO
Para cerrar el programa, presionar la tecla: Q

Requisitos;

Crear entorno virtual
Abrir PowerShell dentro de la carpeta del proyecto y ejecutar:

python -m venv venv

Activar entorno virtual
En Windows PowerShell:

.\venv\Scripts\activate

Instalar dependencias
Con el entorno virtual activado ejecutar:

pip install opencv-python
pip install opencv-contrib-python

Ejecutar el sistema
Ejecutar el archivo principal:

python login_facial.py

Tecnologías utilizadas
Python
OpenCV
Visión por computadora
Detección facial Haar Cascade
