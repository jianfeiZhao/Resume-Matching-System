import plotly.graph_objects as go
import pandas as pd
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
import config

"""
same career: salary-location, demand-location
same location: demand-career, salary-career
salary-working experiences, salary-degree
"""
class RelationsPlot:
    def __init__(self):
        self.job_list = config.job_list_salary

    def same_job_diff_loc(self):
        for job in self.job_list:
            job = ''.join(job.split(" ")).replace('/', '')
            df = pd.read_csv('C:/Desktop/BigData_proj/job_analysis/salary_csv/job/{}_salary.csv'.format(job))
            mymap = go.Densitymapbox(lat=df.lat, lon=df.lon, z=df.salary_med)
            fig = go.Figure(mymap)
            token = 'pk.eyJ1IjoiY3N5MTAzMCIsImEiOiJja2NjaXlnZjYwNTJ1Mnluemx1dzlzZnd2In0.5u5tGKbh0fNfzkiij9z6hg'
            fig.update_layout(mapbox={'accesstoken': token, 'center': {'lon': -97.41107, 'lat': 42.03271}, 'zoom': 3.2},
                              margin={'l': 0, 'r': 0, 't': 0, 'b': 0})
            fig.show()

    def same_loc_diff_job(self):
        # for loc in config.location_dict:
        #     item = "_".join(loc.split(",")[0].split(" "))
        #     df = pd.read_csv('./salary_csv/location/{}.csv)'.format(item)

        #loc = 'Chicago'
        #loc = 'New_York_City'
        #loc = 'Seattle'
        #loc = 'San_Francisco'
        loc = 'Austin'
        
        df = pd.read_csv('C:/Desktop/BigData_proj/job_analysis/salary_csv/location/{}.csv'.format(loc))

        bar1 = px.bar(df, x='job', y='salary_med',
                      # text=df['demand'], textposition='outside',
                      labels={'salary_med': 'salary_median',
                              'job': loc,
                              },
                      color='demand',
                      )

        fig = go.Figure(bar1)
        fig.show()


if __name__ == '__main__':
    plot = RelationsPlot()
    #plot.same_job_diff_loc()
    plot.same_loc_diff_job()
