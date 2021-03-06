from django.db import models
import os
from picks.models import games_new, Stand

#

import pandas as pd


data = games_new.objects.all()
# Delete data
data.delete()

data2 = Stand.objects.all()
data2.delete()

pnt = os.getcwd()

df=pd.read_csv('/home/djangodeploy/nflpp2/picks/week2.csv')
df2=pd.read_csv('/home/djangodeploy/nflpp2/picks/week1_stnd.csv')

#print(df)


row_flow = df2.iterrows()

objs2 = [
    Stand(
        player = row['Player'],
        score = row['Score'],

    )

    for index, row in row_flow
]

Stand.objects.bulk_create(objs2)



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
