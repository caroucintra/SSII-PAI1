import glob, os, hashlib, json

BUFFER_SIZE = 16384 # 16 kilo bytes

# Devuelve una lista de las rutas de todos los ficheros en el directorio especificado y todos sub-dicrectorios
# path: String -> directorio raíz a buscar 
def scan_all_files(path):
    path = path + "\**"
    filenames = []
    for filename in glob.iglob(path, recursive=True):
        if os.path.isfile(filename):  # filter dirs
            filenames.append(os.path.abspath(filename))
    
    hash_all_files(filenames, "sha256")
    return filenames

# Devuelve un dicionario de todos los hash de las rutas de los ficheros en la lista especificada a base de una función de hash y lo guardo en hashes.json
# list_filenames: [] String -> lista con las rutas de los ficheros
# hashfunction: String -> especifica la función de hash
def hash_all_files(list_filenames, hashfunction):
    dict_hashes = {}
    for filename in list_filenames:
        bytes_file = read_file(filename)
        if hashfunction == "md5":
            dict_hashes[filename] = hashlib.md5(bytes_file).hexdigest()
        elif hashfunction == "sh1":
            dict_hashes[filename] = hashlib.sha1(bytes_file).hexdigest()
        else:
            dict_hashes[filename] = hashlib.sha256(bytes_file).hexdigest()

    with open("hashes.json", "w") as write_file:
        json.dump(dict_hashes, write_file)

    return dict_hashes

# Lee un fichero y devuelve los bytes
# file: String -> ruta del fichero a leer
def read_file(file):
    b = b""
    with open(file, "rb") as f:
        while True:
            # lee 16mil bytes del fichero
            bytes_read = f.read(BUFFER_SIZE)
            if bytes_read:
                # si hay bytes, añadelos
                b += bytes_read
            else:
                # si no, terminamos
                break
    return b

# Lee el fichero hashes.json y devuelve el dicionario con la ruta como clave y el hash como valor
def read_hashes_to_dict():
    with open("hashes.json", "r") as read_file:
        dict_hashes = json.load(read_file)
    
    print("\n".join("{0} |||| {1}".format(k, v)  for k,v in dict_hashes.items()))
    return dict_hashes


        

print("Start...")
scan_all_files(
    "filesystem",
)
read_hashes_to_dict()