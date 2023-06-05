import json
import os

import pandas as pd


def convert_json_to_csv(json_filename):
    with open(json_filename, encoding='utf-8') as input_file:
        json_content = json.load(input_file)

    data_frame = pd.DataFrame(json_content)

    configs = []
    for i, item in enumerate(pd.DataFrame(json_content)['configurations']):
        configs.append({
            'Resource_Id': item['origin_id'],
            'Config_Key': data_frame.index[i],
            'Config_Value': item['value'],
            'Do_Encrypt': item['encrypted']
        })

    csv_filename = os.path.splitext(json_filename)[0] + '.csv'
    pd.DataFrame(configs).to_csv(csv_filename, encoding='utf-8', index=False)


if __name__ == '__main__':
    # Change filename to whatever your local filename is.
    # filename = '../baskin_prod.json'
    filename = '../current-preprod-config.json'
    convert_json_to_csv(filename)
