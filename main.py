from pathlib import Path

def main():
    ruta = r"C:\MTS\estudios\python\automatizador de ordenamiento de archivos\carpeta"
    #ruta = r"\carpeta"
    
    p = Path(ruta)

    tipo_archivos = {
        'PDF': '.pdf', 
        'Word': ['.docx', '.doc', '.docm', '.dotx', '.dotm'],
        'TXT': '.txt',
        'IMG': ['.jpg', '.jpeg', '.png', '.gif'],
        'EXCEL': ['.xlsx', '.xlsm', '.xls', '.xlsb'],
        'CSV': '.CSV',
        'JAR': '.JAR'
    }   
    
    arch = {
        '.png': 'IMG',
        '.txt': 'TXT',
        '.docx': 'WORD',
        '.xlsx': 'EXCEL',
        '.pdf': 'PDF',
        '.csv': 'CSV',
        '.jar': 'JAR',
        '.jpeg': 'IMG'
    }

    # for file in p.iterdir():
    #     if file.name.endswith('.txt'):
    #         file.unlink()

    existe = existencia_de_carpetas(p, tipo_archivos)

    if not existe:
        for n in tipo_archivos.keys():
            p.joinpath(n).mkdir(exist_ok=True)
            
    for archivo in p.iterdir():
        for key, value in arch.items():
            if archivo.name.endswith(key):
                archivo.move_into(p / value)


def existencia_de_carpetas(p, tipo_archivos) -> bool:
    
    for file in p.iterdir():

        if file.is_dir() and file.name in tipo_archivos.keys():
            return True
        
    return False























if __name__ == '__main__':
    main()