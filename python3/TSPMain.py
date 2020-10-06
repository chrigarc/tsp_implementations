from TSPInstance import TSPInstance
import sys
import os
import numpy as np

def main(argv):
    assert len(argv) != 0 , 'Se requiere el nombre del archivo'
    assert os.path.isfile(argv[0]), 'El archivo no existe'
    tspInstance = TSPInstance.readFile(argv[0])
    assert tspInstance, 'Error al leer la instancia'
    print(tspInstance.nodes)
    print(tspInstance.distancias)

if __name__ == "__main__":
    main(sys.argv[1:])
