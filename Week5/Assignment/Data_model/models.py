from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, DateTime, create_engine
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class LoanStatus(enum.Enum):
    BORROWED = "borrowed"
    RETURNED = "returned"
    OVERDUE = "overdue"

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(255))
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    # Quan hệ 1-N với Loan
    loans = relationship("Loan", back_populates="member")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    isbn = Column(String(13), unique=True, nullable=False)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    category = Column(String(50))
    total_copies = Column(Integer, default=1)
    available_copies = Column(Integer, default=1)
    
    # Quan hệ 1-N với Loan
    loans = relationship("Loan", back_populates="book")

class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    
    loan_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime)
    status = Column(Enum(LoanStatus), default=LoanStatus.BORROWED)
    
    # Quan hệ ngược lại
    book = relationship("Book", back_populates="loans")
    member = relationship("Member", back_populates="loans")

# Mô tả database modeling
"""
Cấu trúc quan hệ (Entity-Relationship):

1. Member (Thành viên):
   - Lưu trữ thông tin cá nhân của người mượn sách.
   - Quan hệ 1-N với Loan: Một thành viên có thể mượn nhiều lần (thực hiện nhiều giao dịch mượn).

2. Book (Sách):
   - Lưu trữ thông tin về đầu sách, mã ISBN và số lượng bản sao hiện có.
   - Quan hệ 1-N với Loan: Một đầu sách có thể xuất hiện trong nhiều giao dịch mượn.

3. Loan (Giao dịch mượn sách):
   - Là bảng trung gian kết nối Member và Book.
   - Chứa thông tin về ngày mượn, hạn trả, ngày thực trả và trạng thái (Đang mượn, đã trả, quá hạn).
"""

if __name__ == '__main__':
    # 1. Tạo engine kết nối tới file database SQLite (library.db trong cùng thư mục)
    # echo=True sẽ in ra các câu lệnh SQL tự động sinh ra trên terminal
    engine = create_engine('sqlite:///library.db', echo=True)
    
    # 2. Sinh các bảng trong CSDL dựa trên các class kế thừa từ Base
    Base.metadata.create_all(engine)
    
    print("\n--- Tạo cơ sở dữ liệu library.db và các bảng thành công! ---")
