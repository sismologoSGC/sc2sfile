![SGC](images/sgc_logo.png)<!-- .element width="700"-->

# Sc2Sfile 


Rutina realizada para convertir los eventos en Seiscomp a formato sfile  

## 1. Instalacio linux

### - Requerimientos previos
Se corre en sistemas linux.

### - Python
Python Versión 3.7 en adelante. (Usaremos como ejemplo python 3.10)
```bash
sudo apt-get install python3.7 (o 3.8)
```

Tener virtualenv en python.
```bash
python3.7 -m pip install virtualenv
```

#### Instalación con pip 
```bash
python3.7 -m virtualenv env_sc2sf
source env_sc2sf/bin/activate
pip install -r requirements.txt
```

## Instrucciones de uso

El programa se puede ejecutar en cualquier ambiente que tenga los requerimientos instalados, al ejecutarlo se solicitará una serie de parámetros para realizar la consulta: 

#### Ejecución del programa sc2sfile_2023.py en terminal

```bash
$ python3 sc2sfile_2023.py
```
#### Primer parametro
solicita la fecha inicial, y se ingresa de la siguiente manera: 
(YYYY MM DD hh mm ss)  por ejemplo 2023 03 01 00 00 00

```bash
Fecha inicial (YYYY MM DD hh mm ss):   2023 03 01 00 00 00
```

## Autor

- Daniel Siervo 
- Angel Agudelo adagudelo@sgc.gov.co

