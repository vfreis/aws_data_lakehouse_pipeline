def validate_dataframe(df):

    if df.count() == 0:
        raise Exception("Empty dataset detected")

    if df.dropDuplicates().count() != df.count():
        print("Duplicates detected")