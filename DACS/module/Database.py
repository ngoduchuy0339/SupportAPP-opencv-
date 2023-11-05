import pyodbc


# kết nối cơ sở dữ liệu sử dụng pyodbc

def Server_1(ip):

    server = 'DESKTOP-DT03IGN\SQLEXPRESS'
    database = 'SHOP'

    con = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + '; Trusted_connection=yes;')
    cursor = con.cursor()
    return cursor
