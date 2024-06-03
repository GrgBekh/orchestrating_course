from airflow.decorators import dag, task
from datetime import datetime, timedelta
import numpy as np

default_args = {
    'owner' : 'admin',
    'retries' : 2,
    'retry_delay' : timedelta(minutes=1)
}

@dag(dag_id = 'dag_for_dot_product_v1.0',
     default_args=default_args,
     start_date=datetime(2023, 10, 26),
     schedule_interval='@daily'
     )
def dot_computation():

    @task()
    def get_first_vec():
        vec_1 = list(np.random.normal(loc = 1, scale = 0.5, size = 10))
        #vec_1 = 10
        return vec_1
    
    @task()
    def get_second_vec():
        vec_2 = list(np.random.rand(10))
        #vec_2 = 5
        return vec_2
    
    @task()
    def print_dot_product(vec_1, vec_2):
        vec_1_np = np.array(vec_1)
        vec_2_np = np.array(vec_2)
        print(f"dot product of vec_1 and vec_2 equal to {np.sum(vec_1_np*vec_2_np)}")
    
    vec_1 = get_first_vec()
    vec_2 = get_second_vec()
    print_dot_product(vec_1, vec_2)

my_dag = dot_computation()