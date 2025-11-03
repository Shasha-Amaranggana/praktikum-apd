import os
import inquirer
from prettytable import PrettyTable

akun = {
    "1" : {"us" : "1", "pw" : "1", "st" : "admin"},
    "2" : {"us" : "2", "pw" : "2", "st" : "pengguna"}}
char_meta = {
    "1": {"nama": "Mavuika", "elemen": "Pyro", "senjata": "Claymore", "peran": "Main DPS"},
    "2": {"nama": "Furina", "elemen": "Hydro", "senjata": "Sword", "peran": "Sub DPS"},
    "3": {"nama": "Bennet", "elemen": "Pyro", "senjata": "Sword", "peran": "Support"},}
valid_esp = {
    "elemen" : ("Pyro", "Cryo", "Electro", "Hydro", "Anemo", "Geo", "Dendro"),
    "senjata" : ("Sword", "Claymore", "Polearm", "Catalyst", "Bow"),
    "peran" : ("Main DPS", "Sub DPS", "Support")}
request_meta = {}