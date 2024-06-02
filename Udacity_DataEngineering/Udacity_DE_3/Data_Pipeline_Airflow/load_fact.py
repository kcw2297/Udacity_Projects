from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 query="",
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id,
        self.table=table,
        self.query=query
        # Map params here
        # Example:
        # self.conn_id = conn_id

    def execute(self, context):
        self.log.info("Using Hook to get interface")
        redshift=PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Query the sql to insert data to fact_table")
        redshift.run(f"INSERT INTO {self.table} {self.query}")
        
        
        
