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

### Forma general
Con +s se indica la fecha inicial y con +e la fecha final donde se desea hacer la revisión.
```bash
python revision.py +s 20210601T000000 +e 20210620T000000
```
### Filtrar usuario
Se añade +u para poner el usuario.
```bash
python revision.py +s 20210601T000000 +e 20210620T000000 +u ecastillo
```

### Guardar en un archivo
Se añade +o (True o False) donde True es usado para guardar. Se debe añadir "> archivo.txt"
```bash
python revision.py +s 20210601T000000 +e 20210620T000000 +u ecastillo +o True > archivo.txt
```


## Autor

- Daniel Siervo 
- Angel Agudelo adagudelo@sgc.gov.co

