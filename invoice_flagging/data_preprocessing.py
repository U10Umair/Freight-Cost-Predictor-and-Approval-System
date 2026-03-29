# import sqlite3
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# import joblib

# def load_invoice_data():
#     conn=sqlite3.connect('D:\ML projects\Data\inventory.db')
#     query="""
#     WITH purchase_agg AS (
#     SELECT
#         p.PONumber,
#         COUNT(DISTINCT p.Brand) AS total_brands,
#         SUM(p.Quantity) AS total_item_quantity,
#         SUM(p.Dollars) AS total_item_dollars,
#         AVG(julianday(p.ReceivingDate) - julianday(p.PODate)) AS avg_receiving_delay
#     FROM purchases p
#     GROUP BY p.PONumber
# )

# SELECT
#     vi.PONumber,
#     vi.Quantity AS invoice_quantity,
#     vi.Dollars AS invoice_dollars,
#     vi.Freight,
#     (julianday(vi.InvoiceDate) - julianday(vi.PODate)) AS days_po_to_invoice,
#     (julianday(vi.PayDate) - julianday(vi.InvoiceDate)) AS days_to_pay,
#     pa.total_brands,
#     pa.total_item_quantity,
#     pa.total_item_dollars,
#     pa.avg_receiving_delay
# FROM vendor_invoice vi
# LEFT JOIN purchase_agg pa
# ON vi.PONumber = pa.PONumber
#     """
    
#     df=pd.read_sql_query(query,conn)
#     conn.close()
#     return df

# def create_invoice_risk_label(row):
#      # invoice total mismatch with item level total
#     if (abs(row['invoice_dollars']-row['total_item_dollars'])>5):
#         return 1
#     #  abnormally high receiving delay
#     if row['avg_receiving_delay']>10:
#         return 1
#     return 0

# def apply_labels(df):
#     df['flag_invoice']=df.apply(create_invoice_risk_label,axis=1)
#     return df

# def split_data(df,features,target):
#     X=df[features]
#     y=df[target]
    
#     return train_test_split(
#         X,y,test_size=0.2,random_state=42
#     )
    
# def scale_features(X_train,X_test,scaler_path):
#     scalar=StandardScaler()
#     X_train_scaled=scalar.fit_transform(X_train)
#     X_test_scaled=scalar.transform(X_test)
    
#     joblib.dump(scalar,'models\scaler.pkl')
#     return X_train_scaled,X_test_scaled


import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path


def load_invoice_data():
    conn = sqlite3.connect(r'D:\ML projects\Data\inventory.db')

    query = """
    WITH purchase_agg AS (
        SELECT
            p.PONumber,
            COUNT(DISTINCT p.Brand) AS total_brands,
            SUM(p.Quantity) AS total_item_quantity,
            SUM(p.Dollars) AS total_item_dollars,
            AVG(julianday(p.ReceivingDate) - julianday(p.PODate)) AS avg_receiving_delay
        FROM purchases p
        GROUP BY p.PONumber
    )

    SELECT
        vi.PONumber,
        vi.Quantity AS invoice_quantity,
        vi.Dollars AS invoice_dollars,
        vi.Freight,
        (julianday(vi.InvoiceDate) - julianday(vi.PODate)) AS days_po_to_invoice,
        (julianday(vi.PayDate) - julianday(vi.InvoiceDate)) AS days_to_pay,
        pa.total_brands,
        pa.total_item_quantity,
        pa.total_item_dollars,
        pa.avg_receiving_delay
    FROM vendor_invoice vi
    LEFT JOIN purchase_agg pa
    ON vi.PONumber = pa.PONumber
    """

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def create_invoice_risk_label(row):
    if abs(row['invoice_dollars'] - row['total_item_dollars']) > 5:
        return 1
    if row['avg_receiving_delay'] > 10:
        return 1
    return 0


def apply_labels(df):
    df['flag_invoice'] = df.apply(create_invoice_risk_label, axis=1)
    return df


def split_data(df, features, target):
    X = df[features]
    y = df[target]

    return train_test_split(
        X, y, test_size=0.2, random_state=42
    )


def scale_features(X_train, X_test, scaler_path):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # ✅ create folder if not exists
    Path("models").mkdir(exist_ok=True)

    # ✅ use passed path + safe string
    joblib.dump(scaler, scaler_path)

    return X_train_scaled, X_test_scaled
