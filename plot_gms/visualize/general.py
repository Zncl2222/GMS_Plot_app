import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State
from plot_gms.components.modal import ModalState


class GeneralUpload(State):
    has_fig: bool = False
    plot_state: bool = False
    uploaded_data: list = []
    fig: go.Figure = make_subplots(rows=1, cols=1)
    fig_layout: dict = {}
    rows_number: str
    cols_number: str
    plot_options_list: list = ['SinglePlot', 'MutiPlot(SubPlot)']
    plot_option: str = 'No selection yet.'
    uploaded: str = 'Drag and drop files here or click to select files'
    fig_height: str = '800'
    fig_width: str = '1200'

    async def handle_upload_check(self, file: list[pc.UploadFile]):
        self.plot_state = True
        for data in file:
            self.uploaded_data.append(await data.read())
        if self.plot_option == 'MutiPlot(SubPlot)':
            if int(self.rows_number) * int(self.cols_number) < len(self.uploaded_data):
                self.plot_state = False
                return ModalState.change(
                    'Error',
                    'Rows and Cols of subplot should greater than the uploaded files number',
                )
        return self.handle_upload()

    async def handle_upload(self):
        df_list = []
        for data in self.uploaded_data:
            df = pd.read_table(BytesIO(data), header=None, sep=r'\s+').astype(float)
            df_list.append(df)

        if self.plot_option == 'MutiPlot(SubPlot)':
            form_data = {
                'rows_number': int(self.rows_number),
                'cols_number': int(self.cols_number),
            }
            self.fig = GeneralPlot.line_subplot(df_list, form_data)
        else:
            self.fig = GeneralPlot.line_plot(df_list, int(self.fig_height), int(self.fig_width))
        self.has_fig = True
        self.fig_layout = self.fig._layout
        return self.clean_all

    def clean_all(self):
        self.uploaded_data = []
        self.plot_state = False

    def set_fig_height(self, height):
        self.fig_height = height

    def set_fig_width(self, width):
        self.fig_width = width

    def set_rows_number(self, n):
        self.rows_number = n

    def set_cols_number(self, n):
        self.cols_number = n

    def set_plot_option(self, option):
        self.plot_option = option

    def set_uploaded(self, uploaded):
        self.uploaded = uploaded


class GeneralPlot:
    @classmethod
    def line_subplot(cls, df_list, form_data):
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
    def line_plot(cls, df_list, height, width):
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
            height=height,
            width=width,
            plot_bgcolor='rgba(0, 0, 0, 0)',
            legend=dict(y=0.5, traceorder='reversed'),
        )

        return fig
