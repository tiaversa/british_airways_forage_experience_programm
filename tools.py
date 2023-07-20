def add_file_to_s3(local_file_path):
    session = boto3.Session(profile_name='s3_dev')
    #instantiating client
    client = session.client('s3')
    #set variables
    bucket = 'british-airways-project'
    cur_path = os.getcwd()
    filename = os.path.join(cur_path,local_file_path)
    file = filename.split('/')[-1]
    #open the file
    data = open(filename,'rb')
    client.upload_file(filename,bucket,file)
    print(f'File {file} updated successfully to {bucket}.')