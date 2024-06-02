from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 query="",
                 mode="",
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.table=table
        self.query=query
        self.mode=mode
        # Map params here
        # Example:
        # self.conn_id = conn_id

    def execute(self, context):
        self.log.info("Use HOOk to get interface")
        redshift=PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Base on mode (truncate the table) and start loading data")
        if self.mode=="delete_load":
            redshift.run(f"TRUNCATE TABLE {self.table}")
        redshift.run(f"INSERT INTO {self.table} {self.query}")
        
        
        
        