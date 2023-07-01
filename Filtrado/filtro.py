import pandas as pd

filtros = {"Time1":"1643", "Protocol":"17"}
def filtrarDatos(filtros, max):
    chunkSize = 10000 # cantidad de lineas por chunk 
    headers=["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcProt", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"] # nombre de encabezados, debido a que el archivo no tiene
    count = 0 # contador de coincidencias
    flagPrimerChunk = True 

    for chunk in pd.read_csv('/home/mvalenzuela/Downloads/netflow_day-20', chunksize=chunkSize, names=headers): # modificar ruta del archivo antes de ejecutar
        if count > max: # detendra la ejecucion cuando supere la cantidad de coincidencias
            break
        flagPrimerfiltro = True
        for filtro in filtros: # ejecutamos un ciclo for para asignacion de filtros recibidos en los argumentos
            if filtro == "Time1":
                dataFiltro = chunk["Time"] > int(filtros["Time1"])
            elif filtro == "Time2":
                dataFiltro = chunk["Time"] < int(filtros["Time2"])
            else:
                try:
                    dataFiltro= chunk[filtro] == int(filtros[filtro])
                except:
                    dataFiltro = chunk[filtro] == filtros[filtro]
            if flagPrimerfiltro:
                dataFiltros = dataFiltro 
                flagPrimerfiltro = False
            else:
                dataFiltros = dataFiltro & dataFiltros
        
        if flagPrimerChunk: # guardamos las coincidencias
            data = chunk[dataFiltros]
            flagPrimerChunk = False
        else:
            data = pd.concat(data, chunk[dataFiltros])
        count = count + len(chunk[dataFiltros])
    return data # regresamos las coincidencias


