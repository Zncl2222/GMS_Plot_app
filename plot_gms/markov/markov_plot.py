import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pynecone as pc
from io import BytesIO
from plot_gms.state import State


class MarkovPlot(State):
    img: str

    async def handle_upload(self, file: pc.UploadFile):
        """Handle the upload of a file.

        Args:
            file: The uploaded file.
        """
        upload_data = await file.read()
        df = pd.read_table(BytesIO(upload_data), header=None, encoding='UTF16')
        df[2] = df[2].apply(lambda x: np.NaN if str(x).isspace() else x)
        df[3] = df[3].apply(lambda x: np.NaN if str(x).isspace() else x)
        Z = np.zeros((1, np.shape(df)[0], 2))
        Z[0, :] = df.iloc[:, 2:4]
        for i in range(len(Z[0][:, 0])):
            if abs(Z[0][i, 0] - Z[0][i - 1, 0]) >= 20:
                SL = i
            if np.isnan(Z[0][i, 0]) is True:
                SL2 = i
                break

        x1 = range(SL)
        x2 = range(SL, SL2)
        count = 0

        plot(Z, x1, x2, count)


def plot(df, x1, x2, count):
    fig = make_subplots(rows=1, cols=2)
    scatter1 = go.Scatter(x=df[count][x1, 0], y=df[count][x1, 1])
    scatter2 = go.Scatter(x=df[count][x2, 0], y=df[count][x2, 1])
    fig.append_trace(scatter1, 1, 1)
    fig.append_trace(scatter2, 1, 2)

    fig.update_layout(
        height=500,
        width=700,
        title_text='Multiple Subplots with Titles',
    )
    fig.show()


# class markov_chain(pc.State):

#     def ReadData(self):
#         a=os.listdir('./static/data')
#         a.sort(key = len)
#         Z = pd.read_table('./static/data'+'\\'+a[0],header=None,encoding='UTF16')
#         self.Z = np.zeros((len(a),np.shape(Z)[0],2))

#         for i in range(len(a)):
#             Y=pd.read_table('./static/data'+'\\'+a[i],header=None,encoding='UTF16')
#             Y[2]=Y[2].apply(lambda x: np.NaN if str(x).isspace() else x)
#             Y[3]=Y[3].apply(lambda x: np.NaN if str(x).isspace() else x)
#             self.Z[i,:]=Y.iloc[:,2:4]

#         return self.Z

#     def plot(self):
#         a=os.listdir('./static/data')
#         a.sort(key = len)
#         Z = pd.read_table('./static/data'+'\\'+a[0],header=None,encoding='UTF16')
#         self.Z = np.zeros((len(a),np.shape(Z)[0],2))

#         for i in range(len(a)):
#             Y=pd.read_table('./static/data'+'\\'+a[i],header=None,encoding='UTF16')
#             Y[2]=Y[2].apply(lambda x: np.NaN if str(x).isspace() else x)
#             Y[3]=Y[3].apply(lambda x: np.NaN if str(x).isspace() else x)
#             self.Z[i,:]=Y.iloc[:,2:4]
#         for i in range(len(self.Z[0][:,0])):
#             if abs(self.Z[0][i,0]-self.Z[0][i-1,0])>=20:
#                 SL=i
#             if np.isnan(self.Z[0][i,0])==True:
#                 SL2=i
#                 break

#         x1=range(SL)
#         x2=range(SL,SL2)
#         x_max1=self.Z[0][SL2-1][0]
#         count=0
#         # fig = make_subplots(rows=2, cols=1, start_cell="bottom-left")
#         fig = tools.make_subplots(rows=1, cols=2)
#         fig.append_trace(go.Scatter(x=self.Z[count][x1,0], y=self.Z[count][x1,1]), 1, 1)
#         fig.append_trace(go.Scatter(x=self.Z[count][x2,0], y=self.Z[count][x2,1]), 1, 2)

#         # fig.add_trace(go.Scatter(x=self.Z[count][x1,0], y=self.Z[count][x1,1]), row=1, col=1)
#         # fig.add_trace(go.Scatter(x=self.Z[count][x2,0], y=self.Z[count][x2,1]), row=2, col=1)
#         fig.update_layout(height=500, width=700,
#                   title_text="Multiple Subplots with Titles")

#         fig.show()
