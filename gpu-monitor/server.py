import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd

import plotly.figure_factory

app = dash.Dash(__name__)

df = pd.read_csv('log.tsv', sep='\t', parse_dates=['query_time'])
gb = df.groupby(['username', 'hostname', 'gpus.index', 'pid']).query_time

df_gantt = pd.concat([gb.min().rename('Start'), gb.max().rename('Finish')], axis=1).reset_index()
df_gantt['Name'] = df_gantt['username'] + '/' + df_gantt['pid'].apply(str)
df_gantt['Task'] = df_gantt['hostname'] + '/' + df_gantt['gpus.index'].apply(str)
df_gantt = df_gantt.sort_values(['hostname', 'gpus.index'])

# import pdb; pdb.set_trace()

fig = plotly.figure_factory.create_gantt(
    df_gantt.to_dict('record'),
    title='GPU Usage',
    index_col='username',
    # show_colorbar=True,
    # group_tasks=True,
    bar_width=0.45,
    showgrid_x=True,
    showgrid_y=True,
    height=900,
    width=1200,
)

annotations = []
for (data, name) in zip(fig['data'], df_gantt['Name']):
    annotations.append(dict(
        x=data['x'][0] + 0.5 * (data['x'][1] - data['x'][0]),
        y=data['y'][0],
        text=name,
        showarrow=False,
    ))

fig['layout']['annotations'] = annotations
# import pdb; pdb.set_trace()

app.layout = dcc.Graph(
    figure=fig,
    id='graph',
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=1337)
