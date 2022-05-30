import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.font_manager import FontProperties
from pylab import *


class GMS_Plot:
    
    def ReadData(self):
        a=os.listdir('./static/data')
        a.sort(key = len)
        Z = pd.read_table('./static/data'+'\\'+a[0],header=None,encoding='UTF16',sep='\s+')
        Z = np.zeros((len(a),np.shape(Z)[0],2))
        for i in range(len(a)):
            Y=pd.read_table(filepath+'\\'+a[i],header=None,encoding='UTF16',sep='\s+')
            Z[i,:]=Y.iloc[:,2:4]
        return Z
    
    def ReadData2(self):
        a=os.listdir('./static/data')
        a.sort(key = len)
        Z = pd.read_table('./static/data'+'\\'+a[0],header=None,encoding='UTF16')
        Z = np.zeros((len(a),np.shape(Z)[0],2))

        for i in range(len(a)):
            Y=pd.read_table('./static/data'+'\\'+a[i],header=None,encoding='UTF16')
            Y[2]=Y[2].apply(lambda x: np.NaN if str(x).isspace() else x)
            Y[3]=Y[3].apply(lambda x: np.NaN if str(x).isspace() else x)
            Z[i,:]=Y.iloc[:,2:4]
        return Z

    def Subplot4(self,Z,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break
                
        fig, axes = plt.subplots(4,4, sharex=True, sharey=True,figsize=(15,8))
        print(axes.flatten())
        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0], Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0], Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            
            ax.set_xlim([0, x_max1*ratio])
            #ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        #plt.savefig('./static/images/temp.png',dpi=800)
        plt.savefig('./static/images/GMSPlot.png',dpi=800)

    def Subplot3(self,Z,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break

        fig, axes = plt.subplots(3,3, sharex=True, sharey=True,figsize=(15,8))
        print(axes.flatten())
        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0], Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0], Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==False:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1
        plt.tight_layout()
        plt.savefig('./static/images/GMSPlot.png',dpi=800)


    def Subplot2(self,Z,ratio):

        for i in range(len(Z[0][:,0])):
            if abs(Z[0][i,0]-Z[0][i-1,0])>=20:
                SL=i
            if np.isnan(Z[0][i,0])==True:
                SL2=i
                break
        
        fig, axes = plt.subplots(2,2, sharex=True, sharey=True,figsize=(15,8))


        x1=range(SL)
        x2=range(SL,SL2)
        x_max1=Z[0][SL2-1][0]
        count=0

        for i, ax in enumerate(axes.flatten()):
            ax.plot(Z[count][x1,0]*ratio, Z[count][x1,1],linewidth=2,color='k')
            ax.plot(Z[count][x2,0]*ratio, Z[count][x2,1],linewidth=2,color='r',linestyle='--')
            ax.set_ylim([0, 1])
            if self.cc==False:
                ax.set_xlim([0, x_max1*ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count+=1   

        plt.tight_layout()
        
        plt.savefig('./static/images/GMSPlot.png',dpi=800)
        
        if __name__=='__main__':
            plt.show(block=False)
