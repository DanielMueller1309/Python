#!/usr/bin/env python3.8
from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import os

@jit(nopython=True)
def mandelbrot(c, max_iter):
    z = 0j
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

@jit(nopython=True)
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((width, height), dtype=np.uint32)
    for i in range(width):
        for j in range(height):
            mandelbrot_image[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return mandelbrot_image


@jit(nopython=True)
def plot_mandelbrot(xmin, xmax, ymin, ymax, width=800, height=800, max_iter=256, filename="mandelbrot.png"):
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


def save_image(xmin, xmax, ymin, ymax, width, height, max_iter, filename):
    print(f"Saving {filename}, xmin: {xmin}, xmax: {xmax}, ymin: {ymin}, ymax: {ymax}")
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    if np.all(mandelbrot_image == max_iter):
        print(f"Warning: Image {filename} will be completely black")
    plt.imsave(filename, mandelbrot_image, cmap='hot')
    return filename

@jit(nopython=True)
def calculate_max_iter(i, base_max_iter, increase_factor):
    return int(base_max_iter * (increase_factor ** i))

def create_zoom_images(x_center, y_center, zoom_factor, num_images, output_dir="mandelbrot_set_pics", base_max_iter=256, width=800, height=800):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Diese Werte steuern, wie stark max_iter mit jedem Bild zunimmt.
    # Der increase_factor sollte größer als 1 sein, um eine Erhöhung zu gewährleisten.
    increase_factor = 1.05

    scale_factors = [zoom_factor ** i for i in range(num_images)]
    file_names = [os.path.join(output_dir, f"mandelbrot_zoom_{i}.png") for i in range(num_images)]

    max_workers = 4  # Verwenden Sie so viele Kerne, wie Sie für angemessen halten

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for i, (scale, fname) in enumerate(zip(scale_factors, file_names)):
            max_iter = calculate_max_iter(i, base_max_iter, increase_factor)
            # Planen Sie die Bilderstellung
            future = executor.submit(save_image, x_center - scale, x_center + scale, y_center - scale, y_center + scale, width, height, max_iter, fname)
            futures[future] = fname  # Dictionary zum Speichern der Zuordnung Future -> Dateiname

        # Fortschritt überwachen und auf Ergebnisse warten
        for future in as_completed(futures):
            res = future.result()  # Dies blockiert, bis das zugehörige Bild fertig ist
            print(f"{res} is completed.")

x_center, y_center = -0.743643887037158704752191506114774, 0.131825904205311970493132056385139
zoom_factor = 0.85
num_images = 1000

create_zoom_images(x_center, y_center, zoom_factor, num_images)
