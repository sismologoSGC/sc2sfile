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
#### Primer parámetro
Solicita la fecha inicial, y se ingresa de la siguiente manera: 
(YYYY MM DD hh mm ss)  por ejemplo 2023 03 01 00 00 00

```bash
Fecha inicial (YYYY MM DD hh mm ss):   2023 03 01 00 00 00
```
#### Segundo parámetro 
Solicitala fecha final,  y se ingresa de la siguiente manera: 
(YYYY MM DD hh mm ss)  por ejemplo 2023 03 20 23 59 59


```bash
Fecha final (YYYY MM DD hh mm ss):   2023 03 20 23 59 59 
```

#### Tercer parámetro 
Solicita la opción de escoger con 0 para traer solo los eventos localizables o 1 para traer los eventos localizables y no localizables.


```bash
            ________________
            Solo localizables? o agregamos No localizables?:


            ( 0 ) Solo localizables
            ( 1 ) localizables y No localizables
            ________________


            :1 
```

#### Solo localizables
Cuando seleccione la opción 0 para solo localizables  le solicitará los parámetros de magnitud mínima y máxima, los dos valores separados por un espacio, por ejemplo: 0 10

```bash
Magn_min Magn_max (0 9):0 10
```
#### Cuarto parámetro 
Solicita para la consulta los valores de profundidad mínima y profundidad máxima y se ingresa los dos números separados por un espacio por ejemplo: 0 160.

```bash
 Prof_min Prof_max (0 150):0 160
```

#### Quinto parámetro 
Solicita la opción para escoger el tipo de consulta  0  para hacer una consulta radial, 1 para una consulta rectangular y 2 para hacer una consulta trayendo todo lo registrado en seiscomp.

```bash
            ________________
            Tipo de consulta


            ( 0 ) radial
            ( 1 ) cuadrante
            ( 2 ) todo
            ________________


            :0
```

#### Consulta radial
Cuando seleccione la opción 0 de consulta radial le solicitará los parametros de latitud en grados decimales, longitud en grados decimales y radio en grados, los tres valores separados por un espacio, ejemplo: 7.5535 -76.4525 1.6

```bash
Latitud Longitud Radio_grados (4.54 -74.12 0.2): 7.5535 -76.4525 1.6.
```

#### Consulta cuadrante
Cuando seleccione la opción 1 de consulta en cuadrante le solicitará los parámetros de latitud mínima en grados decimales, latitud máxima en grados decimales, longitud mínima en grados decimales y longitud máxima en grados decimales, los cuatro valores separados por un espacio, ejemplo: 2.13 6.51 -76.1 -70.2


```bash
Lat_min Lat_max Long_min Long_max (3.54 4.5 -74.5 -73.12): 2.13 6.51 -76.1 -70.2
```

## Productos

#### En terminal
Al ingresar todos los parametros requeridos el programa hará la consulta y en terminal imprimirá la información general de todos los eventos consultados y los mostrará de la siguiente manera:

```bash
SGC2023fdbkwr
Event:  2023-03-14T11:38:01.005587Z |  +5.720,  -74.189 | 1.13 MLr_2 | manual


                    resource_id: ResourceIdentifier(id="smi:org.gfz-potsdam.de/geofon/SGC2                                                                                                023fdbkwr")
                     event_type: 'earthquake'
           event_type_certainty: 'known'
                  creation_info: CreationInfo(agency_id='SGC', author='scevent@seismo1.sgc                                                                                                .gov.co', creation_time=UTCDateTime(2023, 3, 14, 11, 45, 33, 241958))
            preferred_origin_id: ResourceIdentifier(id="smi:org.gfz-potsdam.de/geofon/NLL.                                                                                                20230314130831.461691.39090")
         preferred_magnitude_id: ResourceIdentifier(id="smi:org.gfz-potsdam.de/geofon/NLL.                                                                                                20230314130831.461691.39090/netMag/MLr_2")
                           ---------
             event_descriptions: 1 Elements
                          picks: 14 Elements
                        origins: 1 Elements
                     magnitudes: 1 Elements
########### NonLinLoc #################
```

#### Sfiles
Al terminar la consulta y la conversión al final en la terminal mostrará un mensaje diciendo lo siguiente:

```bash
#### los sfiles creados se guardaron en la carpeta --> sfiles_20230314_20230314
```

La carpeta tendrá como nombre “sfiles_” y la fecha inicial y final de consulta, y dentro de ella los sfiles generados.

El nombre de cada sfile contiene la fecha y hora de cada evento, tenga presente que en este nombre tiene dos minutos antes del evento por ejemplo:

El sfile 14-0233-36L.S202303   es del evento con fecha de origen 2023-03-14  02:35:36


## Autor

- Daniel Siervo 
- Angel Agudelo adagudelo@sgc.gov.co

