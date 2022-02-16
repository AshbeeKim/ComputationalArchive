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
        
    def check_table(self):
        for idx, (ref, _dataset) in enumerate(self.datasets.items()):
            print(f"\n{str(idx+1)}. {ref}:")
            for cnt, tables in enumerate(list(self.client.list_tables(_dataset))):
                print(f"\t{str(cnt+1)}: {tables.table_id}\n")

    def check_schema(self, path, by=None):
        path = path.split('.')
        table_ref = (self.dataset_refs.get(int(path[0]))).table(path[-1])
        table = self.client.get_table(table_ref)
        cnt = 0
        if by is None:
            for scm in list(table.schema):
                print(f'Schema : {scm}')
                cnt += 1
        else:
            for scm in list(table.schema):
                if scm.field_type == by.upper():
                    print(f'Schema : {scm}')
                    cnt += 1
        print(f'\nTotal Schema by "{by.upper() if by is not None else "None"}": {cnt}')

######################################################################################################################################

    def request_table(self):
        # 
        return table_ref, table
