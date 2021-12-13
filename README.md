# U.S. Wildfires Analysis using AWS pipeline
The AWS pipeline DataAvengers.pdf contains the step by step tutorial to create a pipeline using AWS services.
ProjectDataSetsCsvs folder contains all the nessecary Csv files that were extracted and transformed for the application.
Python Scripts Folder contains the python code to transform the various weather data csv and merged into a single file. The uploadtoS3.py contains the code to push csv files from ec2 to S3 bucket.
228WeatherMerged script contains the code to apply mapping and drop null vales on the dataset.
228firefinal script contains the code to apply mapping and drop null vales on the dataset.
Lambda_function script contains the code to automatically start the crawler when data has been uploaded to S3 and contains code to send AWS sns email to personal email, everytime the its a success or failure.
