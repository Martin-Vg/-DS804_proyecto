from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import Filtrado.filtro as fl

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles') # Instancia de flask llamada app


@app.route('/')  # Anotador para unicamente modificar el codigo sin tener que hacer una instancia de app
def index():
       return render_template('index.html') # cargamos el html desde la plantilla
 

@app.post('/filtrar_datos')
def getInput(): # funcion que es ejecutada al realizar un metodo post en la ruta
       timeStart = request.form.get('timeStart')  # asignacion de variables  
       timeEnd = request.form.get('timeEnd')
       srcDevice = request.form.get('srcDevice')
       dstDevice = request.form.get('dstDevice')   
       protocol = request.form.get('protocol')   
       srcPort = request.form.get('srcPort')   
       dstPort = request.form.get('dstPort')   
       if not max: # comprobaciones
              return "favor de ingresar un numero de coincidencias"
       try:                                      
              max = int(request.form.get('max'))
       except:
              return "Formato de numero de coincidencias invalido"

       try:
              timeStart = int(timeStart)
              timeEnd = int(timeEnd)
       except:
              return "Formato de tiempo invalido"

       try:
              protocol = int(protocol)
       except:
              return "Formato de protocolo invalido"
       filtro = {} # diccionario donde se almacenaran el nombre del filtro con su valor


       if timeStart: # asignacion de valiables 
              filtro["Time1"] = timeStart
       if timeEnd:
              filtro["Time2"] = timeEnd
       if srcDevice:
              filtro["SrcDevice"] = srcDevice
       if dstDevice:
              filtro["DstDevice"] = dstDevice
       if protocol:
              filtro["Protocol"] = protocol
       if srcPort:
              filtro["SrcPort"] = srcPort
       if dstPort:
              filtro["DstPort"] = dstPort
       


       df = pd.DataFrame(fl.filtrarDatos(filtro, max)) # guardamos el dataframe de la informacion filtrada
       return render_template("table.html", column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip) # cargamos la informacion en la plantilla guardada

