import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
from pylab import FormatStrFormatter
from zipfile import ZipFile

matplotlib.use('Agg')


class markov_chain:
    def ReadData(self):
        a = os.listdir('./static/data')
        a.sort(key=len)
        Z = pd.read_table('./static/data' + '\\' + a[0], header=None, encoding='UTF16')
        self.Z = np.zeros((len(a), np.shape(Z)[0], 2))

        for i in range(len(a)):
            Y = pd.read_table('./static/data' + '\\' + a[i], header=None, encoding='UTF16')
            Y[2] = Y[2].apply(lambda x: np.NaN if str(x).isspace() else x)
            Y[3] = Y[3].apply(lambda x: np.NaN if str(x).isspace() else x)
            self.Z[i, :] = Y.iloc[:, 2:4]

        return self.Z

    def Subplot4(self, ratio):
        plt.clf()
        for i in range(len(self.Z[0][:, 0])):
            if abs(self.Z[0][i, 0] - self.Z[0][i - 1, 0]) >= 20:
                SL = i
            if np.isnan(self.Z[0][i, 0]) is True:
                SL2 = i
                break

        fig, axes = plt.subplots(4, 4, sharex=True, sharey=True, figsize=(15, 8))
        x1 = range(SL)
        x2 = range(SL, SL2)
        x_max1 = self.Z[0][SL2 - 1][0]
        count = 0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(self.Z[count][x1, 0], self.Z[count][x1, 1], linewidth=2, color='k')
            ax.plot(
                self.Z[count][x2, 0],
                self.Z[count][x2, 1],
                linewidth=2,
                color='r',
                linestyle='--',
            )
            ax.set_ylim([0, 1])

            ax.set_xlim([0, x_max1 * ratio])
            # ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count += 1
        plt.tight_layout()
        plt.savefig('./static/images/GMSPlot.png', dpi=800)

    def Subplot3(self, ratio):
        plt.clf()
        for i in range(len(self.Z[0][:, 0])):
            if abs(self.Z[0][i, 0] - self.Z[0][i - 1, 0]) >= 20:
                SL = i
            if np.isnan(self.Z[0][i, 0]) is True:
                SL2 = i
                break

        fig, axes = plt.subplots(3, 3, sharex=True, sharey=True, figsize=(15, 8))

        x1 = range(SL)
        x2 = range(SL, SL2)
        x_max1 = self.Z[0][SL2 - 1][0]
        count = 0
        for i, ax in enumerate(axes.flatten()):
            ax.plot(self.Z[count][x1, 0], self.Z[count][x1, 1], linewidth=2, color='k')
            ax.plot(
                self.Z[count][x2, 0],
                self.Z[count][x2, 1],
                linewidth=2,
                color='r',
                linestyle='--',
            )
            ax.set_ylim([0, 1])

            ax.set_xlim([0, x_max1 * ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count += 1
        plt.tight_layout()
        plt.savefig('./static/images/GMSPlot.png', dpi=800)

    def Subplot2(self, ratio):
        plt.clf()
        for i in range(len(self.Z[0][:, 0])):
            if abs(self.Z[0][i, 0] - self.Z[0][i - 1, 0]) >= 20:
                SL = i
            if np.isnan(self.Z[0][i, 0]) is True:
                SL2 = i
                break

        fig, axes = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(15, 8))

        x1 = range(SL)
        x2 = range(SL, SL2)
        x_max1 = self.Z[0][SL2 - 1][0]
        count = 0

        for i, ax in enumerate(axes.flatten()):
            ax.plot(self.Z[count][x1, 0] * ratio, self.Z[count][x1, 1], linewidth=2, color='k')
            ax.plot(
                self.Z[count][x2, 0] * ratio,
                self.Z[count][x2, 1],
                linewidth=2,
                color='r',
                linestyle='--',
            )
            ax.set_ylim([0, 1])

            ax.set_xlim([0, x_max1 * ratio])
            ax.yaxis.set_major_formatter(FormatStrFormatter('%1.1f'))
            plt.setp(ax.get_xticklabels(), fontsize=16)
            plt.setp(ax.get_yticklabels(), fontsize=16)
            count += 1

        plt.tight_layout()

        plt.savefig('./static/images/GMSPlot.png', dpi=800)


class semivariance(markov_chain):
    def __init__(self, x_unit, x_notation):
        self.x_unit = x_unit
        self.x_notation = x_notation

    def semi_plot(self, ratio):

        for i in range(len(self.Z[0][:, 0])):
            if np.isnan(self.Z[0][i, 0]) is True and np.isnan(self.Z[0][i - 1, 0]) is False:
                SL = i
            if np.isnan(self.Z[0][i, 0]) is True and np.isnan(self.Z[0][i + 1, 0]) is False:
                SL2 = i
                break
        x1 = range(SL)
        x2 = range(SL2, len(self.Z[0][:]))

        angle = []
        for i in range(1, 13):
            n = i * 15
            angle.append(str(n))

        for i in range(len(self.Z)):
            plt.plot(
                self.Z[i][x1, 0] * ratio,
                self.Z[i][x1, 1],
                linewidth=2,
                color='k',
                label='Model',
            )
            plt.plot(
                self.Z[i][x2, 0] * ratio,
                self.Z[i][x2, 1],
                linewidth=2,
                color='r',
                linestyle='--',
                label='Theory',
            )
            plt.xticks(fontsize=18)
            plt.yticks(fontsize=18)
            plt.legend(fontsize=18)
            plt.ylabel('Semi-variance', fontsize=24)
            plt.xlabel('Lag distance [' + self.x_unit + ']', fontsize=24)
            plt.title('Angle = ' + angle[i] + '$degree$', fontsize=18)
            plt.ticklabel_format(
                style=self.x_notation,
                axis='x',
                scilimits=(0, 0),
                useMathText=True,
                useOffset=False,
            )
            plt.rc('font', size=17)
            plt.grid(alpha=0.25)
            plt.tight_layout()
            plt.savefig('./static/images/semivariance' + str(i) + '.png', dpi=500)
            plt.clf()

        zip_file = ZipFile('./static/semivariance_plot.zip', 'w')
        for i in range(len(self.Z)):
            zip_file.write('./static/images/semivariance' + str(i) + '.png')
        zip_file.close()
