# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KairoSightWidgetImagePrep.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetImagePrep(object):
    def setupUi(self, WidgetImagePrep):
        WidgetImagePrep.setObjectName("WidgetImagePrep")
        WidgetImagePrep.resize(350, 211)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetImagePrep.sizePolicy().hasHeightForWidth())
        WidgetImagePrep.setSizePolicy(sizePolicy)
        WidgetImagePrep.setMaximumSize(QtCore.QSize(350, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetImagePrep)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelSource = QtWidgets.QLabel(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSource.sizePolicy().hasHeightForWidth())
        self.labelSource.setSizePolicy(sizePolicy)
        self.labelSource.setTextFormat(QtCore.Qt.PlainText)
        self.labelSource.setObjectName("labelSource")
        self.horizontalLayout_2.addWidget(self.labelSource)
        self.comboBoxSource = QtWidgets.QComboBox(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSource.sizePolicy().hasHeightForWidth())
        self.comboBoxSource.setSizePolicy(sizePolicy)
        self.comboBoxSource.setObjectName("comboBoxSource")
        self.horizontalLayout_2.addWidget(self.comboBoxSource)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelPreps = QtWidgets.QLabel(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPreps.sizePolicy().hasHeightForWidth())
        self.labelPreps.setSizePolicy(sizePolicy)
        self.labelPreps.setTextFormat(QtCore.Qt.PlainText)
        self.labelPreps.setObjectName("labelPreps")
        self.horizontalLayout_5.addWidget(self.labelPreps)
        self.comboBoxPreps = QtWidgets.QComboBox(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPreps.sizePolicy().hasHeightForWidth())
        self.comboBoxPreps.setSizePolicy(sizePolicy)
        self.comboBoxPreps.setObjectName("comboBoxPreps")
        self.comboBoxPreps.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxPreps)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxTransform = QtWidgets.QGroupBox(WidgetImagePrep)
        self.groupBoxTransform.setObjectName("groupBoxTransform")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxTransform)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxApplyTransform = QtWidgets.QCheckBox(self.groupBoxTransform)
        self.checkBoxApplyTransform.setCheckable(True)
        self.checkBoxApplyTransform.setTristate(False)
        self.checkBoxApplyTransform.setObjectName("checkBoxApplyTransform")
        self.verticalLayout_3.addWidget(self.checkBoxApplyTransform)
        self.formLayoutTransform = QtWidgets.QFormLayout()
        self.formLayoutTransform.setObjectName("formLayoutTransform")
        self.rotateLabel = QtWidgets.QLabel(self.groupBoxTransform)
        self.rotateLabel.setWordWrap(True)
        self.rotateLabel.setObjectName("rotateLabel")
        self.formLayoutTransform.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rotateLabel)
        self.rotateComboBox = QtWidgets.QComboBox(self.groupBoxTransform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotateComboBox.sizePolicy().hasHeightForWidth())
        self.rotateComboBox.setSizePolicy(sizePolicy)
        self.rotateComboBox.setMinimumSize(QtCore.QSize(5, 0))
        self.rotateComboBox.setObjectName("rotateComboBox")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.formLayoutTransform.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rotateComboBox)
        self.verticalLayout_3.addLayout(self.formLayoutTransform)
        self.horizontalLayout_3.addWidget(self.groupBoxTransform)
        self.groupBoxRemoveBackground = QtWidgets.QGroupBox(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRemoveBackground.sizePolicy().hasHeightForWidth())
        self.groupBoxRemoveBackground.setSizePolicy(sizePolicy)
        self.groupBoxRemoveBackground.setObjectName("groupBoxRemoveBackground")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxRemoveBackground)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBoxApplyRemoveBackground = QtWidgets.QCheckBox(self.groupBoxRemoveBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxApplyRemoveBackground.sizePolicy().hasHeightForWidth())
        self.checkBoxApplyRemoveBackground.setSizePolicy(sizePolicy)
        self.checkBoxApplyRemoveBackground.setObjectName("checkBoxApplyRemoveBackground")
        self.verticalLayout_4.addWidget(self.checkBoxApplyRemoveBackground)
        self.formLayoutRemoveBackground = QtWidgets.QFormLayout()
        self.formLayoutRemoveBackground.setObjectName("formLayoutRemoveBackground")
        self.thresholdLabel = QtWidgets.QLabel(self.groupBoxRemoveBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdLabel.sizePolicy().hasHeightForWidth())
        self.thresholdLabel.setSizePolicy(sizePolicy)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.formLayoutRemoveBackground.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thresholdLabel)
        self.thresholdSpinBox = QtWidgets.QSpinBox(self.groupBoxRemoveBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdSpinBox.sizePolicy().hasHeightForWidth())
        self.thresholdSpinBox.setSizePolicy(sizePolicy)
        self.thresholdSpinBox.setMaximum(99999)
        self.thresholdSpinBox.setObjectName("thresholdSpinBox")
        self.formLayoutRemoveBackground.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thresholdSpinBox)
        self.minSizeLabel = QtWidgets.QLabel(self.groupBoxRemoveBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minSizeLabel.sizePolicy().hasHeightForWidth())
        self.minSizeLabel.setSizePolicy(sizePolicy)
        self.minSizeLabel.setObjectName("minSizeLabel")
        self.formLayoutRemoveBackground.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.minSizeLabel)
        self.minSizeSpinBox = QtWidgets.QSpinBox(self.groupBoxRemoveBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.minSizeSpinBox.setSizePolicy(sizePolicy)
        self.minSizeSpinBox.setMaximum(150)
        self.minSizeSpinBox.setObjectName("minSizeSpinBox")
        self.formLayoutRemoveBackground.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.minSizeSpinBox)
        self.verticalLayout_4.addLayout(self.formLayoutRemoveBackground)
        self.horizontalLayout_3.addWidget(self.groupBoxRemoveBackground)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(WidgetImagePrep)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Discard)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(WidgetImagePrep)
        QtCore.QMetaObject.connectSlotsByName(WidgetImagePrep)

    def retranslateUi(self, WidgetImagePrep):
        _translate = QtCore.QCoreApplication.translate
        WidgetImagePrep.setWindowTitle(_translate("WidgetImagePrep", "Image Prep"))
        self.labelSource.setText(_translate("WidgetImagePrep", "Source:"))
        self.labelPreps.setText(_translate("WidgetImagePrep", "Prep:"))
        self.comboBoxPreps.setItemText(0, _translate("WidgetImagePrep", "*New*"))
        self.groupBoxTransform.setTitle(_translate("WidgetImagePrep", "Transform"))
        self.checkBoxApplyTransform.setText(_translate("WidgetImagePrep", "Apply"))
        self.rotateLabel.setText(_translate("WidgetImagePrep", "Rotate (° Clockwise)"))
        self.rotateComboBox.setItemText(0, _translate("WidgetImagePrep", "45"))
        self.rotateComboBox.setItemText(1, _translate("WidgetImagePrep", "90"))
        self.rotateComboBox.setItemText(2, _translate("WidgetImagePrep", "135"))
        self.rotateComboBox.setItemText(3, _translate("WidgetImagePrep", "180"))
        self.rotateComboBox.setItemText(4, _translate("WidgetImagePrep", "225"))
        self.rotateComboBox.setItemText(5, _translate("WidgetImagePrep", "270"))
        self.rotateComboBox.setItemText(6, _translate("WidgetImagePrep", "315"))
        self.groupBoxRemoveBackground.setTitle(_translate("WidgetImagePrep", "Remove Background"))
        self.checkBoxApplyRemoveBackground.setText(_translate("WidgetImagePrep", "Apply"))
        self.thresholdLabel.setText(_translate("WidgetImagePrep", "Threshold"))
        self.minSizeLabel.setText(_translate("WidgetImagePrep", "Min. Size"))

