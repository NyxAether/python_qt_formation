from typing import Any, Optional, Union
import pandas as pd
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QDateTime
from PySide6.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data: "pd.DataFrame[QDateTime,str]") -> None:
        QAbstractTableModel.__init__(self)
        self.df = data
        self.__rows=self.df.shape[0]
        self.__columns=self.df.shape[1]

    def rowCount(self, parent = QModelIndex()) -> int:
        return self.__rows
    
    def columnCount(self, parent = QModelIndex()) -> int:
        return self.__columns
    
    def headerData(self, section: int, orientation, role: int) -> Any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.df.columns[section]
        else:
            return f"{section}"
    
    def data(self, index: QModelIndex, role = Qt.DisplayRole) -> Any:
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            
            if column == 0:
                date = self.df.iloc[row, column].toPython()
                return str(date)[:-3]
            elif column == 1:
                magnitude = self.df.iloc[row, column]
                return f"{magnitude:.2f}"
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None
