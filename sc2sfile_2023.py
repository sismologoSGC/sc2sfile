#!/usr/bin/python3
# coding=utf-8*
"""
Daniel Siervo <dsiervo@sgc.gov.co> (13 de Mayo de 2022)
Versión en python 3 del programa seiscomp2sfiles.py 
Modificado por I. Molina (18. Feb.2022) para consulta en area circular
Modificado por Angel A. (jul. 2022),  (mar, 2023)
"""

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.header import FDSNNoDataException
from datetime import timedelta
import os
import sys


def get_param():

    server_IP = 'http://10.100.100.232'
    port_fdsn = "8091"
    Format = "mseed"
    # seiscomp 2018-2021 (funciona bien)
    
    #Fechas inicio y final
    st1 = input("\n\tFecha inicial (YYYY MM DD hh mm ss): ")
    st = st1.strip(")").strip("(").replace(" ", "")
    et1 = input("\n\tFecha final (YYYY MM DD hh mm ss): ")
    et = et1.strip(")").strip("(").replace(" ", "")

    #localizable o no localizable
    nloc = input(""" 
            ________________
            Solo localizables? o agregamos No localizables?:
                         
            ( 0 ) Solo localizables 
            ( 1 ) localizables y No localizables
            ________________

            :   """).strip(")").strip("(").strip("(")

    #Magnitudes 
    if nloc == "0":

        mag1 = input("\n\t Magn_min Magn_max (0 9): ")
        mag = mag1.strip(")").strip("(").split()
        print(mag)
    
    elif nloc == "1":
        mag = [0,0]
    else: 
        print("\n\t LA LETRA INGRESADA NO ES CORRECTA, DIGITE 0 o 1")
        sys.exit()

    #Profundidad
    prof1 = input("\n\t Prof_min Prof_max (0 150): ")
    prof = prof1.strip(")").strip("(").split()
    if prof[0] == "0": prof = ["-10",prof[1]]

    #Tipo de consulta
    consulta1 = input("""
            ________________ 
            Tipo de consulta
            
            ( 0 ) radial
            ( 1 ) cuadrante
            ( 2 ) todo
            ________________
            
            :   """)
    #Descargar forma de onda
    cons_wave = input("\n\t Descargar formas de onda? SI(0) NO(1)):  ")

            
    consulta = consulta1.strip(")").strip("(")
    if consulta == "0":
        
        print("##Consulta radial ")
        loc = input("\n\t Latitud Longitud Radio_grados (4.54 -74.12 0.2): ").split()
    elif consulta == "1":
        print("##Consulta por cuadrante")
        loc = input("\n\t Lat_min Lat_max Long_min Long_max (3.54 4.5 -74.5 -73.12 ): ").split()
    elif consulta == "2":
        print("##Todo lo registrado")
        loc =" "
    else:
        print("\n\t LA LETRA INGRESADA NO ES CORRECTA, DIGITE 0, 1 o 2")
        sys.exit()
        
    if cons_wave != "0" and cons_wave != "1":
        print("\n\t LA LETRA INGRESADA NO ES CORRECTA, DIGITE 0 o 1")
        sys.exit()
    
    starttime = UTCDateTime(st)    
    endtime = UTCDateTime(et)

    return server_IP, port_fdsn, starttime, endtime, loc, mag, prof, consulta, nloc, Format, cons_wave


def sc2sfiles(server_IP, port_fdsn, starttime, endtime, loc,mag, prof,consulta,nloc,Format,cons_wave):
    
    client = Client(server_IP+":"+port_fdsn)

    try:
        
        #Fechas inicio y final
        year_s,month_s,day_s  = starttime.year, starttime.month, starttime.day
        year_e,month_e,day_e  = endtime.year, endtime.month, endtime.day
        
        #Magnitudes
        mag_min = float(mag[0])
        mag_max = float(mag[1])
        
        #Profundidad
        prof_min = float(prof[0])
        prof_max = float(prof[1]) 
        
        #( 0 ) solo localizable ( 1 ) localizables y no localizables
        if nloc == "0":

            # ( 0 )  Consulta radial
            if consulta == "0":
                    lat = float(loc[0])
                    long = float(loc[1])
                    radio = float(loc[2])
            
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                latitude=lat, longitude=long,
                                maxradius=radio, mindepth=prof_min, maxdepth=prof_max,minmagnitude=mag_min,
                                maxmagnitude=mag_max)
            # ( 1 ) Consulta por cuadrante
            if consulta == "1":
                    lat_min = float(loc[0])
                    lat_max = float(loc[1])
                    lon_min = float(loc[2])
                    lon_max = float(loc[3])
                    
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                minlatitude=lat_min, maxlatitude=lat_max, minlongitude=lon_min, maxlongitude=lon_max,
                                mindepth=prof_min, maxdepth=prof_max, minmagnitude=mag_min, maxmagnitude=mag_max)
            # ( 2 ) Consultar todo
            if consulta == "2":
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                mindepth=prof_min, maxdepth=prof_max,minmagnitude=mag_min,
                                maxmagnitude=mag_max)
        6#( 0 ) solo localizable ( 1 ) localizables y no localizables
        if nloc == "1":

            # ( 0 )  Consulta radial
            if consulta == "0":
                    lat = float(loc[0])
                    long = float(loc[1])
                    radio = float(loc[2])
            
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                latitude=lat, longitude=long,
                                maxradius=radio, mindepth=prof_min, maxdepth=prof_max)

            # ( 1 ) Consulta por cuadrante
            if consulta == "1":
                    lat_min = float(loc[0])
                    lat_max = float(loc[1])
                    lon_min = float(loc[2])
                    lon_max = float(loc[3])
                    
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                minlatitude=lat_min, maxlatitude=lat_max, minlongitude=lon_min, maxlongitude=lon_max,
                                mindepth=prof_min, maxdepth=prof_max)

            # ( 2 ) Consultar todo
            if consulta == "2":
                    cat = client.get_events(starttime=starttime, endtime=endtime, includearrivals=True,
                                mindepth=prof_min, maxdepth=prof_max)
                    

        
    except FDSNNoDataException:
    # imprime en rojo que la búsqueda no trajo ningún evento
        print("\033[91mNo hay eventos en el área y tiempo seleccionados\033[0m")
        sys.exit()
    mes_e = str(month_e).rjust(2,"0")
    dia_e = str(day_e).rjust(2,"0")
    mes_s = str(month_s).rjust(2,"0")
    dia_s = str(day_s).rjust(2,"0")

    folder_name = f"sfiles_{year_s}{mes_s}{dia_s}_{year_e}{mes_e}{dia_e}" #crea carpeta de salida

# si la carpeta no existe, la crea
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    con_conv = 0
    con_noconv = 0
    for event in cat:
        if event.event_type != "not existing":
            
            time = event.preferred_origin().time - timedelta(hours=0, minutes=2)
        # la forma de onda empieza 2 min antes del sismo
            min_w = time.minute
            event_id = event.resource_id.resource_id.split('/')[2]
            print(event_id)
            print(event)
            
            
            
            if cons_wave == "0":
            #   Forma de onda y nombre 
                #tiempos
                t =  UTCDateTime(int(time.year), int(time.month), int(time.day), int(time.hour), int(time.minute), int(time.second))
                t_d = 720  #12 minutos
                
                client = Client(server_IP+":"+port_fdsn)
                st = client.get_waveforms("*", "*", "*", "*", t, t+t_d)
                name_w = f"{time.year}-{time.month}-{time.day}-{time.hour}{time.minute}-{int(time.second)}M.COL___{len(st)}"
                wave_path = os.path.join(folder_name, name_w)
            #   "ARC PRV   HHZ CM 00 %s %s%s %s%s %s   300"
                #w ="ARC                 %s %s%s %s%s %s   800"%(\
                #str(time.year), str(time.month).rjust(2,"0"), str(time.day).rjust(2,"0"),
                #str(time.hour).rjust(2,"0"), str(min_w).rjust(2,"0"), str(time.second).rjust(2,"0"))
                w=name_w
                
            if cons_wave == "1":
                w="ARC                 %s %s%s %s%s %s   800"%(\
                str(time.year), str(time.month).rjust(2,"0"), str(time.day).rjust(2,"0"),
                str(time.hour).rjust(2,"0"), str(min_w).rjust(2,"0"), str(time.second).rjust(2,"0"))
                
            name = str(time.day).rjust(2,"0")+"-"+str(time.hour).rjust(2,"0")+str(time.minute).rjust(2,"0")+\
            "-"+str(time.second).rjust(2,"0")+"L.S"+str(time.year)+str(time.month).rjust(2,"0")

            
            
        # arreglando los eventos de hypo71
            event2 = fix_hypo71(event)
        
            wf_path = os.path.join(folder_name, name)
            
            try:
                    event2.write(wf_path, format="NORDIC", userid="anls", wavefiles=[w], high_accuracy=False)
                    con_conv += 1
                    if cons_wave == "0":
                        st.write(wave_path, Format) #Guardar forma de onda
            except:
                    os.system(f"rm {wf_path}")
                    print(f"\n\TNO SE PUEDE CONVERTIR EL EVENTO {event_id}")
                    con_noconv += 1
                    continue
            print('Output file name: ' + wf_path)

    print("\nNumero de eventos convertidos:  ", con_conv)
    print("Numero de eventos no convertidos:  ", con_noconv)
    print("\n\t#### los sfiles creados se guardaron en la carpeta --> ", folder_name,"\n\n")
    
def fix_hypo71(event):
    """Si el método de localización del evento fue Hypo71, se llena el método
    origin_uncertainty con los valores máximo y mínimo  entre las incertidumbres
    en latitud y longitud con la clase OriginUncertainty.
    Si el evento no fué localizado por Hypo71, se retorna el evento original.

    Parameters
    ----------
    event : obspy.core.event.event.Event
        Clase de obspy que describe un evento sísmico.
    """
    try:
        loc_method = event.preferred_origin().method_id.id.split('/')[-1]
        
        print("###########",loc_method,"#################")
        if loc_method == 'Hypo71':
            from obspy.core.event.origin import OriginUncertainty
            
            fixed_event = event.copy()
            
            orig = fixed_event.preferred_origin()
            uncs = (orig.latitude_errors.uncertainty, orig.longitude_errors.uncertainty)
            min_unc = min(uncs)
            max_unc = max(uncs)
            origin_uncertainty = OriginUncertainty(
                                    min_horizontal_uncertainty=min_unc,
                                    max_horizontal_uncertainty=max_unc)
            
            # Asignando la incertidumbre al evento
            fixed_event.origins[0].origin_uncertainty = origin_uncertainty
            
            return fixed_event
        else:
            return event
    except:
        return event



if __name__ == "__main__":

    server_IP, port_fdsn, starttime, endtime, loc, mag, prof, consulta, nloc, Format,cons_wave = get_param()

    sc2sfiles(server_IP, port_fdsn, starttime, endtime, loc, mag,prof, consulta, nloc, Format, cons_wave)
