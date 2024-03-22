# Standard library imports #
import os
import shutil
from os.path import normpath
import csv
import io
from textwrap import fill
import subprocess
# Related third party imports #
from tkinter import scrolledtext
from sklearn.cluster import KMeans # entender o porque desse import
from click import command
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
import webbrowser
from tksheet import Sheet
from tkinter import filedialog, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pygments.lexers
from pygments.styles import get_style_by_name
from numpy.linalg import inv
from CTkMenuBar import *
from CTkMessagebox import CTkMessagebox
from CTkToolTip import CTkToolTip
from ttkwidgets.font import *
# Local application/library specific imports #
from components.about import AboutPage
from components.help_window import HelpWindow
from components.tomi_calculations import TOMICalc
from chlorophyll import CodeView
from utility.icons import (add_img, remove_img, font_img, show_plot_img,
                           inventory_img, code_img, folder_img, save_img, new_file_img)
from utility.utilities import (create_custom_button, custom_dropdown,
                               centralize_window, custom_CTkEntry,
                               update_and_centralize_geometry, placeholder_function,
                               custom_messagebox, custom_tooltip)
from utility.color_constants import (TEXT_COLOR, BORDER_COLOR, BTN_FG_COLOR, ENTRY_COLOR,
                             BTN_FG_HOVER_COLOR, FG_COLOR_OUT, FG_COLOR_IN, FG_COLOR_IN2)
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

# GLOBAL VARIABLES
GIECAR_URL = "http://gcr.sites.uff.br/"
GITHUB_URL = "https://github.com/albano-a/GradPress"
SMALL_WINDOW_SIZE = (300, 200)

class NewWindow(tk.Toplevel):
    """
    A class used to create a new window in a tkinter application.

    Attributes
    ----------
    app : object
        an instance of the main application class
    menu_bar : object
        an instance of the MenuBar class

    Methods
    -------
    __init__(self, master=None, app=None)
        Initializes the NewWindow instance and configures the menu bar.
    """
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.app = app
        self.menu_bar = MenuBar(self, self.app)
        self.config(menu=self.menu_bar.menu_bar)

class FilesFrame(ctk.CTkScrollableFrame):
    """
    A class used to create a scrollable frame that displays a list of files.

    Attributes
    ----------
    files : list
        A list of file names in the './uploads' directory.
    listbox : object
        The listbox widget that displays the file names.

    Methods
    -------
    __init__(self, master, **kwargs)
        Initializes the FilesFrame instance and sets up the listbox and scrollbar.
    on_select(self, event)
        Handles the event when a file is selected in the listbox.
    add_file(self)
        Opens a file dialog to select a file to add to the listbox.
    rename_file(self)
        Renames the selected file.
    delete_file(self)
        Deletes the selected file.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # List all files in ./uploads
        self.files = os.listdir("./uploads")

        listbox_frame = tk.Frame(self, bg='#ebebeb')
        listbox_frame.grid(row=0, column=0, padx=10, pady=10)

        self.listbox = tk.Listbox(listbox_frame, width=400, height=200, font=("Segoe UI", 15))
        self.listbox.grid(row=0, column=0, sticky='nsew')  # Use grid instead of pack
        for file in self.files:
            self.listbox.insert(tk.END, file)

        # Create a scrollbar and attach it to the listbox
        scrollbar = ctk.CTkScrollbar(listbox_frame, command=self.listbox.yview, corner_radius=5, fg_color="#f7f7f7")
        scrollbar.grid(row=0, column=1, sticky='ns')  # Use grid instead of pack
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        # Get selected file
        index = self.listbox.curselection()[0]
        selected_file = self.files[index]

    def add_file(self):
        filename = filedialog.askopenfilename()
        if filename:  # Check if a file was selected
            if not os.path.exists("./uploads"):
                os.makedirs("./uploads")
            shutil.copy(filename, "./uploads")
            new_file = os.path.basename(filename)
            self.listbox.insert(tk.END, new_file)
            self.files.append(new_file)  # Update the files list
            custom_messagebox(title="Sucesso", message="Arquivo carregado com sucesso!",
                          icon="./img/icons/check.png", option_1="OK", width=400)

    def rename_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            new_name = tk.simpledialog.askstring("Input", "Novo nome:", parent=self.master)
            if new_name:
                new_path = os.path.join("./uploads", new_name)
                if not os.path.exists(new_path):  # Check if the new file name already exists
                    shutil.move(os.path.join("./uploads", selected_file), new_path)
                    self.listbox.delete(index)
                    self.listbox.insert(index, new_name)
                    self.files[index] = new_name  # Update the files list
                    custom_messagebox(title="Sucesso", message="Arquivo renomeado com sucesso!",
                                  icon="./img/icons/check.png", option_1="OK", width=400)
                else:
                    custom_messagebox(title="Aviso!", message="Esse nome já existe!",
                                  icon="./img/icons/warning.png", option_1="OK", width=400)

    def delete_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            os.remove(os.path.join("./uploads", selected_file))
            self.listbox.delete(index)
            del self.files[index]  # Update the files list
            custom_messagebox(title="Sucesso", message="Arquivo deletado com sucesso!",
                          icon="./img/icons/check.png", option_1="OK", width=400)

class ManageFilesWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_manage_window(self):
        self.manage_window = NewWindow(self.master, self.app)
        self.manage_window.title("Gerenciar arquivos")
        centralize_window(self.manage_window, 600, 500)
        self.manage_window.geometry("600x500")
        self.manage_window.minsize(600, 500)
        self.manage_window.option_add("*Label.font", "Helvetica 15")  # for the font

        # Create a frame within the new window
        self.manage_files_frame = tk.Frame(self.manage_window)
        self.manage_files_frame.grid(row=0, column=0, padx=5, pady=5)
        self.manage_files_frame.place(relx=0.5, rely=0.5, anchor='center')

        # label for the title
        gerenciar_texto = "Gerenciar arquivos"
        self.label = ctk.CTkLabel(self.manage_files_frame, text=gerenciar_texto, font=("Helvetica", 20, "bold"))
        # frame for the list of files
        self.files_frame = FilesFrame(self.manage_files_frame, width=500, height=300, fg_color="transparent")
        # buttons for managing files
        # add btn
        self.add_btn = create_custom_button(self.manage_files_frame, text="Adicionar", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.add_file, width=75, fg_color="#28a745",
                                            hover_color="#1f7f35", text_color="#212121")
        # rename btn
        self.rnm_btn = create_custom_button(self.manage_files_frame, text="Renomear", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.rename_file, width=75, fg_color="#ffc107",
                                            hover_color="#d19d00", text_color="#212121")
        # delete btn
        self.del_btn = create_custom_button(self.manage_files_frame, text="Deletar", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.delete_file, width=75, fg_color="#dc3545",
                                            hover_color="#bf2231", text_color="#212121")
        # return btn
        self.return_btn = create_custom_button(self.manage_files_frame, text="Voltar", font=("Segoe UI", 18, "bold"),
                                               command=self.manage_window.destroy, width=75,fg_color="#17a2b8",
                                               hover_color="#117c8d", text_color="#212121")

        self.label.grid(      row=0, column=0, columnspan=4, padx=10, pady=10)
        self.files_frame.grid(row=1, column=0, columnspan=4,padx=5, pady=5)
        self.add_btn.grid(    row=2, column=0, padx=5, pady=5)
        self.rnm_btn.grid(    row=2, column=1, padx=5, pady=5)
        self.del_btn.grid(    row=2, column=2, padx=5, pady=5)
        self.return_btn.grid( row=2, column=3, padx=5, pady=5)

class CalculationsWindow:
    width=250
    height=15
    border_width=1.2

    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_calculations_window(self):
        self.cal_window = tk.Toplevel(self.master)
        self.cal_window.attributes('-toolwindow', True)

        self.cal_window.grab_set()

        self.cal_window.title("Calculadora")
        # self.cal_window.minsize(600, 600)
        self.cal_window.option_add("*Label.font", "Segoe\\ UI 12")

        # centralize_window(self.cal_window, 800, 600)

        # TODO: Trocar isso por ttk.Notebook
        self.sup_frame_tab = ttk.Notebook(self.cal_window)
        self.sup_frame_tab.bind("<Configure>", \
            lambda event: update_and_centralize_geometry(self.cal_window, self.sup_frame_tab,
                                                         max_size=True, child_window=True))
        self.sup_frame_tab.place(relx=0.5, rely=0.5, anchor='center')

        # tabs
        self.calc_tab_0 = ctk.CTkFrame(self.sup_frame_tab, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN2, border_width=self.border_width,width=self.width)
        self.calc_tab_1 = ctk.CTkFrame(self.sup_frame_tab, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN2, border_width=self.border_width, width=self.width)
        self.calc_tab_2 = ctk.CTkFrame(self.sup_frame_tab, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN2, border_width=self.border_width, width=self.width)

        # Add the tabs to the tab control
        self.sup_frame_tab.add(self.calc_tab_0, text='Plotagem simples')
        self.sup_frame_tab.add(self.calc_tab_1, text='Linhas de Tendência')
        self.sup_frame_tab.add(self.calc_tab_2, text='Gradiente de Pressão')

        # Pack the tab control
        self.sup_frame_tab.pack(expand=1, fill="both")

        self.plot_first_tab(self.calc_tab_0)
        self.second_tab(self.calc_tab_1)
        # self.third_tab(self.calc_tab_2)

        # self.calc_tab_0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_tab_1.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_tab_2.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_tab_3.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_tab_4.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        # self.calc_tab_0 is the whole frame of the first tab

    def plot_first_tab(self, tab, width=width, height=height, border_width=border_width):

        # Defining the 8 frames
        def frames_calc(self):
            self.plot_tab_frames = [ctk.CTkFrame(tab, corner_radius=1, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN2, border_width=border_width)
                                    for _ in range(8)]

            self.plot_tab_frames[0].grid(row=1, column=0, rowspan=1,
                                        columnspan=2, padx=5, pady=5, sticky='nsew') # TextBox, title
            self.plot_tab_frames[1].grid(row=2, column=0, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew') # prof max and min
            self.plot_tab_frames[2].grid(row=2, column=1, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew') #
            self.plot_tab_frames[3].grid(row=3, column=0, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew') # Radio buttons
            self.plot_tab_frames[4].grid(row=3, column=1, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew')
            self.plot_tab_frames[5].grid(row=4, column=0, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew')
            self.plot_tab_frames[6].grid(row=4, column=1, rowspan=1,
                                        columnspan=1, padx=5, pady=5, sticky='nsew')
            self.plot_tab_frames[7].grid(row=5, column=0, rowspan=1,
                                        columnspan=2, padx=5, pady=5, sticky='nsew')

        frames_calc(self)

        self.calculator_text_label = \
            "Plotagem Simples"
        self.calculator_text = ctk.CTkLabel(self.plot_tab_frames[0],
                                            text=self.calculator_text_label,
                                            font=("Segoe UI", 14, "bold"),
                                            justify="center",
                                            width=width, height=height)
        self.calculator_text.pack(fill='x', expand=True, padx=5, pady=5)

        self.calculator_text_label = \
            "Preencha os campos abaixo para gerar um \n gráfico do dado bruto ou tratado."
        self.calculator_text = ctk.CTkLabel(self.plot_tab_frames[0],
                                            text=self.calculator_text_label,
                                            font=("Segoe UI", 12),
                                            justify="center",
                                            width=width, height=height)
        self.calculator_text.pack(fill='x', expand=True, padx=5, pady=5)

        #----------------------------- Frame 1 -------------------------------------------
        # File dropdown menu frame
        # Logica para o menu dropdown
        self.file_dialog_standard(self.plot_tab_frames[1])

        #------------------------------ Frame 2 ----------------------------------------------------
        # Frame for prof_min
        self.prof_min_Frame = ctk.CTkFrame(self.plot_tab_frames[3], fg_color="transparent") # FRAME
        self.prof_min_Label = ctk.CTkLabel(self.prof_min_Frame, text="Prof. min:", font=("Segoe UI", 16), height=height)
        self.prof_min_entry = custom_CTkEntry(self.prof_min_Frame,
                                              placeholder_text="Prof. mínima...")
        custom_tooltip(self.prof_min_entry, "Insira a profundidade mínima se quiser plotar um intervalo", delay=1)

        self.prof_min_Frame.pack(side='top', fill='both', padx=5, pady=5)
        self.prof_min_Label.pack(side='left', padx=5, pady=5)
        self.prof_min_entry.pack(fill='x', expand=True, side='left', padx=5, pady=5)

        # Frame for prof_max
        self.prof_max_frame = ctk.CTkFrame(self.plot_tab_frames[3], fg_color="transparent")
        self.prof_max_label = ctk.CTkLabel(self.prof_max_frame, text="Prof. max:", font=("Segoe UI", 16), height=height)
        self.prof_max_entry = custom_CTkEntry(self.prof_max_frame,
                                              placeholder_text="Prof. máxima...")
        custom_tooltip(self.prof_max_entry, "Insira a profundidade máxima se quiser plotar um intervalo", delay=1)

        self.prof_max_frame.pack(side='top', fill='x', padx=5, pady=5)
        self.prof_max_label.pack(side='left', padx=5, pady=5)
        self.prof_max_entry.pack(fill='x', expand=True, side='left', padx=5, pady=5)

        #---------------------------- Frame 3 --------------------------------------------------------
        #------------------------ Radio Button Frame -------------------------------------------------
        self.radiobtn_frame = ctk.CTkFrame(self.plot_tab_frames[2],
                                           fg_color="transparent",
                                           height=height)
        self.radiobtn_frame.pack(side="left", padx=5, pady=5)

        self.prof_cota_var = tk.StringVar()
        self.prof_cota_ou_nao = ctk.CTkLabel(self.radiobtn_frame, text="Cota?: ",
                                                font=("Segoe UI", 12))
        self.prof_cota_ou_nao.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.prof_cota_radio_y = ctk.CTkRadioButton(self.radiobtn_frame,
                                                    command=self.radiobutton_event,
                                                    variable=self.prof_cota_var,
                                                    value="Sim",
                                                    text="Sim")
        self.prof_cota_radio_y.grid(row=1, column=0, padx=5, pady=5)

        self.prof_cota_radio_n = ctk.CTkRadioButton(self.radiobtn_frame,
                                                    command=self.radiobutton_event,
                                                    variable=self.prof_cota_var,
                                                    value="Não",
                                                    text="Não")
        self.prof_cota_radio_n.grid(row=1, column=1, padx=5, pady=5)
        ############## Mesa Rotatoria
        self.mesa_rot_frame = ctk.CTkFrame(self.plot_tab_frames[4],
                                                fg_color="transparent",
                                                height=height)
        self.mesa_rot_frame.pack(side="right", padx=5, pady=5)

        self.mesa_rot_label = ctk.CTkLabel(self.mesa_rot_frame,
                                        text="Mesa Rotativa: ",
                                        height=height,
                                        font=("Segoe UI", 16))
        self.mesa_rot_label.pack(side="top", padx=5, pady=5)

        self.mesa_rot_entry = custom_CTkEntry(self.mesa_rot_frame,
                                                placeholder_text="Insira aqui...")
        self.mesa_rot_entry.pack(side="bottom", expand=True, padx=5, pady=5)

        custom_tooltip(
                self.mesa_rot_entry,
                "Mesa Rotativa se refere à distância entre a superfície do oceano"\
                "(ou nível do solo para poços terrestres) até uma certa profundidade,"\
                "calculada usando o valor de altura da mesa rotativa.",
                delay=1
            )
        #------------------------ Frame 4 -------------------------------------------------
        # title and skiprows frame
        self.plot_title = ctk.CTkLabel(self.plot_tab_frames[5], text="Nome do Poço: ",
                                            font=("Segoe UI", 16), height=height)

        self.plot_title_entry = custom_CTkEntry(self.plot_tab_frames[5], width=200,
                                                    placeholder_text="Insira aqui...")
        custom_tooltip(self.plot_title_entry, "Insira um título para o gráfico", delay=1)

        self.skip_rows = ctk.CTkLabel(self.plot_tab_frames[5], text="Header?: ",
                                        font=("Segoe UI", 16), height=height)

        self.skip_rows_entry = custom_CTkEntry(self.plot_tab_frames[5], width=200,
                                               placeholder_text="Insira aqui...")
        custom_tooltip(self.skip_rows_entry,
                       "Quantas linhas pular do arquivo carregado.\n Para evitar plotagem de palavras",
                       delay=1)

        self.plot_title.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.plot_title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.skip_rows.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.skip_rows_entry.grid(row=1, column=1, padx=5, pady=5)

        #------------------------------------ axis frame ------------------------------------

        self.x_label = ctk.CTkLabel(self.plot_tab_frames[6],
                                        text="Eixo x: ",
                                        font=("Segoe UI", 16),
                                        height=height)
        self.x_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.x_label_entry = custom_CTkEntry(self.plot_tab_frames[6],
                                                width=200,
                                                placeholder_text="Insira aqui...")
        self.x_label_entry.grid(row=0, column=1, padx=5, pady=5)
        custom_tooltip(
                self.x_label_entry,
                "Insira o nome do eixo x, por exemplo: Pressão",
                delay=1
            )

        self.y_label = ctk.CTkLabel(self.plot_tab_frames[6],
                                        text="Eixo y: ",
                                        font=("Segoe UI", 16),
                                        height=height)
        self.y_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.y_label_entry = custom_CTkEntry(self.plot_tab_frames[6],
                                                width=200,
                                                placeholder_text="Insira aqui...")
        self.y_label_entry.grid(row=1, column=1, padx=5, pady=5)
        custom_tooltip(
                self.y_label_entry,
                "Insira o nome do eixo y, por exemplo: Profundidade",
                delay=1
            )

        #------------------------------------ Plot btn ------------------------------------
        self.calc_btn = create_custom_button(root=self.plot_tab_frames[7],
                                            text="Plotar",
                                            command=self.call_plot_simple,
                                            width=200)
        self.calc_btn.pack(side="top", padx=5, pady=5)

    def second_tab(self, tab, width=220, height=height, border_width=border_width):

        # Defining the frames
        self.second_tab_frames = [ctk.CTkFrame(tab, corner_radius=1,border_color=BORDER_COLOR,
                                fg_color=FG_COLOR_IN2, border_width=border_width)
                                for _ in range(4+1)]

        tab.columnconfigure((0,1), weight=1)
        tab.rowconfigure((0,1,2,3,4), weight=1)

        self.second_tab_frames[0].grid(row=0, column=0, rowspan=1, columnspan=2,
                                       padx=5, pady=5, sticky='nsew')
        self.second_tab_frames[1].grid(row=1, column=0, rowspan=2, columnspan=2,
                                       padx=5, pady=5, sticky='nsew')
        self.second_tab_frames[2].grid(row=3, column=0, rowspan=1, columnspan=1,
                                       padx=5, pady=5, sticky='nsew')
        self.second_tab_frames[3].grid(row=3, column=1, rowspan=1, columnspan=1,
                                       padx=5, pady=5, sticky='nsew')
        self.second_tab_frames[4].grid(row=4, column=0, rowspan=1, columnspan=2,
                                       padx=5, pady=5, sticky='nsew')

        self.linha_tendencia_text_label = \
        "Linhas de Tendência e Identificação de Contato óleo-água"
        self.linha_tendencia_text = ctk.CTkLabel(self.second_tab_frames[0],
                                                text=self.linha_tendencia_text_label,
                                                font=("Segoe UI", 14, "bold"),
                                                justify="center",
                                                width=width, height=height)
        self.linha_tendencia_text_label2 = \
        "Preencha os campos abaixo para plotar as linhas de tendência. \n" + \
        "Kmeans Cluster indica em quantas partes você quer dividir o parâmetro \n" + \
        "para calcular as linhas de tendência."
        self.linha_tendencia_text2 = ctk.CTkLabel(self.second_tab_frames[0],
                                            text=self.linha_tendencia_text_label2,
                                            font=("Segoe UI", 12),
                                            justify="center",
                                            width=width, height=height)

        self.linha_tendencia_text.pack(fill='x', expand=True, padx=5, pady=5)
        self.linha_tendencia_text2.pack(fill='x', expand=True, padx=5, pady=5)

        ####### Frame 2
        self.file_dialog_standard(self.second_tab_frames[1])

        ####### Frame 3 - Pressure input
        self.pressure_units = ["psi/ft", "psi/m", "Kgf/cm2/m", "bar/m"]
        self.pressure_choice = tk.StringVar()
        self.pressure_choice.set(self.pressure_units[0])

        self.press_label = ctk.CTkLabel(self.second_tab_frames[2],
                                text="Unidade da pressão: ",
                                font=("Segoe UI", 16),
                                width=width, height=height)
        self.press_label.pack(fill='both', padx=5, pady=5)

        self.press_option_menu = ctk.CTkOptionMenu(
                                                master=self.second_tab_frames[2],
                                                variable= self.pressure_choice,
                                                values= self.pressure_units,
                                                fg_color="#fdfdfd",
                                                button_color=BTN_FG_COLOR,
                                                button_hover_color=BTN_FG_HOVER_COLOR,
                                                text_color=TEXT_COLOR,
                                                text_color_disabled="#292929",
                                                width=50,
                                                )
        self.press_option_menu.pack(fill='both', padx=5, pady=5)

        ####### Frame 4 - Kmeans Cluster
        self.second_tab_frames[3].columnconfigure((0,1), weight=1, uniform='a')
        self.second_tab_frames[3].rowconfigure((0,1), weight=1, uniform='a')

        # Kmeans Frame
        self.kmeans_frame = ctk.CTkFrame(self.second_tab_frames[3], fg_color="transparent")
        self.kmeans_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        self.kmeans_label = ctk.CTkLabel(self.kmeans_frame, text="Agrupamento: ", font=("Segoe UI", 16), height=height)
        self.kmeans_label.pack(side="left", padx=5, pady=5)

        self.kmeans_entry = custom_CTkEntry(self.kmeans_frame, placeholder_text="Insira aqui...")
        self.kmeans_entry.pack(side="right", expand=True, padx=5, pady=5)

        custom_tooltip(self.kmeans_entry, "Insira o número de agrupamentos para dividir o dado", delay=1)

        # Radio Button Frame
        self.radiobtn_frame = ctk.CTkFrame(self.second_tab_frames[3], fg_color="transparent")
        self.radiobtn_frame.columnconfigure((0,1), weight=1)
        self.header_bool = tk.StringVar()
        self.header_sim_ou_nao = ctk.CTkLabel(self.radiobtn_frame,
                                              text="O arquivo possui header?: ",
                                              font=("Segoe UI", 14))
        self.toggle_frame = ctk.CTkFrame(self.radiobtn_frame, fg_color="transparent")

        self.header_y = ctk.CTkRadioButton(self.toggle_frame,
                                           command=self.radiobutton_event(self.header_bool),
                                           variable=self.header_bool, value="Sim", text="Sim")
        self.header_n = ctk.CTkRadioButton(self.toggle_frame,
                                           command=self.radiobutton_event(self.header_bool),
                                           variable=self.header_bool, value="Não", text="Não")

        self.radiobtn_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nswe')
        self.header_sim_ou_nao.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nswe')
        self.toggle_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nswe')
        self.header_y.pack(side='left', expand=True)
        self.header_n.pack(side='left', expand=True)

        ####### Frame 5 - Plot btn
        self.calc_btn = create_custom_button(root=self.second_tab_frames[4],
                                            text="Plotar",
                                            command=self.call_plot_trends,
                                            width=200)
        self.calc_btn.pack(side="top", padx=5, pady=5)

    def third_tab(self):
        pass

    def radiobutton_event(self, var):
        # Get the currently selected value
        self.selected_value = var.get()

        if self.selected_value == "Sim":
            return "Sim"
        elif self.selected_value == "Não":
            return "Não"

    def open_file(self, skiprows=0):
        arq_label_selected_file = "./uploads/" + self.selected_file.get()
        try:
            pressao_df = pd.read_csv(arq_label_selected_file,
                                    delimiter='[;,]',
                                    skiprows=skiprows,
                                    names=["prof", "pressao"],
                                    engine='python')
            pressao_df = pressao_df.dropna()
            return pressao_df
        except Exception as e:
            custom_messagebox(title="Erro", message=f"Erro ao ler o arquivo {self.selected_file.get()}: {e}",
                          icon="./img/icons/cancel.png", option_1="OK", width=400)
            return None

    # dataframe = self.open_file()
    def file_dialog_standard(self, frame, width=width, height=height, border_width=border_width):
        class CTkCustomOptionMenu(ctk.CTkOptionMenu):
            def destroy(self):
                self.tk.call('destroy', self._w)

        file_names = os.listdir("./uploads")

        self.selected_file = tk.StringVar(frame)
        self.arq_label = ctk.CTkLabel(frame,
                                text="Selecione o arquivo: ",
                                font=("Segoe UI", 16),
                                width=width, height=height)
        self.arq_label.pack(fill='x', padx=5, pady=5)

        self.arq_option_menu = CTkCustomOptionMenu(
                                                master=frame,
                                                variable=self.selected_file,
                                                values=file_names,
                                                fg_color="#fdfdfd",
                                                button_color=BTN_FG_COLOR,
                                                button_hover_color=BTN_FG_HOVER_COLOR,
                                                text_color=TEXT_COLOR,
                                                text_color_disabled="#292929",
                                                width=75,
                                                )
        self.arq_option_menu.pack(fill='x', padx=5, pady=5)

    def plot_simple(self, x, y, title, xlabel, ylabel, ymin, ymax, dataframe):

        if not self.radiobutton_event(self.prof_cota_var):
            msg = custom_messagebox(title="Erro", message="É obrigatório selecionar se o arquivo possui header ou não.",
                                icon="./img/icons/cancel.png", option_1="Cancelar", width=400)

        self.boolean = self.radiobutton_event(self.prof_cota_var)
        self.skip_rows_bool = self.skip_rows_entry.get()

        if self.skip_rows_bool == "Sim":
            self.dataframe = self.open_file(skiprows=1)
            print("Sim was selected")
        else:
            self.dataframe = self.open_file()
            print("Não was selected")

        ymin = int(self.prof_min_entry.get()) if self.prof_min_entry.get() else None
        ymax = int(self.prof_max_entry.get()) if self.prof_max_entry.get() else None

        try:
            self.boolean = self.radiobutton_event()

            if self.boolean == "Sim":
                plt.plot(x, y, 'o')
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                plt.show()
                print("Sim was selected")

            elif self.boolean == "Não":
                plt.plot(x, y, 'o')
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                    plt.gca().invert_yaxis()
                plt.show()
                print("Não was selected")

        except Exception as e:
            custom_messagebox(title="Error", message=f"Um erro ocorreu: {e}",
                        icon="./img/icons/cancel.png", option_1="OK", width=400)

    def call_plot_simple(self):
        # self.dataframe = self.open_file()
        self.plot_simple(self.dataframe.iloc[:, 1],
                          self.dataframe.iloc[:, 0],
                          self.plot_title_entry.get(),
                          self.x_label_entry.get(),
                          self.y_label_entry.get(),
                          self.prof_min_entry.get(),
                          self.prof_max_entry.get(),
                          self.dataframe)

    def plot_trends(self):
        if not self.radiobutton_event(self.header_bool):
            msg = custom_messagebox(title="Erro",
                                    message="É obrigatório selecionar se o arquivo possui header ou não.",
                                    icon="./img/icons/cancel.png",
                                    option_1="Cancelar", width=400)

        self.boolean = self.radiobutton_event(self.header_bool)

        if self.boolean == "Sim":
            df = self.open_file(skiprows=1)
            print("Há header no arquivo")
        else:
            df = self.open_file()
            print("Não há header no arquivo")

        prof = df["prof"]
        pressao = df["pressao"]

        def calculate_slope(ps_a, ps_b):
            if len(ps_a) != len(ps_b):
                raise ValueError("ps_a and ps_b must have the same length")
            coefficients = np.polyfit(ps_a, ps_b, 1)
            return coefficients[0]

        slopes = []
        slope_indices = {}
        for i in range(len(prof) - 1):
            x_values = np.array([prof[i], prof[i + 1]])
            y_values = np.array([pressao[i], pressao[i + 1]])
            slope = calculate_slope(x_values, y_values) * -1
            slopes.append(slope)
            slope_indices[slope] = [i, i + 1]

        # Convert the list of slopes to a numpy array
        slopes_array = np.array([slopes, slopes])

        # Perform KMeans clustering on the slopes
        kmeans_number = int(self.kmeans_entry.get())
        kmeans = KMeans(n_clusters=kmeans_number, random_state=0).fit(slopes_array.T)

        # Classify the data based on the clusters
        classified_data = [list(kmeans.labels_)[0]] + list(kmeans.labels_)

        def convert_classification(class_data):
            if class_data[0] == 1:
                return [1 - label for label in class_data]
            return class_data

        # Convert the classification labels if necessary
        converted_data = convert_classification(classified_data)

        # Separate the data into two groups based on the classification
        top_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 1]
        bottom_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 0]

        # Calculate the line of best fit for each group
        top_prof, top_pressao = zip(*top_values)
        bottom_prof, bottom_pressao = zip(*bottom_values)

        slope_top, intercept_top = np.polyfit(top_prof, top_pressao, 1)
        slope_bottom, intercept_bottom = np.polyfit(bottom_prof, bottom_pressao, 1)

        pressure_unit = self.pressure_choice.get()
        # four pressure units to choose from (psi/ft, psi/m, Kgf/cm2/m, bar/m)

        fluid_pressure = {
        "dry_gas_zero": {"name":"Dry gas zero","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
        "dry_gas": {"name":"Dry gas","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
        "wet_gas": {"name":"Wet gas","gradient":{"psi/ft":0.140,"psi/m":0.459,"kgf/cm2/m":0.030,"bar/m":0.032}},
        "oil_limit": {"name":"Oil limit","gradient":{"psi/ft":0.300,"psi/m":0.984,"kgf/cm2/m":0.069,"bar/m":0.069}},
        "oil_60": {"name":"Oil 60°","gradient":{"psi/ft":0.387,"psi/m":1.270,"kgf/cm2/m":0.089,"bar/m":0.087}},
        "oil_20": {"name":"Oil 20° (heavy)","gradient":{"psi/ft":0.404,"psi/m":1.325,"kgf/cm2/m":0.093,"bar/m":0.091}},
        "fresh_water": {"name":"Fresh water","gradient":{"psi/ft":0.433,"psi/m":1.421,"kgf/cm2/m":0.100,"bar/m":0.098}},
        "sea_water": {"name":"Sea Water","gradient":{"psi/ft":0.444,"psi/m":1.457,"kgf/cm2/m":0.102,"bar/m":0.101}},
        "salt_sat_water": {"name":"Salt sat. Water","gradient":{"psi/ft":0.520,"psi/m":1.706,"kgf/cm2/m":0.120,"bar/m":0.118}},
        "salt_max": {"name":"Salt sat. Water Max","gradient":{"psi/ft":100.000,"psi/m":100.000,"kgf/cm2/m":100.000,"bar/m":100.000}}
        }

        # Get a list of all fluid keys
        fluid_keys = list(fluid_pressure.keys())

        # Initialize an empty dictionary for pressure values
        pressure_values = {}

        # Iterate over each pair of consecutive fluids
        for i in range(len(fluid_keys) - 1):
            # Get the top and bottom fluids
            top_fluid = fluid_keys[i]
            bottom_fluid = fluid_keys[i + 1]

            # Get the pressure gradient values for the top and bottom fluids
            top_pressure = fluid_pressure[top_fluid]["gradient"][pressure_unit]
            bottom_pressure = fluid_pressure[bottom_fluid]["gradient"][pressure_unit]

            # Store the pressure values in the dictionary
            pressure_values[top_fluid] = [top_pressure, bottom_pressure]

        # Remove the first key-value pair from the dictionary
        first_key = next(iter(pressure_values))
        pressure_values.pop(first_key)

        # Initialize the top fluid
        top_fluid = 0

        # Find the fluid that matches the top slope
        for fluid, pressures in pressure_values.items():
            if -1.*round(slope_top,4) >= pressures[0] and -1.*round(slope_top,4) < pressures[1]:
                top_fluid = fluid

        # Find the fluid that matches the bottom slope
        for fluid, pressures in pressure_values.items():
            if -1.*round(slope_bottom,4) >= pressures[0] and -1.*round(slope_bottom,4) < pressures[1]:
                bottom_fluid = fluid

        # Get the names of the top and bottom fluids
        top_fluid_name = fluid_pressure[top_fluid]['name']
        bottom_fluid_name = fluid_pressure[bottom_fluid]['name']

        # Print the names of the top and bottom fluids
        print(top_fluid_name, "|", bottom_fluid_name)


        x_intercept = (intercept_bottom - intercept_top) / (slope_top - slope_bottom)
        y_intercept = slope_top * x_intercept + intercept_top
        print('O ponto de interseção das retas é',x_intercept,y_intercept)

        diff = np.diff(top_prof)
        print(diff)

        # Extended top curve
        mean_cota_top = np.mean(np.diff(top_prof))
        extended_cota_top = [(np.abs(mean_cota_top) + np.max(top_prof))] + list(top_prof)
        extended_pressure_top = np.array(extended_cota_top)*slope_top + intercept_top

        # Extended bot curve
        mean_cota_bot = np.mean(np.diff(bottom_prof))
        extended_cota_bot =  list(bottom_prof) + [(np.min(bottom_prof) + mean_cota_bot)]
        extended_pressure_bot = np.array(extended_cota_bot)*slope_bottom + intercept_bottom

        # Calculate the line of best fit for the top and bottom fluids
        line_top = slope_top * np.array(top_prof) + intercept_top
        line_bottom = slope_bottom * np.array(bottom_prof) + intercept_bottom

        plt.figure(figsize=(13,5))

        plt.subplot(131)
        plt.plot(top_pressao,top_prof,'o',c="C0",label='top curve '+str(round(slope_top,4)))
        plt.plot(bottom_pressao,bottom_prof,'o',c="C3",label='bot curve '+str(round(slope_bottom,4)))
        plt.legend(fontsize='small')
        plt.xlabel('Pressão (PSI)')
        plt.ylabel('Cota (M)')
        plt.grid()
        # plt.show() # Plota o gráfico com os clusters divididos

        plt.subplot(132)
        # Plot the data points for the top and bottom fluids
        plt.plot(top_pressao, top_prof, 'o', c="C0", label=top_fluid_name)
        plt.plot(bottom_pressao, bottom_prof, 'o', c="C3", label=bottom_fluid_name)

        # Plot the lines of best fit for the top and bottom fluids
        plt.plot(line_top, top_prof, c="C9", label=f'{top_fluid_name} {round(slope_top, 4)}')
        plt.plot(line_bottom, bottom_prof, c="C1", label=f'{bottom_fluid_name} {round(slope_bottom, 4)}')

        # Add a legend, labels, and a grid
        plt.legend(fontsize='small')
        plt.xlabel('Pressão (PSI)')
        plt.ylabel('Cota (M)')
        plt.grid()

        plt.subplot(133)
        plt.plot(top_pressao,top_prof,'o',c="C0",label=top_fluid_name)
        plt.plot(bottom_pressao,bottom_prof,'o',c="C3",label=bottom_fluid_name)

        plt.plot(extended_pressure_top,extended_cota_top,c="C9",label=bottom_fluid_name+" "+str(round(slope_bottom,4)))
        plt.plot(extended_pressure_bot,extended_cota_bot,c="C1",label=top_fluid_name+" "+str(round(slope_top,4)))
        plt.plot(y_intercept,x_intercept,'s',c="k",label="Intersection "+str(round(x_intercept,4)) )

        plt.legend(fontsize='small')
        plt.xlabel('Pressure (PSI)')
        plt.ylabel('Level (M)')
        plt.grid()

        plt.tight_layout()
        plt.show()

    def call_plot_trends(self):
        self.plot_trends()


class SheetEditor:
    """
    A class used to represent a Sheet Editor.
    This class provides the functionality to create and manipulate a sheet within a GUI.
    It allows for operations such as adding and removing rows
    and columns, opening and saving the sheet as a CSV file,
    and various other operations provided by the underlying `Sheet` class from the `ctk` library.
    """

    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.sheet = Sheet(self.master)

    def toolbar(self):
        ########################## TOOLBAR ##############################
        self.toolbar_frame = ctk.CTkFrame(self.master, fg_color="#fff")
        self.toolbar_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        self.new_file_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.new_file_frame.pack(side='left', padx=5, pady=5)

        self.folder_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                                corner_radius=10,
                                                border_width=0,
                                                fg_color="transparent")
        self.folder_icon_frame.pack(side='left', padx=5, pady=5)

        self.save_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.save_icon_frame.pack(side='left', padx=5, pady=5)

        self.inventory_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.inventory_frame.pack(side='left', padx=5, pady=5)

        self.plot_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                        border_width=0,
                                        fg_color="transparent")
        self.plot_frame.pack(side='left', padx=5, pady=5)

        self.code_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.code_icon_frame.pack(side='left', padx=5, pady=5)

        self.font_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.font_frame.pack(side='left', padx=5, pady=5)

        self.col_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.col_frame.pack(side='right', padx=5, pady=5)

        self.row_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.row_frame.pack(side='right', padx=5, pady=5)



        add_row_btn = ctk.CTkButton(self.row_frame,
                                    command=self.add_row,
                                    border_width=0,
                                    text="",
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="transparent",
                                    hover_color="#6da3d1"
                                    )
        add_row_btn.grid(row=0,column=0, padx=5, pady=5)
        custom_tooltip(add_row_btn, "+Linhas", delay=0.5)

        add_row_txt = "L"
        add_row_label = ctk.CTkLabel(self.row_frame, text=add_row_txt, font=("Segoe UI",16,"bold"))
        add_row_label.grid(row=0,column=1, padx=2, pady=2)
        # Add buttons to the toolbar


        rm_row_btn = ctk.CTkButton(self.row_frame,
                                text="",
                                command=self.remove_row,
                                image=remove_img,
                                width=10,
                                height=10,
                                fg_color="transparent",
                                hover_color="#d97373"
                                )
        rm_row_btn.grid(row=0,column=2, padx=5, pady=5)
        custom_tooltip(rm_row_btn, "-Linhas", delay=0.5)

        add_col_btn = ctk.CTkButton(self.col_frame,
                                    text="",
                                    command=self.add_column,
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="transparent",
                                    hover_color="#6da3d1"
                                    )
        add_col_btn.grid(row=0,column=0, padx=5, pady=5)
        custom_tooltip(add_col_btn, "+Colunas", delay=0.5)

        add_col_txt = "C"
        add_col_label = ctk.CTkLabel(self.col_frame, text=add_col_txt, font=("Segoe UI",16,"bold"))
        add_col_label.grid(row=0,column=1, padx=2, pady=2)

        rm_col_btn = ctk.CTkButton(self.col_frame,
                                   text="",
                                   command=self.remove_column,
                                   image=remove_img,
                                   width=10,
                                   height=10,
                                   fg_color="transparent",
                                   hover_color="#d97373"
                                   )
        rm_col_btn.grid(row=0,column=2, padx=5, pady=5)
        custom_tooltip(rm_col_btn, "-Colunas", delay=0.5)

        font_selector = ctk.CTkButton(self.font_frame,
                                      text="",
                                      command=placeholder_function,
                                      image=font_img,
                                      width=10,
                                      height=10,
                                      fg_color="transparent",
                                      hover_color="#e2e8f0")
        font_selector.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(font_selector, "Selecionar fonte", delay=0.5)

        plot_btn_toolbar = ctk.CTkButton(self.plot_frame,
                                        text="",
                                        command=self.app.calculate.open_calculations_window,
                                        image=show_plot_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                      hover_color="#e2e8f0")
        plot_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(plot_btn_toolbar, "Abrir Calculadora", delay=0.5)

        inventory_btn_toolbar = ctk.CTkButton(self.inventory_frame,
                                            text="",
                                            command=self.app.manage_files.open_manage_window,
                                            image=inventory_img,
                                            width=10,
                                            height=10,
                                            fg_color="transparent",
                                            hover_color="#e2e8f0")
        inventory_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(inventory_btn_toolbar, "Gerenciador de Arquivos", delay=0.5)

        code_btn_toolbar = ctk.CTkButton(self.code_icon_frame,
                                        text="",
                                        command=self.app.code_editor.open_code_editor,
                                        image=code_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        code_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(code_btn_toolbar, "Editor de Texto", delay=0.5)

        save_btn_toolbar = ctk.CTkButton(self.save_icon_frame,
                                        text="",
                                        command=self.app.sheet_editor.save_sheet,
                                        image=save_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        save_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(save_btn_toolbar, "Salvar", delay=0.5)

        folder_btn_toolbar = ctk.CTkButton(self.folder_icon_frame,
                                        text="",
                                        command=self.app.sheet_editor.open_csv,
                                        image=folder_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        folder_btn_toolbar.grid(row=0, column=0, padx=0, pady=0) # Open
        custom_tooltip(folder_btn_toolbar, "Abrir", delay=0.5)

        new_file_btn_toolbar = ctk.CTkButton(self.new_file_frame,
                                            text="",
                                            command=self.app.sheet_editor.open_sheet,
                                            image=new_file_img,
                                            width=10,
                                            height=10,
                                            fg_color="transparent",
                                            hover_color="#e2e8f0")
        new_file_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(new_file_btn_toolbar, "Novo", delay=0.5)

    def open_sheet(self):
        self.toolbar()
        # Create a frame for the sheet
        self.sheet_editor_frame = ctk.CTkFrame(self.master)
        self.sheet_editor_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        # Configure the master grid to expand
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Configure the sheet_editor_frame grid to expand
        self.sheet_editor_frame.grid_rowconfigure(0, weight=1)
        self.sheet_editor_frame.grid_columnconfigure(0, weight=1)

        # Create a sheet
        self.sheet = Sheet(self.sheet_editor_frame,
                        page_up_down_select_row=True,
                        default_column_width=120,
                        total_columns=100,
                        total_rows=100,
                        startup_select=(0, 1, "rows"),
                        data=[["" for _ in range(26)] for _ in range(100)],
                        theme="light green")

        self.sheet.grid(row=0, column=0, sticky='nsew')  # Place the sheet in the grid

        self.sheet.enable_bindings(("single_select", "drag_select", "column_drag_and_drop", "row_drag_and_drop",
                                   "column_select", "row_select", "column_width_resize", "double_click_column_resize",
                                   "row_width_resize", "column_height_resize", "arrowkeys", "row_height_resize",
                                   "double_click_row_resize", "right_click_popup_menu", "rc_select", "rc_insert_column",
                                   "rc_delete_column", "rc_insert_row", "rc_delete_row",
                                   "edit_cell", "paste", "cut", "delete", "copy", "undo",
                                   "ctrl_select", "shift_select", "ctrl_a", "double_click_cell", "right_click_cell"
                                   ))

        # Configure the grid to expand
        self.sheet.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #self.sheet.set_all_cell_sizes_to_text()
        # print(self.sheet["A1"].expand().options(header=True, index=True).data)
        self.sheet.popup_menu_add_command("Abrir .csv", self.open_csv)
        self.sheet.popup_menu_add_command("Salvar", self.save_sheet)

        self.sheet_span = self.sheet.span(
            header=True,
            index=True,
            hdisp=False,
            idisp=False,
        )

    def add_row(self):
        # Insert a new row at the end of the sheet
        self.sheet.insert_rows(rows=1)

    def add_column(self):
        self.sheet.insert_columns(columns=1)

    def remove_row(self):
        last_row_index = self.sheet.total_rows() - 1
        self.sheet.delete_rows(rows=last_row_index, undo=True)

    def remove_column(self):
        last_column_index = self.sheet.total_columns() - 1
        self.sheet.delete_columns(columns=last_column_index, undo=True)

    def save_sheet(self):
        filepath = filedialog.asksaveasfilename(
            parent=self.master,
            title="Salvar a planilha como...",
            filetypes=[("CSV File", ".csv"), ("TSV File", ".tsv")],
            defaultextension=".csv",
            confirmoverwrite=True,
        )
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(
                    fh,
                    dialect=csv.excel if filepath.lower().endswith(".csv") else csv.excel_tab,
                    lineterminator="\n",
                )
                for row in self.sheet.data:
                    # Clean the data: remove leading/trailing white space
                    cleaned_row = [cell.strip() for cell in row if cell.strip() != '']
                    # Ignore rows that only contain empty cells
                    if cleaned_row:
                        writer.writerow(cleaned_row)
            # Updating the backup
            self.sheet.data_backup = self.sheet.data.copy()
        except Exception as error:
            print(error)

    def open_csv(self):

        filepath = filedialog.askopenfilename(parent=self.master, title="Select a csv file")
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "r") as filehandle:
                filedata = filehandle.read()
            # self.sheet.reset()
            self.sheet.data = [
                r for r in csv.reader(
                    io.StringIO(filedata),
                    dialect=csv.Sniffer().sniff(filedata),
                    skipinitialspace=True,
                )
            ]
        except Exception as error:
            print(error)

    def new_sheet(self):
        self.sheet.reset()
        self.menu_bar.entryconfig(self.open_command, state='normal')

class CodeEditorWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_code_editor(self):
        self.code_editor = NewWindow(self.master, self.app)
        self.code_editor.title("Editor de texto")

        #function that centralizes the window
        # centralize_window(code_editor, 800, 600)

        # code_editor.minsize(300, 200)
        # code_editor.maxsize(300, 200)
        # code_editor.option_add("*Label.font", "Helvetica 15")

        self.code_editor_frame = tk.Frame(self.code_editor)
        self.code_editor_frame.bind("<Configure>",
                                    lambda event:\
                                        update_and_centralize_geometry(self.code_editor,
                                                                       self.code_editor_frame,
                                                                       max_size=True,
                                                                       child_window=True))
        self.code_editor_frame.grid(row=0, column=0, padx=10, pady=10)
        # self.code_editor_frame.place(relx=0.5, rely=0.5, anchor='center')


        # Create a code editor
        self.code_editor_view = CodeView(self.code_editor_frame,
                                         lexer=pygments.lexers.RustLexer, tab_width=4)
        self.code_editor_view.config(font=("Consolas", 16))
        self.code_editor_view.grid(row=0, column=0, sticky='nsew')

        self.code_editor_frame.grid_rowconfigure(0, weight=1)

        self.btn_code_editor_frame = tk.Frame(self.code_editor_frame)
        self.btn_code_editor_frame.grid(row=1, column=0, padx=10, pady=10)

        self.save_code = create_custom_button(self.btn_code_editor_frame,
                                              text="Salvar",
                                              command=self.save_code,
                                              width=100)
        self.save_code.grid(row=0, column=0, padx=10, pady=10)

    def save_code(self):
        # Get the text from the CodeView widget
        code = self.code_editor_view.get("1.0", "end-1c")

        # Open a file dialog to select where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        # Write the code to the file
        if file_path:
            with open(file_path, "w") as file:
                file.write(code)

class Application:
    def __init__(self, master):
        self.master = master
        # self.file_handling = FileViewerPandas(self.master, self)
        self.sheet_editor = SheetEditor(self.master, self)
        self.code_editor = CodeEditorWindow(self.master, self)
        self.menu_bar = MenuBar(self.master, self)
        self.calculate = CalculationsWindow(self.master, self)
        self.tomi = TOMICalc(self.master, self)
        self.manage_files = ManageFilesWindow(self.master, self)

class MenuBar:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.menu_bar = tk.Menu(self.master)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Novo", accelerator='Ctrl+N',
                              command = self.app.sheet_editor.open_sheet)
        self.master.bind_all('<Control-n>', lambda event: self.app.sheet_editor.open_sheet())

        file_menu.add_command(label="Abrir",
                              command=self.app.sheet_editor.open_csv,
                              accelerator='Ctrl+O',
                              #state='disabled'
                              )
        self.master.bind_all('<Control-o>', lambda event: self.app.sheet_editor.open_csv())

        file_menu.add_command(label="Salvar",
                              command=self.app.sheet_editor.save_sheet,
                              accelerator='Ctrl+S')
        self.master.bind_all('<Control-s>', lambda event: self.app.sheet_editor.save_sheet())


        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.master.quit) # TODO: If something is not saved, ask if the user wants to save it
        # Adicionar o botão de arquivo ao menu
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Create an Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        # edit_menu.add_command(label="Abrir PandasGUI", command=self.app.file_handling.view_file)
        edit_menu.add_command(label="Gerenciar arquivos", command=self.app.manage_files.open_manage_window)
        edit_menu.add_command(label="Editor de texto", command=self.app.code_editor.open_code_editor)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar", accelerator='Ctrl+X') # TODO: Create a function or implement the method that cuts the selected text
        edit_menu.add_command(label="Copiar", accelerator='Ctrl+C') # TODO: Create a function or implement the method that copies the selected text
        edit_menu.add_command(label="Colar", accelerator='Ctrl+V') # TODO: Create a function or implement the method that pastes the selected text
        # Add the Edit menu to the menu bar
        # accelerator argument adds the shortcut
        self.menu_bar.add_cascade(label="Editar", menu=edit_menu)

        calculations_menu = tk.Menu(self.menu_bar, tearoff=0)
        calculations_menu.add_command(label="Calculadora",
                                      command=self.app.calculate.open_calculations_window
                                      )
        calculations_menu.add_command(label="TOMI Index",
                                      command=self.app.tomi.open_tomi_window)

        self.menu_bar.add_cascade(label="Calcular", menu=calculations_menu)

        about_menu = tk.Menu(self.menu_bar, tearoff=0)
        about_menu.add_command(label="Ajuda", command=self.help_window) # TODO: Create a function that shows the about window
        self.master.bind_all('<Control-h>', lambda event: self.help_window())
        about_menu.add_command(label="Sobre o GradPress", command=self.about_gradpress_window)

        self.menu_bar.add_cascade(label="Sobre", menu=about_menu)


        self.master.config(menu=self.menu_bar)

    def save_file(self):
        # Get the data from the sheet
        data = self.sheet_editor.sheet.data()

        # Open a save file dialog
        filepath = filedialog.asksaveasfilename(defaultextension=".csv")

        # If a file was selected, save the data to the file
        if filepath:
            with open(filepath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)

    def about_gradpress_window(self):
        self.about_page = AboutPage(self.master)


    def help_window(self):
        # TODO: Create a help window
        help_window = HelpWindow(self.master)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # startup the application
        ctk.set_appearance_mode("light")
        self.title("Kraken Geophysics")
        self.iconbitmap(default="./icon.ico")  # icon
        self.option_add("*Label.font", "Segoe\\ UI 15")  # font
        centralize_window(self, 900, 600) # function that centralizes the window
        self.minsize(800, 600)

        self.sheet_editor = SheetEditor(self, self)
        self.code_editor = CodeEditorWindow(self, self)

        self.calculate = CalculationsWindow(self, self)
        self.tomi = TOMICalc(self, self)
        self.manage_files = ManageFilesWindow(self, self)
        self.menubar = MenuBar(self, self)


        self.sheet_editor.open_sheet()

if __name__ == "__main__":
    app = App()
    app.mainloop()