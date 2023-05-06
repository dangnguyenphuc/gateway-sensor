from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import sys
import time
import pandas as pd
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def Exit_Program():
    sys.exit()

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("System Management Dashboard")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        # Window Icon Photo
        icon = PhotoImage(file='images/pic-icon.png')
        self.window.iconphoto(True, icon)

        # ==============================================================================
        # ================== HEADER ====================================================
        # ==============================================================================
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)


        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='NMDK', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=110, y=200)

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file='images/dashboard-icon.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text="Manage", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(file='images/settings-icon.png')
        self.settings = Label(self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Settings", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # Exit
        self.ExitImage = ImageTk.PhotoImage(file='images/exit-icon.png')
        self.Exit = Label(self.sidebar, image=self.ExitImage, bg='#ffffff')
        self.Exit.place(x=25, y=452)

        self.Exit_text = Button(self.sidebar, text="Exit", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=Exit_Program)
        self.Exit_text.place(x=85, y=462)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        self.pieChart_image = ImageTk.PhotoImage(file='images/pie-graph1.png')
        self.pieChart = Label(self.bodyFrame1, image=self.pieChart_image, bg='#ffffff')
        self.pieChart.place(x=690, y=70)

        # Graph
        self.graph_image = ImageTk.PhotoImage(file='images/graph.png')
        self.graph = Label(self.bodyFrame1, image=self.graph_image, bg='#ffffff')
        self.graph.place(x=40, y=70)

        # Body Frame 2
        self.total_people = Label(self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        self.total_people.place(x=120, y=100)

        self.totalPeopleImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.totalPeople = Label(self.bodyFrame2, image=self.totalPeopleImage, bg='#009aa5')
        self.totalPeople.place(x=220, y=0)

        self.totalPeople_label = Label(self.bodyFrame2, text="Total People", bg='#009aa5', font=("", 12, "bold"),
                                       fg='white')
        self.totalPeople_label.place(x=5, y=5)

        # Body Frame 3
        self.people_left = Label(self.bodyFrame3, text='50', bg='#e21f26', font=("", 25, "bold"))
        self.people_left.place(x=120, y=100)

        # left icon
        self.LeftImage = ImageTk.PhotoImage(file='images/left-icon.png')
        self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#e21f26')
        self.Left.place(x=220, y=0)

        self.peopleLeft_label = Label(self.bodyFrame3, text="Left", bg='#e21f26', font=("", 12, "bold"),
                                      fg='white')
        self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        self.total_earnings = Label(self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        self.total_earnings.place(x=80, y=100)

        self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#ffcb1f', font=("", 12, "bold"),
                                    fg='white')
        self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        self.earningsIcon_image = ImageTk.PhotoImage(file='images/earn3.png')
        self.earningsIcon = Label(self.bodyFrame4, image=self.earningsIcon_image, bg='#ffcb1f')
        self.earningsIcon.place(x=220, y=0)




        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()
    
    def animate(self, i):
        # Generate values
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))
        y_vals2.append(random.randint(0, 5))
        # Get all axes of figure
        ax1, ax2 = plt.gcf().get_axes()
        # Clear current data
        ax1.cla()
        ax2.cla()
        # Plot new data
        ax1.plot(x_vals, y_vals)
        ax2.plot(x_vals, y_vals2)

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=("", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)


def wind():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    wind()



# data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
#          'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
#          }
# df1 = pd.DataFrame(data1)

# data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
#          'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
#          }  
# df2 = pd.DataFrame(data2)

# data3 = {'interest_rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
#          'index_price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
#          }
# df3 = pd.DataFrame(data3)

# root = tk.Tk()

# figure1 = plt.Figure(figsize=(6, 5), dpi=100)
# ax1 = figure1.add_subplot(111)
# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Country Vs. GDP Per Capita')

# figure2 = plt.Figure(figsize=(5, 4), dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2, root)
# line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
# ax2.set_title('Year Vs. Unemployment Rate')

# figure3 = plt.Figure(figsize=(5, 4), dpi=100)
# ax3 = figure3.add_subplot(111)
# ax3.scatter(df3['interest_rate'], df3['index_price'], color='g')
# scatter3 = FigureCanvasTkAgg(figure3, root)
# scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# ax3.legend(['index_price'])
# ax3.set_xlabel('Interest Rate')
# ax3.set_title('Interest Rate Vs. Index Price')

# root.mainloop()



# # values for first graph
# x_vals = []
# y_vals = []
# # values for second graph
# y_vals2 = []

# index = count()
# index2 = count()

# def animate(i):
#     # Generate values
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))
#     y_vals2.append(random.randint(0, 5))
#     # Get all axes of figure
#     ax1, ax2 = plt.gcf().get_axes()
#     # Clear current data
#     ax1.cla()
#     ax2.cla()
#     # Plot new data
#     ax1.plot(x_vals, y_vals)
#     ax2.plot(x_vals, y_vals2)


# # GUI
# root = tk.Tk()
# label = tk.Label(root, text="Realtime Animated Graphs").grid(column=0, row=0)

# # graph 1
# canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
# canvas.get_tk_widget().grid(column=0, row=1)
# # Create two subplots in row 1 and column 1, 2
# plt.gcf().subplots(1, 2)
# ani = FuncAnimation(plt.gcf(), animate, interval=1000, blit=False)

# tk.mainloop()


