# 20220783_정준호.py
# 도서 관리 프로그램 (단순 연결 리스트)

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.book_id}\t{self.title}\t{self.author}\t{self.year}"

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, book):
        new_node = Node(book)
        if self.head == None:
            self.head = new_node
        else:
            p = self.head
            while p.link != None:
                p = p.link
            p.link = new_node

    def find_by_title(self, title):
        p = self.head
        while p != None:
            if p.data.title == title:
                return p.data
            p = p.link
        return None

    def find_by_id(self, book_id):
        p = self.head
        while p != None:
            if p.data.book_id == book_id:
                return p.data
            p = p.link
        return None

    def find_pos_by_title(self, title):
        prev = None
        p = self.head
        while p != None:
            if p.data.title == title:
                return prev, p
            prev = p
            p = p.link
        return None, None

    def delete_by_title(self, title):
        prev, p = self.find_pos_by_title(title)
        if p == None:
            return False
        if prev == None:
            self.head = p.link
        else:
            prev.link = p.link
        return True

    def get_all_books(self):
        books = []
        p = self.head
        while p != None:
            books.append(p.data)
            p = p.link
        return books


class BookManagement:
    def __init__(self):
        self.list = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.list.find_by_id(book_id):
            print("이미 있는 책 번호입니다.")
            return
        if self.list.find_by_title(title):
            print("이미 있는 책 제목입니다.")
            return
        b = Book(book_id, title, author, year)
        self.list.append(b)
        print("도서 추가 완료!")

    def remove_book(self, title):
        if self.list.delete_by_title(title):
            print("도서 삭제 완료!")
        else:
            print("그런 제목의 책은 없습니다.")

    def search_book(self, title):
        b = self.list.find_by_title(title)
        if b:
            print("책 번호:", b.book_id)
            print("제목:", b.title)
            print("저자:", b.author)
            print("출판연도:", b.year)
        else:
            print("그런 제목의 책이 없습니다.")

    def display_books(self):
        books = self.list.get_all_books()
        if len(books) == 0:
            print("현재 등록된 도서가 없습니다.")
        else:
            print("\n번호\t제목\t저자\t출판연도")
            for b in books:
                print(b)
            print()

    def run(self):
        while True:
            print("\n==== 도서 관리 프로그램 ====")
            print("1. 도서 추가")
            print("2. 도서 삭제(책 제목)")
            print("3. 도서 조회(책 제목)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")

            sel = input("메뉴 선택: ")

            if sel == "1":
                try:
                    book_id = int(input("책 번호: "))
                    title = input("책 제목: ")
                    author = input("저자: ")
                    year = int(input("출판 연도: "))
                    self.add_book(book_id, title, author, year)
                except:
                    print("입력 오류입니다.")
            elif sel == "2":
                title = input("삭제할 책 제목: ")
                self.remove_book(title)
            elif sel == "3":
                title = input("조회할 책 제목: ")
                self.search_book(title)
            elif sel == "4":
                self.display_books()
            elif sel == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")


if __name__ == "__main__":
    m = BookManagement()
    m.run()