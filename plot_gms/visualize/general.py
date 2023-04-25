import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State
from plot_gms.components.modal import ModalState
from plot_gms.helper import is_numeric
from .base import VisualizeVar


class GeneralUploadBase(State):
    fig: go.Figure = make_subplots()
    has_fig: bool = False
    is_progressing: bool = False
    fig_layout: dict = {}
    fig_title: str = ''
    fig_title_font_size: str = '10'
    fig_height: str = '600'
    fig_width: str = '1200'
    rows_number: str
    cols_number: str

    plot_options_list: list = ['SinglePlot', 'MutiPlot(SubPlot)']
    plot_option: str = 'No selection yet.'
    uploaded: str = 'Drag and drop files here or click to select files'

    _uploaded_data: list = []
    _df_list: list[pd.DataFrame] = []

    def clean_all(self):
        self.has_fig = True
        self.fig_layout = self.fig._layout
        self._uploaded_data = []
        self.is_progressing = False

    def set_fig_title(self, title):
        self.fig_title = title

    def set_fig_title_font_size(self, size):
        self.fig_title_font_size = size

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


class GeneralPlot(GeneralUploadBase):
    async def handle_upload_check(self, file: list[pc.UploadFile]):
        self._uploaded_data = []
        self.is_progressing = True
        for data in file:
            self._uploaded_data.append(await data.read())
        return self.gen_var_validataion

    async def gen_var_validataion(self):
        if self.plot_option == 'MutiPlot(SubPlot)':
            try:
                if int(self.rows_number) * int(self.cols_number) < len(self._uploaded_data):
                    self.is_progressing = False
                    return ModalState.change(
                        'Error',
                        'Rows and Cols of subplot should greater than the uploaded files number !',
                    )
            except ValueError:
                self.is_progressing = False
                return ModalState.change(
                    'Error',
                    'Rows and Cols should be a number !',
                )

        if is_numeric(self.fig_title_font_size) is False:
            self.is_progressing = False
            return ModalState.change('Error', 'Fig title font size should be a number !')
        if is_numeric(self.fig_height) is False:
            self.is_progressing = False
            return ModalState.change('Error', 'Fig height should be a number !')
        if is_numeric(self.fig_width) is False:
            self.is_progressing = False
            return ModalState.change('Error', 'Fig width should be a number !')

        return self.handle_upload

    async def handle_upload(self):
        for data in self._uploaded_data:
            df = pd.read_table(BytesIO(data), header=None, sep=r'\s+').astype(float)
            self._df_list.append(df)
        if self.plot_option == 'MutiPlot(SubPlot)':
            return self.line_subplot
        else:
            return self.line_plot

    def line_plot(self):
        data = []
        for i in range(len(self._df_list)):
            legend = True
            data.append(
                go.Scatter(
                    mode='markers',
                    x=self._df_list[i].iloc[:, 0],
                    y=self._df_list[i].iloc[:, 1],
                    showlegend=legend,
                ),
            )
        self.fig = go.Figure(data=data)
        self.fig.update_traces(
            marker=dict(
                size=12,
                symbol='circle',
                line=dict(
                    width=2,
                    color='DarkSlateGrey',
                ),
            ),
        )
        self.fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0, 0, 0, 0.2)',
        )
        self.fig.update_yaxes(
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
            updatemenus=VisualizeVar.get_update_menu(),
            annotations=VisualizeVar.get_annotations(),
        )
        self.fig.update_layout(
            VisualizeVar.get_slider(),
        )

        return self.clean_all

    def line_subplot(self):
        rows_number = int(self.rows_number)
        cols_number = int(self.cols_number)
        self.fig = make_subplots(rows=rows_number, cols=cols_number)
        for r in range(rows_number):
            for c in range(cols_number):
                legend = True if (r == 0 and c == 0) else False
                scatter1 = go.Scatter(
                    x=self._df_list[r + c].iloc[:, 0],
                    y=self._df_list[r + c].iloc[:, 1],
                    line=dict(color='black'),
                    showlegend=legend,
                    name='Model',
                )
                self.fig.append_trace(scatter1, r + 1, c + 1)
                self.fig.update_xaxes(
                    showgrid=True,
                    gridwidth=1,
                    gridcolor='rgba(0, 0, 0, 0.2)',
                )
                self.fig.update_yaxes(
                    showgrid=True,
                    gridwidth=1,
                    gridcolor='rgba(0, 0, 0, 0.2)',
                )

        self.fig.update_layout(
            height=int(self.fig_height),
            width=int(self.fig_width),
            title_text='Multiple Subplots with Titles',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            legend=dict(y=0.5, traceorder='reversed'),
        )

        return self.clean_all
