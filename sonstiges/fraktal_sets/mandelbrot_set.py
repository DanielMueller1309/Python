#!/usr/bin/env python3.8
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import os

@jit(nopython=True)
def mandelbrot(c, max_iter):
    z = 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((width, height))
    for x in range(width):
        for y in range(height):
            mandelbrot_image[x, y] = mandelbrot(complex(r1[x], r2[y]), max_iter)
    return mandelbrot_image


def plot_mandelbrot(xmin, xmax, ymin, ymax, width=1800, height=1800, max_iter=256, filename="mandelbrot.png"):
    # Stellen Sie die Figurgröße und DPI ein, wie zuvor besprochen
    dpi = 100
    figsize = (width / dpi, height / dpi)

    # Erstellen Sie eine neue Figur mit der gewünschten Größe und DPI
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    # Generieren Sie das Mandelbrot-Bild
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    # Erstellen Sie das Bild ohne Achsen und Rahmen
    ax.imshow(mandelbrot_image.T, extent=[xmin, xmax, ymin, ymax], aspect='equal', cmap='hot')
    ax.axis('off')
    ax.set_frame_on(False)  # Schaltet den Rahmen der Achse aus

    # Speichern Sie das Bild direkt ohne Rand und ohne zusätzlichen weißen Raum
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(filename, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Saved: {filename}")

def create_zoom_images(x_center, y_center, zoom_factor, num_images, output_dir="mandelbrot_set_pics", max_iter=256):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    for i in range(num_images):
        scale = zoom_factor ** i
        xmin, xmax = x_center - scale, x_center + scale
        ymin, ymax = y_center - scale, y_center + scale

        filename = os.path.join(output_dir, f"mandelbrot_zoom_{i}.png")
        plot_mandelbrot(xmin, xmax, ymin, ymax, max_iter=max_iter, filename=filename)

x_center, y_center = -0.743643887037158704752191506114774, 0.131825904205311970493132056385139
zoom_factor = 0.95
num_images = 1000

create_zoom_images(x_center, y_center, zoom_factor, num_images)
