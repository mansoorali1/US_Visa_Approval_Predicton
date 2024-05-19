from us_visa.data_access.usvisa_data import USvisaData
from us_visa.entity.config_entity import DataIngestionConfig

data_ingestion_config=DataIngestionConfig()
 
data_ingestion_config = data_ingestion_config

usvisa_data = USvisaData()
dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
                                                        data_ingestion_config.collection_name)


print(dataframe)
