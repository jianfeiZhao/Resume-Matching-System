import pyodbc,csv

server = "bigdatacsy.database.windows.net"
user = "sam"
password = "NYUBigData!"
db = "bigdata_db"
driver= '{ODBC Driver 17 for SQL Server}'

class LoadData:
    def __init__(self):
        self.db = pyodbc.connect(
            'DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + db + ';UID=' + user + ';PWD=' + password)
        self.cur = self.db.cursor()
        #self.job = ''
        self.job_details = []
    """
    def load_data(self):
        query = "select * from job_info where job_query = ?"
        self.cur.execute(query,self.job)
        result = self.cur.fetchall()
        for item in result:
            self.job_details.append(item)
    """
    def load_data(self):
        query = "select * from job_info_no_dup"
        self.cur.execute(query)
        result = self.cur.fetchall()
        for item in result:
            self.job_details.append(item)

    def write_csv(self):
        with open("jobs.csv", "w",newline='',encoding='utf-8-sig',errors='ignore') as f:
            print('writing in csv...')
            w = csv.writer(f)
            w.writerow(('id','job','title','company','location','description'))
            w.writerows(self.job_details)

    def main(self):
        #self.job += input('Input job:')
        self.load_data()
        self.write_csv()


if __name__ == '__main__':
    ld = LoadData()
    ld.main()