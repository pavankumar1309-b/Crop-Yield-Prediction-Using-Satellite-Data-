import rasterio
import numpy as np

def calculate_ndvi(image_path):
    with rasterio.open(image_path) as src:
        red = src.read(3).astype(float)
        nir = src.read(4).astype(float)
        ndvi = (nir - red) / (nir + red + 1e-5)
    return np.mean(ndvi)
