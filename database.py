from sqlalchemy import create_engine, text
from collections import defaultdict

import os


KEY  = os.environ.get('KEY_DB')
string_key = str(KEY)
db_string = 'mysql+pymysql://63dp0wrpbxdb8o98y9t2:'+ string_key +'@aws.connect.psdb.cloud/indevo?charset=utf8mb4'
engine = create_engine(
    db_string, 
    connect_args={
    'ssl':{
         "ssl_ca": "/etc/ssl/cert.pem"

    }
})



def user_info_capture():
    with engine.connect() as conn:
        results = conn.execute(text('SELECT * FROM user_log_info'))
        final_result = []
        for row in results.all():
          final_result.append(row._asdict())
        return final_result


def load_info(id):
    with engine.connect() as conn:
    
        results = conn.execute( text("SELECT * FROM user_log_info WHERE id = """+ id))
        rows = results.fetchall()
        if len(rows) == 0:
            return None
        else:
            return rows
