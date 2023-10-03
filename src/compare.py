import logging
import scan, config, scan
from scan import *

# Compara los hashes antiguos de la última exploración con los nuevos hashes del estado actual del sistema de archivos
# Devuelve una lista con sublistas de ficheros completos y cambiados
# new_hashes: directiorio con la ruta como clave y el hash como valor
def compare_hashes(dict_new_hashes):
    saved_hashes = read_hashes_to_dict()
    new_hashes = dict_new_hashes["hashes"]
    good_files = []
    changed_files = []
    file_info = []
    # check for added or changed files
    for key in new_hashes.keys():
        if new_hashes[key] == saved_hashes[key]:
            good_files.append(key)
        else:
            changed_files.append(key)
    print("alles gut")
    file_info.append(good_files)
    file_info.append(changed_files)
    write_to_log(file_info)
    return file_info


# Crea un documento de log
def initialize_log():
    log_format = '%(asctime)s - %(message)s'
    logging.basicConfig(filename='log.log', filemode='a', format=log_format, level=logging.INFO)
    logging.info("Log initialized")


# Escribe los resultados del scan en el documento de log
def write_to_log(file_info):
    print(len(file_info))
    total_files = len(file_info[0]) + len(file_info[1])
    
    logging.info(str(total_files) + " ficheros revisados")
    logging.info("Encontrados " + str(len(file_info[0])) + " ficheros completos")

    for i in range(len(file_info[0])):
        print(file_info[0][i])
        logging.info(file_info[0][i])
    
    logging.info("Encontrados " + str(len(file_info[1])) + " ficheros cambiados")
    for j in range(len(file_info[1])):
        print(file_info[1][j])
        logging.info(file_info[1][j])


""" initialize_log()
conf = config.writeDefaultConfig()
dict_new_hashes = scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], True, False)
compare_hashes(dict_new_hashes) """