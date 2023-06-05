import argparse
import sys
import pandas as pd
from PySide6 import QtWidgets
from PySide6.QtCore import QTimeZone, QDateTime

from main_window import MainWindow
from python_qt_formation.container_widget import Widget


def transform_date(utc_time: str, timezone: None | QTimeZone = None) -> QDateTime:
    """Transform the date/time provided in the file as an str using utc into
    an Object QDateTime from the correct timezone

    Args:
        utc_time (str): time represented with the format `yyyy-MM-ddTHH:mm:ss.zzzZ`
        timezone (None | QTimeZone, optional): String defining the time zone.
        Defaults to None.

    Returns:
        QDateTime: Input time transformed accordingly with `timezone`
    """
    utc_format = "yyyy-MM-ddTHH:mm:ss.zzzZ"
    new_date = QDateTime().fromString(utc_time, utc_format)
    if timezone:
        new_date.setTimeZone(timezone)
    return new_date


def read_earthquake_data(
    data_fname: str,
) -> "pd.DataFrame[QDateTime, str]":  # type: ignore
    """Read the earthquake data file and return only the magnitude and the time

    Args:
        data_fname (str): Path to the data file

    Returns:
        Tuple[pd.Series[str], pd.Series[QDateTime]]: Magnitude and time of
        the observed magnitude
    """
    df = pd.read_csv(data_fname)
    df = df[df.mag >= 0]

    timezone = QTimeZone(b"Europe/Paris")

    df["times"] = df["time"].apply(transform_date, args=(timezone,))  # type: ignore
    return df[["times", "mag"]]


if __name__ == "__main__":
    option = argparse.ArgumentParser()
    option.add_argument("-f", "--file", type=str, required=True)
    args = option.parse_args()
    data = read_earthquake_data(args.file)

    app = QtWidgets.QApplication(sys.argv)
    widget = Widget(data)
    main_w = MainWindow(widget)
    main_w.show()
    sys.exit(app.exec())
