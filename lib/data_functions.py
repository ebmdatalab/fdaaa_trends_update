import csv
from zipfile import ZipFile
from requests import get
from io import BytesIO

def fda_reg(path):
    """
    Point this function towards the fdaaa_regulatory_snapshot.csv file to turn it into a
    dictionary for what you need in this analysis
    See https://doi.org/10.1101/266452 for more information
    """
    fda_reg_dict = {}
    with open(path) as old_fda_reg:
        reader = csv.DictReader(old_fda_reg)
        for d in reader:
            fda_reg_dict[d['nct_id']] = d['is_fda_regulated']
    return fda_reg_dict

def get_data(path):
    """
    Quick function to load the raw ClinicalTrials.gov data which is a CSV of JSON (can think of as ndjson as well)
    """

    with ZipFile(BytesIO(get(path, stream=True).content), 'r') as zf:
        with zf.open('clinicaltrials_raw_clincialtrials_json_2021-01-18.csv', 'r') as ctgov:
            lines = ctgov.readlines()
            return lines
        
def get_data_local(path):
    """
    Quick function to load the raw ClinicalTrials.gov data which is a CSV of JSON (can think of as ndjson as well) when you have a local file
    """
    with open(path, 'r') as ctgov:
        lines = ctgov.readlines()
        return lines
        
