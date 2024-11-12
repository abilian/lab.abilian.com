
[Apache Airflow](https://airflow.apache.org/) is a popular and powerful open-source platform used to programmatically author, schedule, and monitor workflows. It is designed to handle complex data pipelines and dependencies between tasks. It is built on Python and allows you to define your workflows using Python code.

## Key features

1. **Directed Acyclic Graph (DAG) based workflows**: Airflow represents workflows as DAGs, ensuring tasks run in a specific order without cycles.
2. **Extensible**: Airflow provides a rich ecosystem of operators, hooks, and executors that can be extended to meet custom requirements.
3. **Scalable**: Airflow can distribute tasks across multiple worker nodes, allowing it to handle large-scale workflows.
4. **Web-based UI**: Airflow comes with a web-based UI for monitoring and managing workflows, providing detailed information about task status, logs, and more.
5. **Integration**: Airflow can easily integrate with various databases, APIs, and other data sources.

## Installation

To install Apache Airflow, use the following command (it is recommended to do this inside a virtual environment):
```
pip install apache-airflow
```

Or:
```
pipx install apache-airflow
```

## Example usage

To get started with Apache Airflow, you need to create a Python script to define a DAG with its tasks and dependencies. Here's a simple example:

```python
# dags/example_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print("Hello from the task!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

start_task = DummyOperator(task_id='start_task', dag=dag)
hello_task = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> hello_task >> end_task
```

After defining the DAG, you need to place the Python script in the `dags` folder of your Airflow installation. By default, Airflow will look for DAGs in the `$HOME/dags` directory.

Then you will need to initialize Airflow's database (by default, a SQLite DB):

```
airflow db init
airflow users create --username admin --role Admin -e sf@example.com -f stefane -l fermigier
```

Finally, start the Airflow webserver and scheduler with the following commands (in separate terminal windows):

```
airflow webserver --port 8080
airflow scheduler
```

You should now be able to access the Airflow web UI at `http://localhost:8080` and see your example DAG listed.

## More detailed tutorials

- https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html


## Alternatives

- [[Prefect]]

<!-- Keywords -->
#workflows
<!-- /Keywords -->
