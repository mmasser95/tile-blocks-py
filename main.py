import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calc_tiles(area_width, area_height, tile_width, tile_height):
    tiles_x = math.ceil(area_width / tile_width)
    tiles_y = math.ceil(area_height / tile_height)

    tiles_x_completed = math.floor(area_width / tile_width)
    tiles_y_completed = math.floor(area_height / tile_height)

    tiles_complete = tiles_x * tiles_y

    spare_x = area_width % tile_width
    spare_y = area_height % tile_height

    # waste_x = (tiles_y * (tile_width - spare_x)) if spare_x > 0 else 0
    # waste_y = (tiles_x * (tile_height - spare_y)) if spare_y > 0 else 0

    print(f"Area: {area_width}x{area_height}")

    print(f"Tile: {tile_width}x{tile_height}")

    print(f"Tiles (with uncompleted): {tiles_x}x{tiles_y}")

    print(f"Tiles (completed): {tiles_x_completed}x{tiles_y_completed}")

    print(f"Tiles needed: {tiles_complete}")

    print(f"Spares: {spare_x}x{spare_y}")

    plot_tiles2(area_width, area_height, tile_width, tile_height)
    plot_intercalated_tiles(area_width, area_height, tile_width, tile_height)

def plot_tiles(area_width, area_height, tile_width, tile_height):
    fig, ax = plt.subplots(figsize=(10, 6))

    tiles_x = math.ceil(area_width / tile_width)
    tiles_y = math.ceil(area_height / tile_height)

    spare_x = area_width % tile_width
    spare_y = area_height % tile_height

    for i in range(tiles_x):
        for j in range(tiles_y):
            x = i * tile_width
            y = j * tile_height

            width = tile_width if x + tile_width <= area_width else spare_x
            height = tile_height if y + tile_height <= area_height else spare_y

            if width == tile_width and height == tile_height:
                color = "lightblue"
            else:
                color = "red"  # Baldosas incompletas en rojo

            rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    ax.set_xlim(0, area_width)
    ax.set_ylim(0, area_height)
    ax.set_xticks([i * tile_width for i in range(tiles_x + 1)])
    ax.set_yticks([j * tile_height for j in range(tiles_y + 1)])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_title("Distribución de baldosas en la pared")
    ax.set_aspect('equal')

    plt.savefig("tiles_grid.png")  # Guarda la imagen en un archivo

def plot_tiles2(area_width, area_height, tile_width, tile_height, joint=0):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Calcula la cantidad de baldosas necesarias
    tiles_x = math.ceil(area_width / (tile_width + joint))
    tiles_y = math.ceil(area_height / (tile_height + joint))

    spare_x = area_width % (tile_width + joint)
    spare_y = area_height % (tile_height + joint)

    for i in range(tiles_x):
        for j in range(tiles_y):
            x = i * (tile_width + joint)
            y = j * (tile_height + joint)

            width = tile_width if x + tile_width <= area_width else spare_x - joint
            height = tile_height if y + tile_height <= area_height else spare_y - joint

            width = max(width, 0)
            height = max(height, 0)

            color = "lightblue" if width == tile_width and height == tile_height else "red"
            rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

            if color == "red":
                ax.text(x + width / 2, y + height / 2, f"{width} x {height}", 
                        color="black", fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))

    # **Ajustar límites para dejar espacio a las etiquetas**
    ax.set_xlim(-tile_width * 1.5, area_width + tile_width * 1.5)
    ax.set_ylim(-tile_height * 1.5, area_height + tile_height * 1.5)

    # **Etiquetas de dimensiones**
    ax.annotate(f"{area_width} cm", (area_width / 2, -tile_height), 
                ha="center", va="center", fontsize=12, color="black",
                arrowprops=dict(facecolor='black', arrowstyle="<->"))

    ax.annotate(f"{area_height} cm", (-tile_width, area_height / 2), 
                ha="center", va="center", fontsize=12, color="black", rotation=90,
                arrowprops=dict(facecolor='black', arrowstyle="<->"))

    # Configuración de la cuadrícula
    ax.set_xticks([i * (tile_width + joint) for i in range(tiles_x + 1)])
    ax.set_yticks([j * (tile_height + joint) for j in range(tiles_y + 1)])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_title(f"Distribución de baldosas con junta de {joint} cm")
    ax.set_aspect('equal')
    plt.savefig("tiles_grid.png")  # Guarda la imagen en un archivo


def plot_intercalated_tiles(area_width, area_height, tile_width, tile_height):
    fig, ax = plt.subplots(figsize=(10, 6))

    tiles_x = math.ceil(area_width / tile_width)
    tiles_y = math.ceil(area_height / tile_height)

    spare_x = area_width % tile_width
    spare_y = area_height % tile_height

    for j in range(tiles_y):
        offset = (tile_width / 2) if j % 2 == 1 else 0  # Desplazamiento en filas pares

        for i in range(tiles_x + 1):  # Una baldosa extra por el desplazamiento
            x = i * tile_width - offset
            y = j * tile_height

            width = tile_width
            height = tile_height

            # Ajustar si la baldosa sobresale del área
            if x < 0:
                width += x
                x = 0
            elif x + tile_width > area_width:
                width = area_width - x

            if y + tile_height > area_height:
                height = area_height - y

            # Validar que la baldosa tenga tamaño real
            if width <= 0 or height <= 0:
                continue

            color = "lightblue" if width == tile_width and height == tile_height else "red"
            rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

            # **Agregar etiquetas de dimensiones**

            # Mostrar etiqueta solo si la baldosa es incompleta
            if color == "red":
                text_x, text_y = x + width / 2, y + height / 2
                bbox_props = dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8)

                # Si la baldosa es muy pequeña, movemos la etiqueta afuera
                if width < tile_width * .6 or height < tile_height * .6:
                    arrow_x, arrow_y = text_x+width*.6, text_y + height * .6
                    ax.annotate(f"{width} x {height}", (text_x, text_y), 
                                xytext=(arrow_x, arrow_y), textcoords="data",
                                arrowprops=dict(facecolor='black', arrowstyle="->"), 
                                fontsize=8, ha='center', va='center', bbox=bbox_props)
                else:
                    ax.text(text_x, text_y, f"{width:.2f} x {height:.2f}", 
                            color="black", fontsize=8, ha='center', va='center', bbox=bbox_props)

    ax.annotate(f"{area_width} cm", (area_width / 2, -tile_height * 0.5), 
                ha="center", va="center", fontsize=10, color="black",
                arrowprops=dict(facecolor='black', arrowstyle="<->"))

    ax.annotate(f"{area_height} cm", (-tile_width * 0.7, area_height / 2), 
                ha="center", va="center", fontsize=10, color="black", rotation=90,
                arrowprops=dict(facecolor='black', arrowstyle="<->"))
    # Configuración del gráfico
    ax.set_xlim(0, area_width)
    ax.set_ylim(0, area_height)
    ax.set_xticks([i * tile_width for i in range(tiles_x + 1)])
    ax.set_yticks([j * tile_height for j in range(tiles_y + 1)])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_title("Distribución de baldosas intercaladas")
    ax.set_aspect('equal')

    plt.savefig("tiles_grid_intercalated.png")  # Guarda la imagen en un archivo



def calcular_baldosas_intercaladas(ancho_area, alto_area, ancho_baldosa, alto_baldosa):
    # Número de filas necesarias
    filas = math.ceil(alto_area / alto_baldosa)

    # Alternancia de filas completas e intercaladas
    baldosas_por_fila_par = math.ceil(ancho_area / ancho_baldosa)
    baldosas_por_fila_impar = math.ceil((ancho_area - (ancho_baldosa / 2)) / ancho_baldosa) + 1  # Una extra en el borde

    # Se alternan filas pares e impares
    total_baldosas = 0
    for i in range(filas):
        if i % 2 == 0:  # Fila completa
            total_baldosas += baldosas_por_fila_par
        else:  # Fila intercalada
            total_baldosas += baldosas_por_fila_impar

    # Calcular desperdicio (considerando cortes en cada fila)
    desperdicio_x = (filas * (ancho_baldosa - (ancho_area % ancho_baldosa))) if ancho_area % ancho_baldosa > 0 else 0
    desperdicio_y = (baldosas_por_fila_par * (alto_baldosa - (alto_area % alto_baldosa))) if alto_area % alto_baldosa > 0 else 0
    desperdicio_total = desperdicio_x + desperdicio_y

    return total_baldosas, desperdicio_total

calc_tiles(135, 170, 30, 20)
