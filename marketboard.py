# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from typing import NamedTuple
from enum import Enum
from statistics import mean
from heapq import nsmallest
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()
sheet_id = os.getenv('SHEET_ID')
bicolor_sheet = "Bicolor"
bicolor_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={bicolor_sheet}"
bicolor_data = pd.read_csv(bicolor_url)

aphorism_sheet = "Aphorism"
aphorism_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={aphorism_sheet}"
aphorism_data = pd.read_csv(aphorism_url)

class HqFilter(Enum):
    NONE = 0
    HQ = 1
    NQ = 2

class ItemData(NamedTuple):
    value: float
    name: str
    price: float


# Deprecated
def access_marketboard(item, filter=HqFilter.NONE, server="primal"):
    response = requests.get("https://universalis.app/api/history/"+server+"/" + str(item.id))
    data = response.json()
    dotProduct = 0
    totalWeight = 0
    for entry in data["entries"]:
        if filter == HqFilter.HQ and entry["hq"] is False:
            continue
        if filter == HqFilter.NQ and entry["hq"] is True:
            continue

        val = entry["pricePerUnit"]
        weight = entry["quantity"]
        dotProduct += val * weight
        totalWeight += weight

    print(item.name + " " + str(dotProduct / totalWeight))
    return dotProduct / totalWeight

# cutoff is hella hacky
def curr_marketboard_low(item, filter=HqFilter.NONE, server="primal", cutoff=99999):
    response = requests.get("https://universalis.app/api/history/"+server+"/" + str(item.ID))
    data = response.json()
    prices = []
    for listing in data["entries"]:
        if filter == HqFilter.HQ and listing["hq"] is False:
            continue
        if filter == HqFilter.NQ and listing["hq"] is True:
            continue
        prices.append(listing["pricePerUnit"])
        cutoff = cutoff - 1
        if cutoff < 0:
            break

    estVal = mean(nsmallest(10, prices))
    print(item.Name + " " + str(estVal))
    return estVal

# Returns the list sorted by best value
# Tuple : (value, name, marketboard price)
def get_best_bicolor():
    bicolor_results = []

    for item in bicolor_data.itertuples():
        avgprice = curr_marketboard_low(item, HqFilter.NONE, "Hyperion", 50)
        value = avgprice / item.Price
        bicolor_results.append(ItemData(value, item.Name, avgprice))

    bicolor_results.sort(reverse=True)
    return bicolor_results

def get_best_aphorism():
    aphorism_results = []

    for item in aphorism_data.itertuples():
        avgprice = curr_marketboard_low(item, HqFilter.NONE, "Hyperion", 50)
        value = avgprice / item.Price
        aphorism_results.append(ItemData(value, item.Name, avgprice))

    aphorism_results.sort(reverse=True)
    return aphorism_results

