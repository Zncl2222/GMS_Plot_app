import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State


class MarkovPlotBase(State):
    has_fig: bool = False
    is_progressing: bool = False
    fig: go.Figure = make_subplots()
    fig_title: str = ''
    fig_title_font_size = '30'
    fig_layout: dict = {}
    fig_width: str = '1200'
    fig_height: str = '600'
    x_scale: str = '1'
    x_lim: str = '100'

    _upload_data: list = []
    _df1: list[pd.DataFrame] = []
    _df2: list[pd.DataFrame] = []

    def mk_clean_all(self):
        self._df1 = []
        self._df2 = []
        self._upload_data = []
        self.is_progressing = False

    def set_mk_fig_title_font_size(self, size):
        self.fig_font_size = size

    def set_mk_fig_title(self, title):
        self.fig_title = title

    def set_mk_fig_width(self, width):
        self.fig_width = width

    def set_mk_fig_heigth(self, height):
        self.fig_height = height

    def set_mk_x_scale(self, scale):
        self.x_scale = scale

    def set_mk_x_lim(self, xlim):
        self.x_lim = xlim


class MarkovPlot(MarkovPlotBase):
    async def markov_handle_upload(self, file: list[pc.UploadFile]):
        for data in file:
            self._upload_data.append(await data.read())
        self.is_progressing = True
        return self.markov_data_reading

    async def markov_data_reading(self):
        for data in self._upload_data:
            df = pd.read_table(BytesIO(data), header=None, encoding='UTF16')
            df[2] = df[2].apply(lambda x: np.NaN if str(x).isspace() else x).astype(float)
            df[3] = df[3].apply(lambda x: np.NaN if str(x).isspace() else x).astype(float)
            df = df[(df[2].notna() & df[3].notna())]
            self._df1.append(df[(df[0] == 'Measured Data')])
            self._df2.append(df[(df[0]) == 'Markov Chain'])

        return self.markov_plot()

    def markov_plot(self):
        number = int((len(self._df1)) ** 0.5)
        if number != 0:
            self.fig = make_subplots(rows=number, cols=number)
            for r in range(number):
                for c in range(number):
                    legend = True if (r == 0 and c == 0) else False
                    scatter1 = go.Scatter(
                        x=self._df1[r + c].iloc[:, 2] * float(self.x_scale),
                        y=self._df1[r + c].iloc[:, 3],
                        line=dict(color='black'),
                        showlegend=legend,
                        name='Model',
                    )
                    scatter2 = go.Scatter(
                        x=self._df2[r + c].iloc[:, 2] * float(self.x_scale),
                        y=self._df2[r + c].iloc[:, 3],
                        line=dict(color='red', dash='dash'),
                        showlegend=legend,
                        name='Theory',
                    )
                    self.fig.append_trace(scatter1, r + 1, c + 1)
                    self.fig.append_trace(scatter2, r + 1, c + 1)
                    # Update xaxis properties
                    self.fig.update_xaxes(
                        range=[0, float(self.x_lim)],
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='rgba(0, 0, 0, 0.2)',
                    )
                    self.fig.update_yaxes(
                        range=[0, 1],
                        showgrid=True,
                        gridwidth=1,
                        gridcolor='rgba(0, 0, 0, 0.2)',
                    )

            self.fig.update_layout(
                height=int(self.fig_height),
                width=int(self.fig_width),
                title=dict(
                    text=self.fig_title,
                    font=dict(size=int(self.fig_title_font_size)),
                    automargin=True,
                    yref='paper',
                ),
                plot_bgcolor='rgba(0, 0, 0, 0)',
                legend=dict(y=0.5, traceorder='reversed'),
            )
            self.has_fig = True
            self.fig_layout = self.fig._layout
            return self.mk_clean_all
