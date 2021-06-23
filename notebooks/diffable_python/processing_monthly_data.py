# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import numpy as np
from datetime import date
from tqdm.auto import tqdm
from zipfile import ZipFile

import os
import re
import matplotlib.pyplot as plt

import sys
from pathlib import Path
cwd = os.getcwd()
parent = str(Path(cwd).parents[0])
sys.path.append(parent)

# +
old_fda = parent + '/data/fdaaa_regulatory_snapshot.csv'

#This takes a full clinicaltrials.gov dataset from our archives
#Due to size, this is not in our GitHub repo, but stored on Dropbox 
#Example path to data is below
path = 'https://www.dropbox.com/s/rrdhpuosiveh5wf/clinicaltrials_raw_clincialtrials_json_2021-06-15.csv.zip?dl=1'

from lib.data_functions import fda_reg, get_data

fda_reg_dict = fda_reg(old_fda)
lines = get_data(path, '2021-06-15')

#headers is just the list of header names to save space here
from lib.final_df import make_row, make_dataframe, headers

#Just pACTs/ACTs
df = make_dataframe(tqdm(lines), fda_reg_dict, headers, act_filter=True, scrape_date = date(2021,6,15))

#We won't need this anymore so deleting to save some memory
del lines

#Uncomment this to save as a csv as appropriate
df.to_csv(parent + '/data/applicable_trials_2021-06-15.csv', index=False)
# -






# +


