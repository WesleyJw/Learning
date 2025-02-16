
# Trabalhando com dados do tipo NetCDF
# NetCDF is based on the HDF5 file format,
# which allows for the segregation of metadata and different data
# types in the same file.

import numpy as pd
import rioxarray
import xarray
import matplotlib.pyplot as plt

# Read the Dataset
fn_path = "../pr_2020.nc"
fn_path1 = "/home/wesley/Downloads/zipped_file.nc"

xr = rioxarray.open_rasterio(fn_path1)

# Change units


# Print out the dims, attrs, and coords properties of xr to see how the data are structured.

print(xr.dims)
# print(xr.attrs)
# print(xr.coords)

#xr.attrs['units'] = 'mm'

# print(xr.attrs)
#print("\n\n ")
#print("*" * 20)
#print(xr[0, 100:105, 100:105])
#print(xr['pre'][600, 100:105, 100:105])


#xr_masked = xr['pre'].where(xr['pre'] != xr['pre'].attrs['missing_value'])
#xr_masked[112, :, :].plot()

# xr.attrs
