from config.settings import SETTING_INFO

Querry = ""
member = []

# Setting info
db_sqlite3 = SETTING_INFO.DB_DIR
currentTime = SETTING_INFO.currentTime
conn = SETTING_INFO.conn
cur = conn.cursor()

class Member:
    
    def select_all_member():
        with conn:
            Querry = " select * from auth_user "
            cur.execute(Querry)
            member = cur.fetchall()
            print("[RESULT] QUERRY :",member)
            
            # print(type(member))
            # print(type(member[0]))
            
            # print(member[0])
            # print(member[1])
            
        return member
    
    def select_update_member(id,password, birth, address):
        with conn:
            Querry = " UPDATE auth_user "
            Querry +=" SET "
            Querry +=" password = '"+password+"'"
            Querry +=" birth = '"+birth+"'"
            Querry +=" address = '"+address+"'"
            Querry +=" WHERE id = '"+id+"'"
            cur.execute(Querry)
            member = cur.fetchall()
        return True
        
    def select_delete_member(id):
        data = str(id)
        print("입력데이터 TYPE :", type(data),"  data:",data)
        with conn:
            Querry = " DELETE FROM auth_user WHERE id = "+data
            cur.execute(Querry)
            member = cur.fetchall()
        return True