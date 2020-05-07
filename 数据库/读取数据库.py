import pymysql


def get_loan_number(file):
    connect = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="951103",
        db="bugpz",
        charset='utf8'
    )
    print("写入中，请等待……")
    cursor = connect.cursor()
    sql = "select * from zhmm"
    cursor.execute(sql)
    number = cursor.fetchall()
    fp = open('数据库测试.txt', "w")
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        fp.write(loanNumber[0] )
    fp.close()
    cursor.close()
    connect.close()
    print("写入完成,共写入%d条数据……" % loan_count)


if __name__ == "__main__":
    file = r"G:\BUGPZ\数据库\数据库测试.txt"
    get_loan_number(file)