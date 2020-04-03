import pandas as pd
import json

baseloc = '/mnt/c/Users/AHolm/Work Folders/Documents/Maps/Affiliates/'

csv = 'SEIA Affiliate Contact Information for Website.csv'
geojson = 'SEIA_StateAffiliates.geojson'

def merge_data_into_json():
  df = pd.read_csv(baseloc + csv)
  with open(baseloc + geojson) as file:
    json_file = json.load(file)
    #for k, v in json_file['features'].items():
      #print(f"Key: {k}    Value: {v}")
    for item in json_file['features']:
      #print(f"Item: {item['properties']}")
      #for k, v in item['properties'].items():
      #  print(f"Key: {k}    Value: {v}")
      state = item['properties']['NAME']
      if(state in df['state_full'].unique().tolist()):
        tmp_df = df[df['state_full'] == state]
        item['properties']['affiliate'] = std_value(tmp_df['affiliate'].iloc[0])
        item['properties']['affiliate_state'] = std_value(tmp_df['affiliate_state'].iloc[0])
        item['properties']['latitude'] = std_value(tmp_df['latitude'].iloc[0])
        item['properties']['longitude'] = std_value(tmp_df['longitude'].iloc[0])
        item['properties']['street'] = std_value(tmp_df['street'].iloc[0])
        item['properties']['city'] = std_value(tmp_df['city'].iloc[0])
        item['properties']['state'] = std_value(tmp_df['state'].iloc[0])
        item['properties']['zipcode'] = std_value(tmp_df['zipcode'].iloc[0])
        item['properties']['contact_name'] = std_value(tmp_df['contact_name'].iloc[0])
        item['properties']['contact_role'] = std_value(tmp_df['contact_role'].iloc[0])
        item['properties']['contact_phone'] = std_value(tmp_df['contact_phone'].iloc[0])
        item['properties']['contact_email'] = std_value(tmp_df['contact_email'].iloc[0])
        item['properties']['website'] = std_value(tmp_df['website'].iloc[0])
        item['properties']['contact_name2'] = std_value(tmp_df['contact_name2'].iloc[0])
        item['properties']['contact_role2'] = std_value(tmp_df['contact_role2'].iloc[0])
        item['properties']['contact_phone2'] = std_value(tmp_df['contact_phone2'].iloc[0])
        item['properties']['contact_email2'] = std_value(tmp_df['contact_email2'].iloc[0])
      else:
        print("State not in df")
  json.dump(json_file, open(baseloc+geojson, 'w'))
  return

def std_value(a_var):
  if(pd.notnull(a_var)):
    ret_val = a_var
  else:
    ret_val = None
  return ret_val

if __name__ == '__main__':
  merge_data_into_json()
