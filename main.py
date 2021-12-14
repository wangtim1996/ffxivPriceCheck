# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from typing import NamedTuple
from enum import Enum
from statistics import mean
from heapq import nsmallest


class HqFilter(Enum):
    NONE = 0
    HQ = 1
    NQ = 2


class AllegoryItem(NamedTuple):
    name: str
    id: int
    cost: int


class ExarchicItem(NamedTuple):
    name: str
    id: int
    value: int

class BicolorItem(NamedTuple):
    name: str
    id: int

BicolorStore = [
    BicolorItem("Yakow Chuck", 36254)
    , BicolorItem("Luncheon Toad Skin", 36243)
    , BicolorItem("Berkanan Sap", 36261)
    , BicolorItem("Hamsa Tenderloin", 36253)
    , BicolorItem("Amra", 36264)
    , BicolorItem("Gaja Hide", 36242)
    , BicolorItem("Kumbhira Skin", 36245)
    , BicolorItem("Ovibos Milk", 36255)
    , BicolorItem("Almasty Fur", 36203)
    , BicolorItem("Saiga Hide", 36244)
    , BicolorItem("Dynamite Ash", 36259)
    , BicolorItem("Lunatender Blossom", 36258)
    , BicolorItem("Mousse Flesh", 36258)
    , BicolorItem("Bird of Elpis Breast", 36630)
    , BicolorItem("Egg of Elpis", 36256)
    , BicolorItem("Ophiotauros Hide", 36246)
    , BicolorItem("Petalouda Scales", 36260)
    , BicolorItem("Dynamis Crystal", 36262)
]


AllegoryStore = [
    AllegoryItem("Aluminum Ore", 32945, 20)
    , AllegoryItem("Workbench Refining Sand", 32946, 20)
    , AllegoryItem("Thylacoleo Skin", 32948, 20)
    , AllegoryItem("Horsetail", 32944, 20)
    , AllegoryItem("Gardenia Fruit", 32947, 20)
    , AllegoryItem("Spirit Extract", 32949, 20)
    , AllegoryItem("Dwarven Chromite", 29969, 10)
    , AllegoryItem("Caprice Fleece", 29975, 10)
    , AllegoryItem("Megalania Skin", 29977, 10)
    , AllegoryItem("Workbench Resin", 29971, 10)
    , AllegoryItem("Tempest Adhesive", 29973, 10)
    , AllegoryItem("Dried Hi-Ether", 29979, 10)
]

NeoStore = [
    ExarchicItem("Exarchic Sword", 31813, 21)
    , ExarchicItem("Exarchic Baghnakhs", 31814, 42)
    , ExarchicItem("Exarchic Axe", 31815, 42)
    , ExarchicItem("Exarchic Spear", 31816, 42)
    , ExarchicItem("Exarchic Longbow", 31817, 42)
    , ExarchicItem("Exarchic Daggers", 31818, 42)
    , ExarchicItem("Exarchic Guillotine", 31819, 42)
    , ExarchicItem("Exarchic Handgonne", 31820, 42)
    , ExarchicItem("Exarchic Cane", 31821, 42)
    , ExarchicItem("Exarchic Rod", 31822, 42)
    , ExarchicItem("Exarchic Grimoire", 31823, 42)
    , ExarchicItem("Exarchic Codex", 31824, 42)
    , ExarchicItem("Exarchic Star Globe", 31825, 42)
    , ExarchicItem("Exarchic Blade", 31826, 42)
    , ExarchicItem("Exarchic Rapier", 31827, 42)
    , ExarchicItem("Exarchic Gunblade", 31828, 42)
    , ExarchicItem("Exarchic Glaives", 31829, 42)
    , ExarchicItem("Exarchic Tower Shield", 31830, 21)
]

ExarchicStore = [
    ExarchicItem("Exarchic Sword", 31813, 21)
    , ExarchicItem("Exarchic Baghnakhs", 31814, 42)
    , ExarchicItem("Exarchic Axe", 31815, 42)
    , ExarchicItem("Exarchic Spear", 31816, 42)
    , ExarchicItem("Exarchic Longbow", 31817, 42)
    , ExarchicItem("Exarchic Daggers", 31818, 42)
    , ExarchicItem("Exarchic Guillotine", 31819, 42)
    , ExarchicItem("Exarchic Handgonne", 31820, 42)
    , ExarchicItem("Exarchic Cane", 31821, 42)
    , ExarchicItem("Exarchic Rod", 31822, 42)
    , ExarchicItem("Exarchic Grimoire", 31823, 42)
    , ExarchicItem("Exarchic Codex", 31824, 42)
    , ExarchicItem("Exarchic Star Globe", 31825, 42)
    , ExarchicItem("Exarchic Blade", 31826, 42)
    , ExarchicItem("Exarchic Rapier", 31827, 42)
    , ExarchicItem("Exarchic Gunblade", 31828, 42)
    , ExarchicItem("Exarchic Glaives", 31829, 42)
    , ExarchicItem("Exarchic Tower Shield", 31830, 21)
    ###################
    , ExarchicItem("Exarchic Circlet of Fending" ,31831,33)
    , ExarchicItem("Exarchic Coat of Fending" ,31832,42)
    , ExarchicItem("Exarchic Gauntlets of Fending" ,31833,33)
    , ExarchicItem("Exarchic Hose of Fending" ,31834,42)
    , ExarchicItem("Exarchic Sabatons of Fending" ,31835,33)
    , ExarchicItem("Exarchic Plate Belt of Fending",31836, 21)
    ###################
    , ExarchicItem("Exarchic Circlet of Maiming",31837, 33)
    , ExarchicItem("Exarchic Mail of Maiming",31838, 42)
    , ExarchicItem("Exarchic Gauntlets of Maiming",31839, 33)
    , ExarchicItem("Exarchic Hose of Maiming",31840, 42)
    , ExarchicItem("Exarchic Sabatons of Maiming",31841, 33)
    , ExarchicItem("Exarchic Plate Belt of Maiming",31842, 21)
    ###################
    , ExarchicItem("Exarchic Hood of Striking",31843, 33)
    , ExarchicItem("Exarchic Top of Striking",31844, 42)
    , ExarchicItem("Exarchic Armguards of Striking",31845, 33)
    , ExarchicItem("Exarchic Bottoms of Striking",31846, 42)
    , ExarchicItem("Exarchic Boots of Striking",31847, 33)
    , ExarchicItem("Exarchic Sash of Striking",31848, 21)
    ###################
    , ExarchicItem("Exarchic Hood of Aiming",31849, 33)
    , ExarchicItem("Exarchic Top of Aiming",31850, 42)
    , ExarchicItem("Exarchic Armguards of Aiming",31851, 33)
    , ExarchicItem("Exarchic Bottoms of Aiming",31852, 42)
    , ExarchicItem("Exarchic Boots of Aiming",31853, 33)
    , ExarchicItem("Exarchic Sash of Aiming",31854, 21)
    ###################
    , ExarchicItem("Exarchic Hood of Scouting",31855, 33)
    , ExarchicItem("Exarchic Top of Scouting",31856, 42)
    , ExarchicItem("Exarchic Armguards of Scouting",31857, 33)
    , ExarchicItem("Exarchic Bottoms of Scouting",31858, 42)
    , ExarchicItem("Exarchic Boots of Scouting",31859, 33)
    , ExarchicItem("Exarchic Sash of Scouting",31860, 21)
    ###################
    , ExarchicItem("Exarchic Circlet of Healing",31861, 33)
    , ExarchicItem("Exarchic Coat of Healing",31862, 42)
    , ExarchicItem("Exarchic Gloves of Healing",31863, 33)
    , ExarchicItem("Exarchic Hose of Healing",31864, 42)
    , ExarchicItem("Exarchic Shoes of Healing",31865, 33)
    , ExarchicItem("Exarchic Plate Belt of Healing",31866, 21)
    ###################
    , ExarchicItem("Exarchic Hat of Casting",31867, 33)
    , ExarchicItem("Exarchic Coat of Casting",31868, 42)
    , ExarchicItem("Exarchic Gloves of Casting",31869, 33)
    , ExarchicItem("Exarchic Hose of Casting",31870, 42)
    , ExarchicItem("Exarchic Shoes of Casting",31871, 33)
    , ExarchicItem("Exarchic Plate Belt of Casting",31872, 21)
    ###################
    , ExarchicItem("Exarchic Earrings of Fending",31873, 21)
    , ExarchicItem("Exarchic Earrings of Slaying",31874, 21)
    , ExarchicItem("Exarchic Earrings of Aiming",31875, 21)
    , ExarchicItem("Exarchic Earrings of Healing",31876, 21)
    , ExarchicItem("Exarchic Earrings of Casting",31877, 21)
    ###################
    , ExarchicItem("Exarchic Choker of Fending",31878, 21)
    , ExarchicItem("Exarchic Choker of Slaying",31879, 21)
    , ExarchicItem("Exarchic Choker of Aiming",31880, 21)
    , ExarchicItem("Exarchic Choker of Healing",31881, 21)
    , ExarchicItem("Exarchic Choker of Casting",31882, 21)
    ###################
    , ExarchicItem("Exarchic Bracelet of Fending",31883, 21)
    , ExarchicItem("Exarchic Bracelet of Slaying",31884, 21)
    , ExarchicItem("Exarchic Bracelet of Aiming",31885, 21)
    , ExarchicItem("Exarchic Bracelet of Healing",31886, 21)
    , ExarchicItem("Exarchic Bracelet of Casting",31887, 21)
    ###################
    , ExarchicItem("Exarchic Ring of Fending",31888, 21)
    , ExarchicItem("Exarchic Ring of Slaying",31889, 21)
    , ExarchicItem("Exarchic Ring of Aiming",31890, 21)
    , ExarchicItem("Exarchic Ring of Healing",31891, 21)
    , ExarchicItem("Exarchic Ring of Casting",31892, 21)
]

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
    response = requests.get("https://universalis.app/api/history/"+server+"/" + str(item.id))
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
    print(item.name + " " + str(estVal))
    return estVal

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    command = "bicolor"

    if command == "bicolor":
        bicolorResults = []
        for item in BicolorStore:
            avgprice = curr_marketboard_low(item, HqFilter.NONE, "Hyperion", 50)
            bicolorResults.append((avgprice, item.name))

        bicolorResults.sort(reverse=True)
        print(bicolorResults)
    elif command == "allegory":
        results = []
        for item in AllegoryStore:
            avgprice = curr_marketboard_low(item)
            results.append(((avgprice/item.cost), item.name))

        results.sort(reverse=True)
        print(results)
    elif command == "exarchic":
        exarchicResults = []
        for item in ExarchicStore:
            avgprice = curr_marketboard_low(item, HqFilter.HQ)
            exarchicResults.append(((item.value / avgprice), item.name))
        exarchicResults.sort(reverse=True)
        print(exarchicResults)








