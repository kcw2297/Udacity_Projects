from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 check_sql="check_sql_general",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.table=table
        self.check_sql=check_sql

    def execute(self, context):
        self.log.info("Use Hook to get interface")
        redshift=PostgresHook(self.redshift_conn_id)
        dq_checks=[
            {self.check_sql : "SELECT COUNT(*) FROM users WHERE userid is null", 'expected_result': 0},
        {self.check_sql : "SELECT COUNT(*) FROM songs WHERE songid is null", 'expected_result': 0},
        {self.check_sql : "SELECT COUNT(*) FROM artists WHERE artist_id is null", 'expected_result': 0},
        {self.check_sql : "SELECT COUNT(*) FROM time WHERE start_time is null", 'expected_result': 0}]
        
        self.log.info("Start data quality check")
        for table in self.table:
            for check in dq_checks:
                sql = check.get(self.check_sql, None)
                exp_result = check.get('expected_result', None)
                if sql is not None:
                    records = redshift.get_records(sql)[0]
                    if records ==exp_result:
                        raise ValueError(f"Data quality check failed. {table} returned no results")
                
        
     
        
