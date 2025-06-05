import os
def create_directory():

    if not os.path.isdir('reports'):
        os.makedirs("reports")
    else :
        raise ValueError("Erreru sur la création du repertoire reports")

    if not os.path.isdir('logs'):
        os.makedirs("logs")
    else :
        raise ValueError("Erreru sur la création du repertoire logs")