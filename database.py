from sqlalchemy import create_engine, text
db_string = 'mysql+pymysql://b2dp0z2ds9xocq9vbt3k:pscale_pw_8PAOHHHkLt50RYPMFyrcDZrtqINJlfuoEIYJbQN2Pma@aws.connect.psdb.cloud/indevo?charset=utf8mb4'
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
