import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State


class GeneralUpload(State):
    has_fig = False
    fig = make_subplots(rows=1, cols=1)
    fig_layout = {}

    async def handle_upload(self, file: list[pc.UploadFile]):
        upload_data = []
        for data in file:
            upload_data.append(await data.read())

        df_list = []
        for data in upload_data:
            df = pd.read_table(BytesIO(data), header=None)
            df_list.append(df)
        self.fig = GeneralPlot.plot(df_list)
        self.fig_layout = self.fig._layout


class GeneralPlot:
    @classmethod
    def plot(self, df_list):
        number = int((len(df_list)) ** 0.5)
        if number != 0:
            fig = make_subplots(rows=number, cols=number)
            for r in range(number):
                for c in range(number):
                    legend = True if (r == 0 and c == 0) else False
                    scatter1 = go.Scatter(
                        x=df_list[r + c].iloc[:, 2],
                        y=df_list[r + c].iloc[:, 3],
                        line=dict(color='black'),
                        showlegend=legend,
                        name='Model',
                    )
                    fig.append_trace(scatter1, r + 1, c + 1)
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
