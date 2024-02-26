from snowflake.core import Root
from snowflake.snowpark import Session

connection_params = {
    "account": "<your snowflake account>",
    "user": "<your snowflake user>",
    "password": "<your snowflake password>",
    "role": "<snowflake user role>",
    "warehouse": "<snowflake warehouse>",
    "database": "<snowflake database>",
    "schema": "<snowflake schema>"
}
#Here the <> encoded should be credentials

session = Session.builder.configs(connection_params).create()
#df = session.create_dataframe([[1, 2], [3, 4]], schema=["a", "b"])
#df = df.filter(df.a > 1)
#df.show()
#pandas_df = df.to_pandas()  # this requires pandas installed in the Python environment
#result = df.collect()

root_connection = Root(session)

#Task Creationg
from snowflake.core.task import Task
from datetime import timedelta
task = Task(
        'bloomberg',definition = 'select 1',schedule=timedelta(hours=1))
)

#schema informations
schema = root_connection.databases["sample_db"].schemas['public']
print(schema.name)
print(schema.datbase.name)

task_reference = schema.tasks.create(task)
print(task.name)
print(task.fetch())
print(task.schedule)
print(task.schema_name)
print(task.fully_qualified_name)
#some functions
#task.resume()
#task.suspend()
#task.execute()


