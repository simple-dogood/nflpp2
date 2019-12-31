from django.db import models
import os
from picks.models import games_new



import pandas as pd

pnt = os.getcwd()

df=pd.read_csv('/Users/briandougherty/django-sites/nflpp/picks/week2.csv')

#print(df)


row_iter = df.iterrows()



objs = [

    games_new(

        Game_ID = row['Game_ID'],

        Team1  = row['T1'],

        Team2  = row['T2'],

        Spread  = row['Spread'],

        Total = row['Total'],

    )

    for index, row in row_iter

]

games_new.objects.bulk_create(objs)




#Note: myClass_in_model: the class (i.e., the table you want to populate data from csv) we defined in Django model.py
#Note: field_1 to filed_4 are the fields you defined in your Django model.
