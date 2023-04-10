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
    rows_number: str
    cols_number: str
    plot_options_list = ['SinglePlot', 'MutiPlot(SubPlot)']
    plot_option: str = 'No selection yet.'

    async def handle_upload(self, file: list[pc.UploadFile]):
        upload_data = []
        for data in file:
            upload_data.append(await data.read())

        df_list = []
        for data in upload_data:
            df = pd.read_table(BytesIO(data), header=None, sep=r'\s+').astype(float)
            df_list.append(df)

        if self.plot_option == 'MutiPlot(SubPlot)':
            form_data = {
                'rows_number': int(self.rows_number),
                'cols_number': int(self.cols_number),
            }
            self.fig = GeneralPlot.line_subplot(df_list, form_data)
        else:
            self.fig = GeneralPlot.line_plot(df_list)
        self.has_fig = True
        self.fig_layout = self.fig._layout

    def set_rows_number(self, n):
        self.rows_number = n

    def set_cols_number(self, n):
        self.cols_number = n

    def set_plot_option(self, option):
        self.plot_option = option


class GeneralPlot:
    @classmethod
    def line_subplot(self, df_list, form_data):
        rows_number = form_data['rows_number']
        cols_number = form_data['cols_number']
        fig = make_subplots(rows=rows_number, cols=cols_number)
        for r in range(rows_number):
            for c in range(cols_number):
                legend = True if (r == 0 and c == 0) else False
                scatter1 = go.Scatter(
                    x=df_list[r + c].iloc[:, 0],
                    y=df_list[r + c].iloc[:, 1],
                    line=dict(color='black'),
                    showlegend=legend,
                    name='Model',
                )
                fig.append_trace(scatter1, r + 1, c + 1)
                # Update xaxis properties
                fig.update_xaxes(
                    showgrid=True,
                    gridwidth=1,
                    gridcolor='rgba(0, 0, 0, 0.2)',
                )
                fig.update_yaxes(
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

    @classmethod
    def line_plot(self, df_list):
        data = []
        for i in range(len(df_list)):
            legend = True
            data.append(
                go.Scatter(
                    x=df_list[i].iloc[:, 0],
                    y=df_list[i].iloc[:, 1],
                    showlegend=legend,
                ),
            )
        fig = go.Figure(data=data)
        # Update xaxis properties
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0, 0, 0, 0.2)',
        )
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0, 0, 0, 0.2)',
        )

        fig.update_layout(
            height=800,
            width=1200,
            plot_bgcolor='rgba(0, 0, 0, 0)',
            legend=dict(y=0.5, traceorder='reversed'),
        )

        return fig
