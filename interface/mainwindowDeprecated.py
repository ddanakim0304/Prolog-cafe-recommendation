# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 281, 291))
        self.graphicsView.setObjectName("graphicsView")
        self.cafe_name = QtWidgets.QLabel(self.centralwidget)
        self.cafe_name.setGeometry(QtCore.QRect(40, 350, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.cafe_name.setFont(font)
        self.cafe_name.setObjectName("cafe_name")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setGeometry(QtCore.QRect(50, 590, 100, 32))
        self.previous_button.setObjectName("previous_button")
        self.manage_constraints = QtWidgets.QGroupBox(self.centralwidget)
        self.manage_constraints.setGeometry(QtCore.QRect(330, 590, 371, 61))
        self.manage_constraints.setObjectName("manage_constraints")
        self.comboBox = QtWidgets.QComboBox(self.manage_constraints)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 211, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.manage_constraints)
        self.pushButton.setGeometry(QtCore.QRect(260, 20, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(170, 590, 100, 32))
        self.next_button.setObjectName("next_button")
        self.result_info = QtWidgets.QLabel(self.centralwidget)
        self.result_info.setEnabled(False)
        self.result_info.setGeometry(QtCore.QRect(100, 630, 131, 16))
        self.result_info.setStyleSheet("")
        self.result_info.setObjectName("result_info")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 110, 371, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.opening_closing = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.opening_closing.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.opening_closing.sizePolicy().hasHeightForWidth()
        )
        self.opening_closing.setSizePolicy(sizePolicy)
        self.opening_closing.setMinimumSize(QtCore.QSize(356, 143))
        self.opening_closing.setBaseSize(QtCore.QSize(0, 120))
        self.opening_closing.setObjectName("opening_closing")
        self.label_9 = QtWidgets.QLabel(self.opening_closing)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.daySelect = QtWidgets.QComboBox(self.opening_closing)
        self.daySelect.setGeometry(QtCore.QRect(10, 30, 211, 32))
        self.daySelect.setObjectName("daySelect")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.daySelect.addItem("")
        self.label_10 = QtWidgets.QLabel(self.opening_closing)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.remove_opening_closing = QtWidgets.QPushButton(self.opening_closing)
        self.remove_opening_closing.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_opening_closing.setObjectName("remove_opening_closing")
        self.from_time = QtWidgets.QTimeEdit(self.opening_closing)
        self.from_time.setGeometry(QtCore.QRect(100, 60, 118, 22))
        self.from_time.setObjectName("from_time")
        self.to_time = QtWidgets.QTimeEdit(self.opening_closing)
        self.to_time.setGeometry(QtCore.QRect(100, 90, 118, 22))
        self.to_time.setObjectName("to_time")
        self.label_12 = QtWidgets.QLabel(self.opening_closing)
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QtCore.QRect(110, 120, 131, 16))
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.opening_closing)
        self.transportation = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.transportation.sizePolicy().hasHeightForWidth()
        )
        self.transportation.setSizePolicy(sizePolicy)
        self.transportation.setMinimumSize(QtCore.QSize(357, 114))
        self.transportation.setObjectName("transportation")
        self.transportType = QtWidgets.QComboBox(self.transportation)
        self.transportType.setGeometry(QtCore.QRect(10, 30, 131, 21))
        self.transportType.setMaxVisibleItems(3)
        self.transportType.setPlaceholderText("")
        self.transportType.setObjectName("transportType")
        self.transportType.addItem("")
        self.transportType.addItem("")
        self.transportType.addItem("")
        self.travel_time = QtWidgets.QLineEdit(self.transportation)
        self.travel_time.setGeometry(QtCore.QRect(50, 60, 81, 21))
        self.travel_time.setObjectName("travel_time")
        self.label_7 = QtWidgets.QLabel(self.transportation)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 31, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.transportation)
        self.label_8.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_8.setObjectName("label_8")
        self.remove_transportation = QtWidgets.QPushButton(self.transportation)
        self.remove_transportation.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_transportation.setObjectName("remove_transportation")
        self.transportation_warning = QtWidgets.QLabel(self.transportation)
        self.transportation_warning.setEnabled(False)
        self.transportation_warning.setGeometry(QtCore.QRect(110, 90, 131, 16))
        self.transportation_warning.setStyleSheet("")
        self.transportation_warning.setObjectName("transportation_warning")
        self.verticalLayout_2.addWidget(self.transportation)
        self.power_sockets = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.power_sockets.sizePolicy().hasHeightForWidth()
        )
        self.power_sockets.setSizePolicy(sizePolicy)
        self.power_sockets.setMinimumSize(QtCore.QSize(0, 60))
        self.power_sockets.setObjectName("power_sockets")
        self.socketCheck = QtWidgets.QCheckBox(self.power_sockets)
        self.socketCheck.setEnabled(True)
        self.socketCheck.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.socketCheck.setCheckable(True)
        self.socketCheck.setChecked(True)
        self.socketCheck.setObjectName("socketCheck")
        self.remove_power_sockets = QtWidgets.QPushButton(self.power_sockets)
        self.remove_power_sockets.setGeometry(QtCore.QRect(250, 20, 100, 32))
        self.remove_power_sockets.setObjectName("remove_power_sockets")
        self.verticalLayout_2.addWidget(self.power_sockets)
        self.wifi = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifi.sizePolicy().hasHeightForWidth())
        self.wifi.setSizePolicy(sizePolicy)
        self.wifi.setMinimumSize(QtCore.QSize(0, 60))
        self.wifi.setObjectName("wifi")
        self.wifi_check = QtWidgets.QCheckBox(self.wifi)
        self.wifi_check.setEnabled(True)
        self.wifi_check.setGeometry(QtCore.QRect(10, 30, 171, 20))
        self.wifi_check.setCheckable(True)
        self.wifi_check.setChecked(True)
        self.wifi_check.setObjectName("wifi_check")
        self.remove_wifi = QtWidgets.QPushButton(self.wifi)
        self.remove_wifi.setGeometry(QtCore.QRect(250, 20, 100, 32))
        self.remove_wifi.setObjectName("remove_wifi")
        self.verticalLayout_2.addWidget(self.wifi)
        self.dietary_pref = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dietary_pref.sizePolicy().hasHeightForWidth())
        self.dietary_pref.setSizePolicy(sizePolicy)
        self.dietary_pref.setMinimumSize(QtCore.QSize(357, 67))
        self.dietary_pref.setObjectName("dietary_pref")
        self.dietaryPreference = QtWidgets.QComboBox(self.dietary_pref)
        self.dietaryPreference.setGeometry(QtCore.QRect(10, 30, 211, 32))
        self.dietaryPreference.setObjectName("dietaryPreference")
        self.dietaryPreference.addItem("")
        self.dietaryPreference.addItem("")
        self.dietaryPreference.addItem("")
        self.remove_diet = QtWidgets.QPushButton(self.dietary_pref)
        self.remove_diet.setGeometry(QtCore.QRect(250, 30, 100, 32))
        self.remove_diet.setObjectName("remove_diet")
        self.verticalLayout_2.addWidget(self.dietary_pref)
        self.price = QtWidgets.QGroupBox(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(330, 40, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy)
        self.price.setMinimumSize(QtCore.QSize(357, 0))
        self.price.setMaximumSize(QtCore.QSize(500, 440))
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(self.price)
        self.label_6.setGeometry(QtCore.QRect(140, 30, 58, 16))
        self.label_6.setObjectName("label_6")
        self.maximumPrice = QtWidgets.QLineEdit(self.price)
        self.maximumPrice.setGeometry(QtCore.QRect(10, 30, 113, 21))
        self.maximumPrice.setObjectName("maximumPrice")
        self.cafe_address = QtWidgets.QLabel(self.centralwidget)
        self.cafe_address.setGeometry(QtCore.QRect(50, 400, 221, 51))
        self.cafe_address.setWordWrap(True)
        self.cafe_address.setObjectName("cafe_address")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cafe_name.setText(_translate("MainWindow", "Dandy Cafe"))
        self.label_11.setText(_translate("MainWindow", "CAFE FINDER"))
        self.previous_button.setText(_translate("MainWindow", "previous"))
        self.manage_constraints.setTitle(_translate("MainWindow", "Manage Constraints"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Travel Time"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Must have wifi"))
        self.comboBox.setItemText(
            2, _translate("MainWindow", "Must have power sockets")
        )
        self.comboBox.setItemText(3, _translate("MainWindow", "Dietary Preference"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Meals"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Opening Time"))
        self.pushButton.setText(_translate("MainWindow", "add"))
        self.next_button.setText(_translate("MainWindow", "next"))
        self.result_info.setText(_translate("MainWindow", "Input Time is in 24hrs"))
        self.opening_closing.setTitle(_translate("MainWindow", "Opening/Closing times"))
        self.label_9.setText(_translate("MainWindow", "From"))
        self.daySelect.setItemText(0, _translate("MainWindow", "monday"))
        self.daySelect.setItemText(1, _translate("MainWindow", "tuesday"))
        self.daySelect.setItemText(2, _translate("MainWindow", "wednesday"))
        self.daySelect.setItemText(3, _translate("MainWindow", "thursday"))
        self.daySelect.setItemText(4, _translate("MainWindow", "friday"))
        self.daySelect.setItemText(5, _translate("MainWindow", "saturday"))
        self.daySelect.setItemText(6, _translate("MainWindow", "sunday"))
        self.label_10.setText(_translate("MainWindow", "To"))
        self.remove_opening_closing.setText(_translate("MainWindow", "remove"))
        self.label_12.setText(_translate("MainWindow", "Input Time is in 24hrs"))
        self.transportation.setTitle(_translate("MainWindow", "Transportation"))
        self.transportType.setItemText(0, _translate("MainWindow", "Walk"))
        self.transportType.setItemText(1, _translate("MainWindow", "Public Transport"))
        self.transportType.setItemText(2, _translate("MainWindow", "Taxi/Moto"))
        self.label_7.setText(_translate("MainWindow", "for"))
        self.label_8.setText(_translate("MainWindow", "minutes"))
        self.remove_transportation.setText(_translate("MainWindow", "remove"))
        self.transportation_warning.setText(
            _translate("MainWindow", "Input Time is in 24hrs")
        )
        self.power_sockets.setTitle(_translate("MainWindow", "Power sockets"))
        self.socketCheck.setText(_translate("MainWindow", "Must have power sockets"))
        self.remove_power_sockets.setText(_translate("MainWindow", "remove"))
        self.wifi.setTitle(_translate("MainWindow", "Wifi"))
        self.wifi_check.setText(_translate("MainWindow", "Must have wifi"))
        self.remove_wifi.setText(_translate("MainWindow", "remove"))
        self.dietary_pref.setTitle(_translate("MainWindow", "Dietary Preference"))
        self.dietaryPreference.setItemText(0, _translate("MainWindow", "vegan"))
        self.dietaryPreference.setItemText(1, _translate("MainWindow", "vegeterian"))
        self.dietaryPreference.setItemText(2, _translate("MainWindow", "none"))
        self.remove_diet.setText(_translate("MainWindow", "remove"))
        self.price.setTitle(_translate("MainWindow", "What is the maximum price"))
        self.label_6.setText(_translate("MainWindow", "pesos"))
        self.cafe_address.setText(
            _translate(
                "MainWindow", "Av. Sta. Fe 750, C1006 Cdad. Autónoma de Buenos Aires"
            )
        )

    def re_add_constraint(self):
        selected = self.comboBox.currentText()

        if selected == "Travel Time":
            self.transportation.show()
            self.verticalLayout_2.addWidget(self.transportation)

        elif selected == "Must have wifi":
            if not self.getWifiOptions():
                return False
            self.wifiVar = "yes"
            self.getCafes()
            self.wifi.show()
            self.verticalLayout_2.addWidget(self.wifi)

        elif selected == "Must have power sockets":
            if not self.getSocketOptions():
                return False
            self.socketsVar = "yes"
            self.getCafes()
            self.power_sockets.show()
            self.verticalLayout_2.addWidget(self.power_sockets)

        elif selected == "Dietary Preference":
            self.dietary_pref.show()
            self.verticalLayout_2.addWidget(self.dietary_pref)

        elif selected == "Opening Time":
            days_options = self.getOpenDays()
            if days_options:
                # Clear existing items
                self.daySelect.clear()

                # Add only the available days
                for day in days_options:
                    self.daySelect.addItem(day)

                self.opening_closing.show()
                self.verticalLayout_2.addWidget(self.opening_closing)
            else:
                print("No days available for current constraints")
                return False

    def getOpenDays(self):
        try:
            query = f"findall(DaysOpened, (cafe_query(Cafe, Address, PTTime, WalkTime, TaxiTime, {self.priceVar}, {self.wifiVar}, {self.socketsVar}, {self.veganPreferenceVar}, {self.needsMealsVar}, DaysOpened, ClosingHours, OpeningHours), suitable_cafe(Cafe, {self.transportVar}, {self.maxTimeVar}, {self.priceVar}, {self.wifiVar}, {self.socketsVar}, {self.veganPreferenceVar}, {self.needsMealsVar}, VisitDay, {self.fromVar}, {self.toVar})), L)."
            open_days_result = list(prolog.query(query))

            days = set()
            if open_days_result and "L" in open_days_result[0]:
                days_lists = open_days_result[0]["L"]
                for day_list in days_lists:
                    days.update(day_list)  # Add all days from each list to the set

            return sorted(days)  # Return sorted list of unique days
        except Exception as e:
            print(f"Error getting open days: {e}")
            return []

    def setupDaySelect(self):
        """Set up the day selection combo box with available days."""
        # Clear existing items
        self.daySelect.clear()

        # Add only the days that are in day_options
        for day in self.dayOptions.keys():
            self.daySelect.addItem(day)

        # Set initial time constraints for first day
        if self.dayOptions:
            first_day = self.daySelect.currentText()
            opening_time = self.dayOptions[first_day][0]

            # Create QTime object for opening time
            hours = int(opening_time)
            minutes = int((opening_time % 1) * 60)
            opening_qtime = QtCore.QTime(hours, minutes)

            # Set minimum time for the from_time widget
            self.from_time.setMinimumTime(opening_qtime)

        # Connect day selection change to update time constraints
        self.daySelect.currentTextChanged.connect(self.update_time_constraints)

    def update_time_constraints(self, selected_day):
        """Update time constraints when day selection changes."""
        if selected_day in self.dayOptions:
            opening_time = self.dayOptions[selected_day][0]
            closing_time = self.dayOptions[selected_day][1]

            # Create QTime objects
            hours_open = int(opening_time)
            minutes_open = int((opening_time % 1) * 60)
            opening_qtime = QtCore.QTime(hours_open, minutes_open)

            hours_close = int(closing_time)
            minutes_close = int((closing_time % 1) * 60)
            closing_qtime = QtCore.QTime(hours_close, minutes_close)

            # Set time constraints
            self.from_time.setMinimumTime(opening_qtime)
            self.to_time.setMaximumTime(closing_qtime)

            # If current time is outside valid range, reset to opening time
            if self.from_time.time() < opening_qtime:
                self.from_time.setTime(opening_qtime)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())