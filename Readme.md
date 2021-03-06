
<div  align="center">
	<h1  style="text-align: center">Command Line Employees Schedule</h1>
</div>

<div align="center" >
	<img width="500" src=""/>
</div>

_Acerca del proyecto_
Linea de comandos para obtener una lista de empleados que coinciden con el mismo horario en la oficina.

## Soluci贸n馃殌
Para la soluci贸n se considero usar una linea de comandos donde el usuario pueda ingresar el nombre del archivo .txt y  el formato de salida de los datos. Esta 煤ltima opci贸n se consider贸 implementarla debido a que se puede agregar funcionalidades como exportar los datos a un pdf, excel o cualquier tipo de formato.

Se empez贸 por definir las pruebas unitarias deacuerdo a los datos de prueba que tenia el ejercicio.


## Caracteristicas馃搵
1. Ejecuci贸n por linea de comandos
2. Salida en formato String, diccionario y pipe.
3. Descripci贸n de los comandos para ejecutar.

## Estructura de las carpetas馃搧
- `setup.py`: La configuraci贸n del paquete para ser instalado y ejecutado.
- `employees`: punto de entrada de la aplicaci贸n.
- `test`: Carpeta que contiene las pruebas unitarias.
- `schedule`: Carpeta que contiene toda la l贸gica del programa.
  - `models`: Contiene las clases para crear los objetos de los empleados y de los horarios.
  - `utils`: Contiene pedazos de c贸digo a manera de librer铆as propias.
  - `transformData`: Contiene la l贸gica para convertir la salida en varios formatos.
  - `services.py`: Contiene los servicios para lectura del .txt y generar la lista de coincidencia de los empleados.
  - `command.py`: Contiene la l贸gica y agrupaci贸n de los comandos que ser谩n ejecutados, esta consume los servicios de `services.py`.

### Pre-requisites 馃搵

1. Python 3.6.9 o superior
2. Pipe

## Instalaci贸n馃殌

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

Correr el ambiente virtual ejecutando el script dentro de la carpeta `./.env/bin/activate` si esta en linux. Si esta en windows ser谩 la carpeta `./.env/Scripts/activate.ps1`

Con el ambiente virtual de python corriendo ejecutar el comando.
```shell
pip install -e .
```

### Utilizaci贸n 馃敡

Con el paquete instalado se tiene los siguientes comandos.
- `employees schedule coincided [options]`: este comando permitira tener la lista de empleados que coincidieron en la oficina.

__Options:__
  - -f, --file TEXT : el nombre del archivo .txt
  - -ft, --format TEXT : Formato de salida, puede ser un diccionario = dict, pipe = pipe, o un string, si no envia esta opci贸n por defecto es un string.

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

## Ejecutar pruebas unitarias 鈿欙笍

Las pruebas unitarias se encuentrar en la carpeta `test`, el comando para correr las pruebas es el siguiente:
```shell
python -m unittest discover -v
```


## Contruido con 馃洜锔?


* [Python](https://www.python.org/) - Lenguaje de programaci贸n
* [Click](https://click.palletsprojects.com/en/8.0.x/) - Interfaz de linea de comandos.


## Autor 鉁掞笍

* **Javier Manobanda** - *Trabajo Inicial* - [Github](https://github.com/JaviMiot)


## License 馃搫
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---
鈱笍 with鉂わ笍 by [Javier Manobanda](https://github.com/JaviMiot)馃槉
