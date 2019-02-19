import json
import os
from tqdm import tqdm

def df2squad(df, version='v2.0', output_dir=None):
   """
   Converts a pandas dataframe with columns ['title', 'content'] to a json file with SQuAD format.

   Arguments:
       df {pd.DataFrame} -- a pandas dataframe with columns ['title', 'content']
       version {string} -- the SQuAD dataset version format

   Keyword Arguments:
       output_dir {string} -- Enable export of output (default: {None})

   Returns:
       json_data -- A json object with SQuAD format
   """

   json_data = {}
   json_data['version'] = version
   json_data['data'] = []

   for index, row in tqdm(df.iterrows()):
       temp = {'title': row['title'],
               'paragraphs': []}
       for paragraph in row['paragraphs']:
           temp['paragraphs'].append({'context': paragraph,
                                      'qas': []})
       json_data['data'].append(temp)

   if output_dir:
       with open(os.path.join(output_dir, 'custom-{}.json'.format(version)), 'w') as outfile:
           json.dump(json_data, outfile)

   return json_data
