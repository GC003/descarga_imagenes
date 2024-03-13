import os
import requests

def descargar_imagenes(urls, carpeta_destino):
    try:
        # Verifica si la carpeta de destino existe
        if not os.path.exists(carpeta_destino):
            # Creacion de la carpeta si no existe
            os.makedirs(carpeta_destino)

        for i, url in enumerate(urls, start=1):
            # Realiza la solicitud GET a la URL de la imagen
            respuesta = requests.get(url)
            
            # Verifica si la solicitud fue exitosa (código de estado 200)
            if respuesta.status_code == 200:
                # Extrae el nombre del archivo de la URL y guarda la imagen en la carpeta de destino
                nombre = os.path.join(carpeta_destino, f"imagen_{i}.jpg")
                with open(nombre, 'wb') as archivo:
                    archivo.write(respuesta.content)
                print(f"Imagen {i} descargada y guardada en {nombre}.")
            else:
                print(f"Error al descargar la imagen {i}. Código de estado: {respuesta.status_code}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    # Ejemplo de uso: Descargar imágenes desde URLs
    urls_ejemplo = [
        "https://example.com/imagen1.jpg",
        "https://example.com/imagen2.jpg",
        "https://example.com/imagen3.jpg"
    ]

    carpeta_destino_ejemplo = "imagenes_descargadas"
    descargar_imagenes(urls_ejemplo, carpeta_destino_ejemplo)
    
