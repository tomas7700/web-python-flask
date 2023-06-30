from sqlalchemy import create_engine, text
import os

db_string = os.environ.get('KEY_DB')
engine = create_engine(
    db_string, 
    connect_args={
    'ssl':{
         "ssl_ca": "/etc/ssl/cert.pem"

    }
})



with engine.connect() as conn:
    results = conn.execute(text('SELECT * FROM user_log_info'))
    final_result = []
    for row in results.all():
          final_result.append(row._asdict())

    print(final_result)

def user_info_capture():
    with engine.connect() as conn:
        results = conn.execute(text('SELECT * FROM user_log_info'))
        final_result = []
        for row in results.all():
          final_result.append(row._asdict())
        return final_result



