
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

