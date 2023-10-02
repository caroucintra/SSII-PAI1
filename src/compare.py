import hashlib, logging
from scan import *

# Compara los hashes antiguos de la última exploración con los nuevos hashes del estado actual del sistema de archivos
# Devuelve una lista con sublistas de ficheros completos y cambiados
# new_hashes: directiorio con la ruta como clave y el hash como valor
def compare_hashes(new_hashes):
    saved_hashes = read_hashes_to_dict()
    old_hashes = saved_hashes["hashes"]
    good_files = []
    changed_files = []
    file_info = [good_files, changed_files]
    # check for added or changed files
    for key in new_hashes.keys():
        if new_hashes[key] == old_hashes[key]:
            good_files.append(key)
        else:
            changed_files.append(key)
    write_to_log(changed_files)
    return file_info

# 
def initialize_log():
    logging.basicConfig(filename='log.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info("Log initialized")


#
def write_to_log(file_info):
    total_files = 0
    for h in range(4):
        total_files += len(file_info[h])
    logging.info(str(total_files) + " ficheros revisados")
    logging.info("Encontrados " + str(len(file_info[0])) + " ficheros completos\n")
    for i in file_info[0]:
        logging.info(file_info[0][i])
    logging.info("Encontrados " + str(len(file_info[1])) + " ficheros cambiados\n")
    for j in file_info[1]:
        logging.info(file_info[1][j])