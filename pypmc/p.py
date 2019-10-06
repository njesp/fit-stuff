"""
Docstring
"""
from fitparse import FitFile
import pandas as pd


def load_workout(workout_file):
    """
    Load fitfile and transforms
    it into a pandas Dataframe.
    Nan Values are replaced.
    :param workout_file:
    :return dataframe:
    """
    # Load the fitfile
    fitfile = FitFile(workout_file)

    # This is a ugly hack
    # to avoid timing issues
    while True:
        try:
            fitfile.messages
            break
        except KeyError:
            continue

    # Get all data messages that are of type record
    workout = []
    for record in fitfile.get_messages('record'):
        r = {}
        # Go through all the data entries in this record
        for record_data in record:
            r[record_data.name] = record_data.value

        workout.append(r)
    workout_df = pd.DataFrame(workout)
    workout_df.fillna(method='ffill', inplace=True)
    workout_df.fillna(method='backfill', inplace=True)
    return workout_df


wo = load_workout("c:/Drive/dokumenter/niels/garmin-fit-files/2019-10-05T07_20_32+00_00_4126149379.fit")
print(wo)
