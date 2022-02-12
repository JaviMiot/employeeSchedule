
<div  align="center">
	<h1  style="text-align: center">Command Line Employees Schedule</h1>
</div>

<div align="center" >
	<img width="500" src=""/>
</div>

_Acerca del proyecto_
Linea de comandos para obtener una lista de empleados que coinciden con el mismo horario en la oficina.

## Solución🚀
Para la solución se considero usar una linea de comandos donde el usuario pueda ingresar el nombre del archivo .txt y  el formato de salida de los datos. Esta última opción se consideró implementarla debido a que se puede agregar funcionalidades como exportar los datos a un pdf, excel o cualquier tipo de formato.

Se empezó por definir las pruebas unitarias deacuerdo a los datos de prueba que tenia el ejercicio.


## Caracteristicas📋
1. Ejecución por linea de comandos
2. Salida en formato String, diccionario y pipe.
3. Descripción de los comandos para ejecutar.

## Estructura de las carpetas📁
- `setup.py`: La configuración del paquete para ser instalado y ejecutado.
- `employees`: punto de entrada de la aplicación.
- `test`: Carpeta que contiene las pruebas unitarias.
- `schedule`: Carpeta que contiene toda la lógica del programa.
  - `models`: Contiene las clases para crear los objetos de los empleados y de los horarios.
  - `utils`: Contiene pedazos de código a manera de librerías propias.
  - `transformData`: Contiene la lógica para convertir la salida en varios formatos.
  - `services.py`: Contiene los servicios para lectura del .txt y generar la lista de coincidencia de los empleados.
  - `command.py`: Contiene la lógica y agrupación de los comandos que serán ejecutados, esta consume los servicios de `services.py`.

### Pre-requisites 📋

1. Python 3.6.9 o superior
2. Pipe

## Instalación🚀

Clonar el repositorio
```shell
git clone https://github.com/JaviMiot/employeeSchedule.git
```
Ingresar a la carpeta del proyecto
```shell
cd employeeSchedule/
```

Crear un ambiente virtual
```shell
python3 -m venv .env
```

Correr el ambiente virtual ejecutando el script dentro de la carpeta `./.env/bin/activate` si esta en linux. Si esta en windows será la carpeta `./.env/Scripts/activate.ps1`

Con el ambiente virtual de python corriendo ejecutar el comando.
```shell
pip install -e .
```

### Utilización 🔧

Con el paquete instalado se tiene los siguientes comandos.
- `employees schedule coincided [options]`: este comando permitira tener la lista de empleados que coincidieron en la oficina.

__Options:__
  - -f, --file TEXT : el nombre del archivo .txt
  - -ft, --format TEXT : Formato de salida, puede ser un diccionario = dict, pipe = pipe, o un string, si no envia esta opción por defecto es un string.

Para obtener ayuda usa el comando `--help`
```shell
employees schedule coincided --help
Usage: employees schedule coincided [OPTIONS]

Options:
  -f, --file TEXT     The file .txt with employees schedule
  -ft, --format TEXT  Output format, Can use dict = dictionary, pipe =
                      pipe. Default is string
  --help              Show this message and exit.
```

__Ejemplos__

```shell
employees schedule coincided -f fakerDataAll.txt -ft pipe

>>output
RENE-ASTRID: 2 |RENE-ANDRES: 2 |RENE-CARLOS: 5 |RENE-JORGE: 2 |RENE-JOSUE: 2 |ASTRID-ANDRES: 3 |ASTRID-CARLOS: 2 |ASTRID-JORGE: 3 |ASTRID-JOSUE: 3 |ANDRES-CARLOS: 2 |ANDRES-JORGE: 3 |ANDRES-JOSUE: 3 |CARLOS-JORGE: 2 |CARLOS-JOSUE: 2 |JORGE-JOSUE: 3 |
```

```shell
employees schedule coincided -f fakerDataAll.txt -ft dict

>>output
{'RENE-ASTRID': 2, 'RENE-ANDRES': 2, 'RENE-CARLOS': 5, 'RENE-JORGE': 2, 'RENE-JOSUE': 2, 'ASTRID-ANDRES': 3, 'ASTRID-CARLOS': 2, 'ASTRID-JORGE': 3, 'ASTRID-JOSUE': 3, 'ANDRES-CARLOS': 2, 'ANDRES-JORGE': 3, 'ANDRES-JOSUE': 3, 'CARLOS-JORGE': 2, 'CARLOS-JOSUE': 2, 'JORGE-JOSUE': 3}
```

```shell
employees schedule coincided -f fakerDataAll.txt

>>output
RENE-ASTRID: 2
RENE-ANDRES: 2
RENE-CARLOS: 5
RENE-JORGE: 2
RENE-JOSUE: 2
ASTRID-ANDRES: 3
ASTRID-CARLOS: 2
ASTRID-JORGE: 3
ASTRID-JOSUE: 3
ANDRES-CARLOS: 2
ANDRES-JORGE: 3
ANDRES-JOSUE: 3
CARLOS-JORGE: 2
CARLOS-JOSUE: 2
JORGE-JOSUE: 3
```

## Ejecutar pruebas unitarias ⚙️

Las pruebas unitarias se encuentrar en la carpeta `test`, el comando para correr las pruebas es el siguiente:
```shell
python -m unittest discover -v
```


## Contruido con 🛠️


* [Python](https://www.python.org/) - Lenguaje de programación
* [Click](https://click.palletsprojects.com/en/8.0.x/) - Interfaz de linea de comandos.


## Autor ✒️

* **Javier Manobanda** - *Trabajo Inicial* - [Github](https://github.com/JaviMiot)


## License 📄
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
⌨️ with❤️ by [Javier Manobanda](https://github.com/JaviMiot)😊
