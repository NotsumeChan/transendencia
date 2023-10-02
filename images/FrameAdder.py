from PIL import Image, ImageDraw

# Ruta de la imagen que deseas procesar
imagen_path = "C:/Users/Notsume/Documents/universidad/proyecto de titulo/Transcendencia/game/images/assets/tm/Eleccion_ropa/prenda_03.jpg"

# Abre la imagen original
imagen_original = Image.open(imagen_path)

# Define el color del marco (en formato RGBA, donde el último valor es la opacidad)
color_marco = (128, 0, 128, 255)  # Morado

# Ancho del marco
ancho_marco = 10

# Crea una copia de la imagen original para mantenerla intacta
imagen_con_marco = imagen_original.copy()

# Crea un objeto ImageDraw para dibujar el marco en la copia
dibujar = ImageDraw.Draw(imagen_con_marco)

# Obtiene las dimensiones de la imagen
ancho, alto = imagen_con_marco.size

# Dibuja el marco en la imagen copia
dibujar.rectangle([(0, 0), (ancho - 1, alto - 1)], outline=color_marco, width=ancho_marco)

# Guarda la imagen con el marco morado
imagen_con_marco_path = "imagen_con_marco.jpg"
imagen_con_marco.save(imagen_con_marco_path)

# Cierra las imágenes
imagen_original.close()
imagen_con_marco.close()

print(f"Se ha agregado un marco morado a {imagen_path} y se ha guardado como {imagen_con_marco_path}.")
