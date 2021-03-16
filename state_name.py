import pandas as pd
import numpy as np

def census_and_regions():

    state_names = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        #'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        #'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        #'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        #'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        #'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }
    
    #create list of states and the location of their center of population
    state_census=pd.read_csv('CenPop2010_Mean_ST.txt').iloc[:,1:5]
    for i in state_census.index:
        if not state_census.loc[i,'STNAME'] in state_names:
            state_census.drop(index=i, inplace=True)
    
    abbrev=np.full((state_census.count()[0],1),'na')
    for i in range(state_census.count()[0]):
        try:
            abbrev[i] = state_names[state_census.STNAME[i]]
        except:
            pass
    state_census['ABBREV'] = abbrev;
    state_census=state_census.set_index('ABBREV')
    
    region = {
    'D1':['VT','RI'],
    'D4':['ND','SD'],
    'D8':['MT','WY'],
    'D9':['HI','AK']
    }
    
    region_merge = {
    'D1':['VT','RI'],
    'D4':['ND','SD'],
    'D8':['MT','WY'],
    }
    
    region_sep= {
    'D9':['HI','AK']
    }

    
    return [state_census, region, region_merge, region_sep]




