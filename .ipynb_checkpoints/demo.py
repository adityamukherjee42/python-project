import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

specs = [[{'type':'pie'}, {"type": "bar"}]]
fig = make_subplots(rows=1, cols=2, specs=specs, shared_yaxes = True, subplot_titles=['Pie Chart', 'Grouped Bar Chart'])

##My data creation##                    
df_pie=pd.DataFrame({'index':[1,2,3,4], 'count':[442,459,289,280]})                    
df_bar=pd.DataFrame({'Satisfaction': ['Excellent', 'Excellent', 'Good', 'Good', 'Poor', 'Poor', 'Neutral', 'Neutral'], 'count': [442, 459, 289, 280, 442, 459, 289, 280], 'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']})                    

fig.add_trace(go.Pie(
                            labels = df_pie['index'], 
                            values = df_pie['count'],
                            hole = 0.6,
                            marker_colors = ['#353837','#646665', '#8e9492', '#c9d1ce'],
                            textinfo='percent+value',  ## ADD - display both
                            ), 1, 1)  

## New column to get percentage of row across all Male/Females
df_bar['percentage'] = df_bar.groupby(['Gender'])['count'].transform(lambda z: round(z / z.sum() * 100))

## New column - text of count and percentage - how you need the annotation shown
df_bar['Text']=df_bar['count'].astype(str) + ',' + df_bar['percentage'].astype(str)+'%'

## Create individual traces for Male and Female
trace1 = go.Bar(
    x=df_bar[df_bar.Gender == 'Male']['Satisfaction'],
    y=df_bar[df_bar.Gender == 'Male']['count'],
    name='Male',
    text=df_bar[df_bar.Gender == 'Male']['Text'], ## Display text
    textposition='auto',
)

trace2 = go.Bar(
    x=df_bar[df_bar.Gender == 'Female']['Satisfaction'],
    y=df_bar[df_bar.Gender == 'Female']['count'],
    name='Female',
    text=df_bar[df_bar.Gender == 'Male']['Text'], ## Display text
    textposition='auto'
)

fig.append_trace(trace1, 1,2) ## Add as first set of bars in second subplot
fig.append_trace(trace2,1,2) ## Add as second set of bars in second subplot

##Removed your original code
#fig.add_trace(go.Bar(
#                        x = df_bar['Satisfaction'],
#                        y = df_bar['count'],
#                        base  =df_bar['Gender'],
#                        ),1,2)

fig.update_layout(showlegend=False, 
                  title=dict(text="Visualization",
                             font=dict(
                                        family="Arial",
                                        size=20,
                                        color='#283747')
                    ))  

fig.show()
