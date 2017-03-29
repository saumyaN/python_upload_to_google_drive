from extensions import db
import constants


def get_data():
    from manage import app
    with app.app_context():
        engine = db.get_engine(app, bind='dgtech')
        account_invoice_query = constants.SQL_QUERY
        print(account_invoice_query)
        dbcopy_f = open('/tmp/dgtech.csv', 'wb')
        fake_conn = engine.raw_connection()
        fake_cur = fake_conn.cursor()
        fake_cur.copy_expert(account_invoice_query, dbcopy_f)