import boto3
try:
    s3_resource = boto3.resource('s3')
    bucket_name = 'bucket228s3'
    fires_data_file_path = 'ProjectDataSets/18m_fires_final.csv'
    WeatheDataFilePath = 'ProjectDataSets/HourlyWeatherData_Merged.csv'
    s3_resource.meta.client.upload_file(fires_data_file_path,bucket_name,'Fires/18m_fires_final.csv')
    s3_resource.meta.client.upload_file(WeatheDataFilePath,bucket_name,'HourlyWeather/HourlyWeatherData_Merged.csv')
    print('All files uploaded succesfully to S3 bucket')
except BaseException as e:
    print(e)
   