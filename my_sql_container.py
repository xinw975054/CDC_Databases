import os
import sys
import pymysql

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='413426Txwd!',
        host='127.0.0.1')

    # create cursor
    cursor = cnx.cursor()

    cnx.commit()
    cursor.close()
    cnx.close()    

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     

# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    sys.exit()

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 5600:5600 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    sys.exit()

# if -init
if(argument == '-init'):
    init_mysql()
    sys.exit()