
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="FFMSWASMYSCHOOL",
    database="library_mngmnt_sys",
)

class student:
    def __init__(self):
        pass
    def search_book(self):
        self.search_query='SELECT b.isdn, b.name,a.name,b.status,p.name FROM book b, author a,bk_athr_info bai, publisher p, bk_pblshr_info bpi WHERE b.name like "%"%s"%" and b.location_id=bai.location_id and a.a_id=bai.a_id and b.location_id=bpi.location_id and bpi.p_id=p.p_id'
        self.user_input=input("Enter name of the book")
        print(type(self.user_input))
        self.books=db.cursor()
        self.books.execute(self.search_query,(self.user_input, ))
        self.result=self.books.fetchall()
        for book in self.result:
            print(book)
class admin:
    def __init__(self):
        pass
    def add_book(self):
        self.database=db.cursor()
        self.add_query='INSERT INTO book (location_id,isdn,name,status,edition) VALUES( %s,%s,%s,%s,%s)'
        self.add_author_query='INSERT INTO author (a_id,Name) VALUES(%s,%s)'
        self.add_bk_athr_query='INSERT INTO bk_athr_info (location_id,a_id) VALUES(%s,%s)'
        self.add_bk_pblshr_query = 'INSERT INTO bk_pblshr_info (p_id,location_id) VALUES(%s,%s)'
        self.add_publisher_query='INSERT INTO publisher (p_id,Name) VALUES(%s,%s)'
        self.loc_id=int(input("Enter the location where book will be placed"))
        self.isdn=int(input("Enter the ISDN of book"))
        self.book_name=input("Enter the name of the book")
        self.status=input("What is status of book? Available or Issued")
        self.edition=input("Enter the edition of book")
        self.author_name=input("Author name")
        self.author_id=int(input("Enter author ID"))
        self.publisher=input("Publisher Name")
        self.publisher_id=int(input("Enter publisher ID"))
        self.book_data = (self.loc_id,self.isdn,self.book_name,self.status,self.edition)
        self.author_data=(self.author_id,self.author_name)
        self.publisher_data=(self.publisher_id,self.publisher)
        self.database.execute(self.add_query,self.book_data)
        self.database.execute(self.add_author_query,self.author_data)
        self.database.execute(self.add_bk_athr_query,(self.book_data[0],self.author_data[0],))
        self.database.execute(self.add_publisher_query,self.publisher_data)
        self.database.execute(self.add_bk_pblshr_query,(self.publisher_data[0],self.book_data[0]))
        db.commit()
    def remove_book(self):
        self.database=db.cursor()
        # self.author_info_remove_query='DELETE FROM bk_athr_info bai WHERE bai.location_id=(SELECT b.location_id FROM book b where b.Name=%s  )'
        # self.publisher_info_remove_query='DELETE FROM bk_pblshr_info bpi WHERE bpi.location_id=(SELECT b.location_id FROM book b where b.Name=%s  )'
        self.book_info_remove_query='DELETE FROM book b WHERE b.name=%s'
        self.user_input=input("Enter the name of book you want to delete")
        self.database.execute(self.publisher_info_remove_query,(self.user_input,))
        self.database.execute(self.author_info_remove_query,(self.user_input,))
        self.database.execute(self.book_info_remove_query,(self.user_input,))
        db.commit()


s=student()
a=admin()
# s.search_book()
# a.add_book()
a.remove_book()

