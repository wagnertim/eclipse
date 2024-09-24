#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:20:37 2021

@author: timw
"""

# This function reads and plots an AERIoe netCDF file.

#  Start by importing the necessary bits.

import netCDF4 as nc


def read_tropoe(f):

    #  Load the file

    ds=nc.Dataset(f)

    #  I don't want to have to deal with the automatic masking that the netcdf 4 
    #  module does, so I'm turning off all the masking now.

    for k in ds.variables:
        ds.variables[k].set_auto_mask(False)

    #  Define an AERI class that contains all of the data in there that we're 
    #  going to use. 

    class aeri:

        base = ds['base_time'][:]
        offset = ds['time_offset'][:]
        time = ds['hour'][:]
        height = ds['height'][:]
        temp = ds['temperature'][:]
        wvmr = ds['waterVapor'][:]
        sig_t = ds['sigma_temperature'][:]
        sig_q = ds['sigma_waterVapor'][:]

    #
    
    return aeri