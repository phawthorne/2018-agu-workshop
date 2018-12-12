import numpy as np
import requests

"""
Module to download data, do moving average calculations.
"""


def generate_url(location):
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location}-TAVG-Trend.txt'
    return url


def download_data(location):
    """
    Downloads average temperature data for `location`. Returns as a np.array.
    """
    url = generate_url(location)
    response = requests.get(url)
    data = np.loadtxt(response.iter_lines(), comments="%")
    return data


def moving_average(data, width):
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return moving_avg
