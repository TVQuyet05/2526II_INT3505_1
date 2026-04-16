from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    published_year = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year
        }

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

DB_PATH = 'sqlite:///library.db'

def get_engine(db_path=DB_PATH):
    # check_same_thread=False cần thiết cho SQLite trong web framework để tránh lỗi Thread
    return create_engine(db_path, connect_args={"check_same_thread": False})

def init_db(db_path=DB_PATH):
    engine = get_engine(db_path)
    # Sinh các bảng trong CSDL
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Thêm dữ liệu mẫu nếu bảng books rỗng
    if session.query(Book).count() == 0:
        session.add_all([
            Book(title="To Kill a Mockingbird", author="Harper Lee", published_year=1960),
            Book(title="1984", author="George Orwell", published_year=1949),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", published_year=1925)
        ])
    
    # Thêm dữ liệu mẫu nếu bảng users rỗng
    if session.query(User).count() == 0:
        session.add_all([
            User(name="Alice", email="alice@example.com"),
            User(name="Bob", email="bob@example.com")
        ])
        
    session.commit()
    session.close()

class BookModel:
    def __init__(self, db_path=DB_PATH):
        self.engine = get_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        with self.Session() as session:
            return [b.to_dict() for b in session.query(Book).all()]

    def get_by_id(self, book_id):
        with self.Session() as session:
            book = session.query(Book).filter(Book.id == book_id).first()
            return book.to_dict() if book else None

    def add(self, title, author, published_year=None):
        if not title or not author:
            raise ValueError("Title and author are required")
        with self.Session() as session:
            new_book = Book(title=title, author=author, published_year=published_year)
            session.add(new_book)
            session.commit()
            return new_book.to_dict()

    def update(self, book_id, update_data):
        with self.Session() as session:
            book = session.query(Book).filter(Book.id == book_id).first()
            if not book:
                return None
            
            if 'title' in update_data:
                book.title = update_data['title']
            if 'author' in update_data:
                book.author = update_data['author']
            if 'published_year' in update_data:
                book.published_year = update_data['published_year']
                
            session.commit()
            return book.to_dict()

    def delete(self, book_id):
        with self.Session() as session:
            book = session.query(Book).filter(Book.id == book_id).first()
            if not book:
                return False
            session.delete(book)
            session.commit()
            return True

class UserModel:
    def __init__(self, db_path=DB_PATH):
        self.engine = get_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        with self.Session() as session:
            return [u.to_dict() for u in session.query(User).all()]

    def get_by_id(self, user_id):
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            return user.to_dict() if user else None

    def add(self, name, email):
        if not name or not email:
            raise ValueError("Name and email are required")
        with self.Session() as session:
            new_user = User(name=name, email=email)
            session.add(new_user)
            try:
                session.commit()
                return new_user.to_dict()
            except IntegrityError:
                session.rollback()
                raise ValueError("Email already exists")

    def delete(self, user_id):
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return True

if __name__ == '__main__':
    # Chạy trực tiếp file này để chủ động tạo database library.db
    print("Đang khởi tạo database và nạp dữ liệu mẫu...")
    init_db()
    print("--- Tạo cơ sở dữ liệu library.db và các bảng thành công! ---")
