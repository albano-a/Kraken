import pandas as pd
import os
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Interface.pyInterface.plot_ui import Ui_SimplePlotWindow
from Functions.general import timing_function


class SimplePlotWindow(QMainWindow, Ui_SimplePlotWindow):
    def __init__(self):
        super(SimplePlotWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plot Simples")
        # Initialize self.selected_file
        self.selected_file = None

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir("src/uploads")
        self.selectFileComboBox.addItems(self.files)

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.headerSim.toggled.connect(self.on_headerSim_toggled)

        self.lineColorComboBox.addItems(
            [
                "blue",
                "red",
                "green",
                "yellow",
                "black",
                "purple",
                "orange",
                "pink",
                "brown",
                "gray",
            ]
        )

        # plot btn
        self.simplePlotBtn.clicked.connect(self.call_plot_simple)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_simple_plotting(self):
        try:
            self.mesa_rotativa = self.inputMesaRotativa.text()
            self.header_lines = self.inputHeaderLines.text()

            self.selected_file = self.selectFileComboBox.currentText()
            # Verifica se self.header_lines não é uma string vazia
            if self.header_lines != "":
                # Tenta converter self.header_lines para um inteiro
                try:
                    skiprows = int(self.header_lines)
                except ValueError:
                    QMessageBox.critical(self, "Error", "Wrong header lines!")
                    return pd.DataFrame()
            else:
                skiprows = 0

            # Obtém o texto do botão marcado no fileButtonGroup
            self.file_type_button_text = self.fileButtonGroup.checkedButton().text()

            if self.file_type_button_text == "csv":
                try:
                    dataframe = pd.read_csv(
                        f"uploads/{self.selected_file}",
                        delimiter="[;,]",
                        names=["prof", "pressao"],
                        engine="python",
                        skiprows=skiprows,
                    )
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"There was an error: {e}")
                    return pd.DataFrame()

            elif self.file_type_button_text == "txt":
                try:
                    dataframe = pd.read_csv(
                        f"uploads/{self.selected_file}",
                        skiprows=skiprows,
                        delimiter="\t",
                        names=["prof", "pressao"],
                        engine="python",
                    )
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"There was an error: {e}")
                    return pd.DataFrame()

            elif self.file_type_button_text == "xlsx":
                try:
                    dataframe = pd.read_excel(
                        f"uploads/{self.selected_file}",
                        skiprows=skiprows,
                        names=["prof", "pressao"],
                    )
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"There was an error: {e}")
                    return pd.DataFrame()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"There was an error: {e}")
            return pd.DataFrame()

    def plot_simple(self, x, y, title, xlabel, ylabel, ymin, ymax):
        self.selected_color = self.lineColorComboBox.currentText()

        if self.mesa_rotativa != "":
            try:
                y = int(self.mesa_rotativa) - y
            except ValueError:
                QMessageBox.critical(self, "Error", "Wrong rotary table value")
                return
        try:
            ymin = int(self.prof_min) if self.prof_min != "" else None
            ymax = int(self.prof_max) if self.prof_max != "" else None

        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid depth values!")
            return

        try:
            # Obtém o texto do botão marcado no cotaButtonGroup
            cota_button_text = self.cotaButtonGroup.checkedButton().text()

            if cota_button_text != "Yes" or cota_button_text != "No":
                QMessageBox.critical(self, "Error", "Yes or No not selected!")

            if cota_button_text == "Yes":
                plt.plot(x, y, "o", color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                plt.show()
                print("plotted")

            elif cota_button_text == "No":
                plt.plot(x, y, "o", color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                    plt.gca().invert_yaxis()
                plt.show()
                print("plotted")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"There was an error in the plot: {e}")

    @timing_function
    def call_plot_simple(self):
        self.dataframe = self.open_file_for_simple_plotting()
        self.title = self.inputPlotTitle.text()
        self.x_axis = self.inputPlotXAxis.text()
        self.y_axis = self.inputPlotYAxis.text()
        self.prof_min = self.inputProfMin.text()
        self.prof_max = self.inputProfMax.text()
        print(self.dataframe, self.title, self.x_axis, self.y_axis)

        # Check if the inputs are provided
        if not self.title or not self.x_axis or not self.y_axis:
            QMessageBox.critical(self, "Error", "All inputs must be provided.")
            return

        if self.dataframe.empty:
            QMessageBox.critical(self, "Error", "The dataframe is empty.")
            return

        # Try to create the plot and catch any errors
        try:
            self.plot_simple(
                self.dataframe.iloc[:, 1],
                self.dataframe.iloc[:, 0],
                self.title,
                self.x_axis,
                self.y_axis,
                self.prof_min,
                self.prof_max,
            )
            print("Plotting...")
        except Exception as e:
            QMessageBox.critical(
                self, "Error", f"An error occurred while creating the plot: {str(e)}"
            )