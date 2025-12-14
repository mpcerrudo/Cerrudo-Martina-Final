# Cerrudo-Martina-Final
Organizador es una aplicación de línea de comandos desarrollada en Python que permite gestionar tareas de forma simple y eficiente. El programa posibilita crear, listar, marcar como completadas y eliminar tareas, almacenando la información de manera persistente en una base de datos SQLite.

El objetivo principal del proyecto es demostrar la aplicación práctica de los conceptos fundamentales de programación en Python, haciendo énfasis en la modularización, el uso de buenas prácticas, la documentación del código y la utilización de herramientas profesionales.

Funcionalidades principales:
-Inicializar una base de datos local.
-Agregar nuevas tareas con título, descripción, prioridad y fecha de vencimiento.
-Listar tareas existentes en formato de tabla.
-Marcar tareas como completadas.
-Eliminar tareas.

Requisitos del sistema:
-Python versión 3.9 o superior.
-Sistema operativo: Windows, Linux o macOS.
-Acceso a una terminal o consola de comandos.

Instalación y ejecución local
1. Clonar o descargar el proyecto
   git clone <url-del-repositorio>                                                            
   cd Organizador 

2. Crear un entorno virtual (venv)
El uso de un entorno virtual permite aislar las dependencias del proyecto y evitar conflictos con otras instalaciones de Python.
 python -m venv venv
 venv\Scripts\activate
 
3. Instalación de dependencias
Con el entorno virtual activado, instalar las dependencias necesarias:
 pip install -r requirements.txt
Las dependencias principales son:
-click: creación de interfaces de línea de comandos.
-tabulate: presentación de datos en formato de tabla.
-pytest: ejecución de pruebas automáticas.

Uso del programa
Inicializar la base de datos
 python -m src.Organizador.cli init-db
Agregar una tarea
 python -m src.Organizador.cli add "Estudiar Python" -d "Repasar estructuras" -p 2 -D 2025-12-15
Listar tareas
  python -m src.Organizador.cli list
Marcar una tarea como completada
 python -m src.Organizador.cli done 1
Eliminar una tarea
 python -m src.Organizador.cli delete 1

Ejecución de pruebas
El proyecto incluye pruebas automáticas para validar el correcto funcionamiento de las principales funcionalidades.
 pytest
Estas pruebas verifican la creación, actualización y eliminación de tareas, así como el correcto manejo de la base de datos.

Estructura del proyecto
task_manager/
├─ src/
│ └─ task_manager/
│ ├─ cli.py # Interfaz de línea de comandos
│ ├─ tasks.py # Modelo de datos (Task)
│ ├─ storage.py # Persistencia en SQLite
│ └─ utils.py # Funciones auxiliares
├─ tests/ # Pruebas automáticas
├─ docs/ # Documentación adicional
├─ requirements.txt # Dependencias
└─ README.md # Documentación principal

Buenas prácticas aplicadas
-Código modularizado y organizado por responsabilidades.
-Uso de docstrings siguiendo la PEP 257.
-Estilo de código conforme a la PEP 8.
-Aplicación del principio del Zen de Python: "Simple is better than complex".
-Uso de entorno virtual para facilitar la reproducibilidad y el trabajo colaborativo.

Organizador es un proyecto educativo que integra los principales conceptos de la programación en Python en una aplicación funcional y clara. Su diseño simple y modular permite comprender fácilmente su funcionamiento y sirve como base para proyectos de mayor complejidad en el futuro.
