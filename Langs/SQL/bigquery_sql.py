# reference by Kaggle(kaggle.com)
import time
from google.cloud import bigquery
from collections import OrderedDict

class PubBigQuery:
    client = bigquery.Client()
    
    def __init__(self, *args, option=False):
        self.option = option
        self.dataset_refs, self.datasets = self.request_dataset(*args)

    def request_dataset(self, *args):
        if self.option:
            try: # inheritance
                args = list(*args)
            except TypeError:
                args = list(args)
            
            assert len(args) <= 3
            dataset_refs = dict([(idx, self.client.dataset(name, project='bigquery-public-data')) for idx, name in enumerate(list(args))])

            # API request
            datasets = OrderedDict()
            for _k, _v in dataset_refs.items():
                datasets[_v.dataset_id] = self.client.get_dataset(_v)
                time.sleep(3)
            return dataset_refs, datasets
        else:
            dataset_ref = {0: self.client.dataset(''.join(*args), project='bigquery-public-data')}
            dataset = {(dataset_ref.get(0)).dataset_id: self.client.get_dataset((dataset_ref.get(0)))}
            return dataset_ref, dataset
        
    def check_table(self):
        for idx, (ref, _dataset) in enumerate(self.datasets.items()):
            print(f"\n{str(idx+1)}. {ref}:")
            for cnt, tables in enumerate(list(self.client.list_tables(_dataset))):
                print(f"\t{str(cnt+1)}: {tables.table_id}")
                
    def request_table(self, path):
        """
        The path's format should be f'\{dataset_idx\}.\{table_name\}'.
        Generally counting number is start from 0 in CS, but use starting from 1 in here.
        """
        path = path.split('.')
        table_ref = (self.dataset_refs.get(int(path[0])-1 if int(path[0]) != 0 else int(path[0]))).table(path[-1])
        table = self.client.get_table(table_ref)
        return table_ref, table

    def check_schema(self, path, by=None):
        """
        The path's format should be f'\{dataset_idx\}.\{table_name\}'.
        Generally counting number is start from 0 in CS, but use starting from 1 in here.
        """
        table_ref, table = self.request_table(path)
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


# inheritance
class QueryResult(PubBigQuery):
    safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
    path = list()

    def __init__(self, *args, option=False):
        super(QueryResult, self).__init__(args, option=option)

    def show_table(self, path):
        _, table = super().request_table(path)
        print(self.client.list_rows(table, max_results=5).to_dataframe().to_markdown())

    # method overriding
    def request_table(self, path, adds=False):
        table_ref, table = super().request_table(path)
        if adds:
            self.path.append(path.split('.'))
        return table_ref, table

######################################################################################################################################
    
    def request_query_result(self, query):
        query_job = self.client.query(query, job_config=self.safe_config)
        return query_job.to_dataframe()
