# reference by Kaggle(kaggle.com)
import time
from google.cloud import bigquery

class PubBigQuery:
    client = bigquery.Client()
    
    def __init__(self, option=False):
        self.option = option

    def request_dataset(self, *args):
        if self.option:
            assert len(args) <= 3
            dataset_refs = dict([(idx, self.client.dataset(name, project='bigquery-public-data')) for idx, name in enumerate(args)])

            # API request
            datasets = dict()
            for _k, _v in dataset_refs.items():
                datasets[_k] = self.client.get_dataset(_v)
                time.sleep(3)
            return dataset_refs, datasets
        else:
            dataset_ref = self.client.dataset(''.join(args), project='bigquery-public-data')
            dataset = self.client.get_dataset(dataset_ref)
            return dataset_ref, dataset

######################################################################################################################################
        
    def check_table(self):
        print()
        
    def request_table(self):
        # 
        return table_ref, table
