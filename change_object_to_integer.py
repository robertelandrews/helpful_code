# change 'object' column type to numerical value (either float or int)
# pandas required

# check whether pandas is installed
import pandas as pd

def change_obj_to_int(df, col_list):
    '''
    df (df): pandas DataFrame
    collist (list): list of columns you'd like to change
    '''
    try:
        df[col_list].astype(str).astype(int)
    except:
        Exception as e:
        # Handle the exception and print the error message
        print(f"An error occurred: {e}")
        exit()