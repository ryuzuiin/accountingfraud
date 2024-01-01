import pandas as pd

def data_reader(data_path, data_format, year_start, year_end):
    temp = pd.read_csv(data_path, header=0)

    data = ()

    if data_format == 'data_default':
        # Filter data for the specified years
        idx = (temp.iloc[:,0] >= year_start) & (temp.iloc[:, 0] <= year_end)
        filtered_data = temp[idx]

        # Extract the required columns
        data['years'] = filtered_data.iloc[:, 0]
        data['firms'] = filtered_data.iloc[:, 1]
        data['paaers'] = filtered_data.iloc[:, 2]
        data['labels'] = filtered_data.iloc[:, 3]
        data['features'] = filtered_data.iloc[:, 4:32]

        data['num_observations'] = data['features'].shape[0]
        data['num_features'] = data['features'].shape[1]


    else:
        print('Error : unsupported data format!')

    print(f'Data Loaded: (data_path), (data["num_features"]) features, (data["num_observations"]) observations.')

    return data

