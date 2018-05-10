/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGroupBox *horizontalGroupBox;
    QGridLayout *gridLayout_2;
    QSpacerItem *horizontalSpacer_2;
    QLabel *label_3;
    QPushButton *pushButton;
    QLineEdit *lineEdit;
    QPushButton *pushButton_3;
    QPushButton *pushButton_2;
    QLabel *label;
    QLabel *label_2;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_4;
    QSpacerItem *verticalSpacer;
    QLabel *label_4;
    QLabel *label_5;
    QTextEdit *textEdit;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(749, 318);
        MainWindow->setMinimumSize(QSize(749, 314));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setMinimumSize(QSize(749, 304));
        horizontalGroupBox = new QGroupBox(centralWidget);
        horizontalGroupBox->setObjectName(QStringLiteral("horizontalGroupBox"));
        horizontalGroupBox->setGeometry(QRect(0, 50, 501, 251));
        gridLayout_2 = new QGridLayout(horizontalGroupBox);
        gridLayout_2->setSpacing(5);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        gridLayout_2->setSizeConstraint(QLayout::SetDefaultConstraint);
        gridLayout_2->setContentsMargins(5, 5, 5, 5);
        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 0, 1, 1, 1);

        label_3 = new QLabel(horizontalGroupBox);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout_2->addWidget(label_3, 5, 0, 1, 1);

        pushButton = new QPushButton(horizontalGroupBox);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        gridLayout_2->addWidget(pushButton, 6, 1, 1, 1);

        lineEdit = new QLineEdit(horizontalGroupBox);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        gridLayout_2->addWidget(lineEdit, 2, 2, 1, 1);

        pushButton_3 = new QPushButton(horizontalGroupBox);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));

        gridLayout_2->addWidget(pushButton_3, 0, 2, 1, 1);

        pushButton_2 = new QPushButton(horizontalGroupBox);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));

        gridLayout_2->addWidget(pushButton_2, 5, 2, 1, 1);

        label = new QLabel(horizontalGroupBox);
        label->setObjectName(QStringLiteral("label"));

        gridLayout_2->addWidget(label, 0, 0, 1, 1);

        label_2 = new QLabel(horizontalGroupBox);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_2->addWidget(label_2, 2, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 2, 1, 1, 1);

        pushButton_4 = new QPushButton(horizontalGroupBox);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));

        gridLayout_2->addWidget(pushButton_4, 3, 2, 1, 1);

        verticalSpacer = new QSpacerItem(0, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_2->addItem(verticalSpacer, 4, 1, 1, 1);

        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(180, 0, 291, 51));
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(590, 10, 41, 31));
        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        textEdit->setGeometry(QRect(510, 50, 221, 221));
        MainWindow->setCentralWidget(centralWidget);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "Import .GPX file with geolocaiton", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "Ready", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "Select File", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "Select File", nullptr));
        label->setText(QApplication::translate("MainWindow", "Import the .TCX file", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "Enter the correct distance (in meters)", nullptr));
        pushButton_4->setText(QApplication::translate("MainWindow", "Fix", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#0bbeff;\">Garmin Activity Tool</span></p></body></html>", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Log</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
