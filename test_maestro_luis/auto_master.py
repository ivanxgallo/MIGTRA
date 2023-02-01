#!/usr/bin/env python

###################################################################
###################################################################
##############---------- AUTO MASTER 3000 ------------#############
###################################################################
###################################################################

# This code is a way to automate the changes in the Master Excel
# Author: I.G.
# Year: 2023
# Version: 1.0



#----------------------------- RECUERDA -----------------------------#
# Para dar argumentos que se autocompleten:
#           complete -f -o default -X '!*.extension_archivos' este_script.py -(letra_asignada_al_argumento)
# Para no tener que utilizar la forma "python scrip.py -a argumento" y usar "script -a argumento":
#           sudo ln -s /ruta/al/script/script.py /usr/local/bin/script

# sudo ln -s /home/ivan/migtra/pruebas_locales/test_maestro_luis/auto_master.py /usr/local/bin/AutoMaster

# Para reconocer formato file en argumento usar:
#           type=argparse.FileType('r')

import argparse
from changes import *

parser = argparse.ArgumentParser(description='Este es un ejemplo de script ejecutable')

# Here we define the arguments in the comand line
parser.add_argument('-c', '--changes', type=str, help='Nombre del maestro con los cambios en color', required=True)
parser.add_argument('-p', '--previous', type=str, help='Nombre del maestro anterior', required=True)
parser.add_argument('-t', '--utc', type=int, help='Diferencia de horas respecto a UTC', default=3)


# Here we store the variables as args.variable_name
args        =       parser.parse_args()
file_i      =       args.changes
file_f      =       args.previous
delta_utc   =       args.utc


# here we save the changes
changes = get_sheet_changes(file_i)

# then we put the changes in a new excel file
set_sheet_changes(changes, file_f, delta_utc)

