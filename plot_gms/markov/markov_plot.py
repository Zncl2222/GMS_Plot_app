import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State


class MarkovPlotUpload(State):
    fig = make_subplots(rows=1, cols=1)
    fig_layout = {}

    async def handle_upload(self, file: list[pc.UploadFile]):
        upload_data = []
        for data in file:
            upload_data.append(await data.read())

        df1 = []
        df2 = []
        for data in upload_data:
            df = pd.read_table(BytesIO(data), header=None, encoding='UTF16')
            df[2] = df[2].apply(lambda x: np.NaN if str(x).isspace() else x).astype(float)
            df[3] = df[3].apply(lambda x: np.NaN if str(x).isspace() else x).astype(float)
            df = df[(df[2].notna() & df[3].notna())]
            df1.append(df[(df[0] == 'Measured Data')])
            df2.append(df[(df[0]) == 'Markov Chain'])

        self.fig = MarkovPlot.markov_plot(df1, df2)
        self.fig_layout = self.fig._layout


class MarkovPlot:
    @classmethod
    def markov_plot(self, df1, df2):
        number = int((len(df1)) ** 0.5)
        if number != 0:
            fig = make_subplots(rows=number, cols=number)
            for r in range(number):
                for c in range(number):
                    legend = True if (r == 0 and c == 0) else False
                    scatter1 = go.Scatter(
                        x=df1[r + c].iloc[:, 2],
                        y=df1[r + c].iloc[:, 3],
                        line=dict(color='black'),
                        showlegend=legend,
                        name='Model',
                    )
                    scatter2 = go.Scatter(
                        x=df2[r + c].iloc[:, 2],
                        y=df2[r + c].iloc[:, 3],
                        line=dict(color='red', dash='dash'),
                        showlegend=legend,
                        name='Theory',
                    )
                    fig.append_trace(scatter1, r + 1, c + 1)
                    fig.append_trace(scatter2, r + 1, c + 1)
                    # Update xaxis properties
                    fig.update_xaxes(
                        range=[0, 75],
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='rgba(0, 0, 0, 0.2)',
                    )
                    fig.update_yaxes(
                        range=[0, 1],
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='rgba(0, 0, 0, 0.2)',
                    )

            fig.update_layout(
                height=800,
                width=1200,
                title_text='Multiple Subplots with Titles',
                plot_bgcolor='rgba(0, 0, 0, 0)',
                legend=dict(y=0.5, traceorder='reversed'),
            )

            return fig
