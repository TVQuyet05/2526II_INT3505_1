import pytest
from models import BookModel, UserModel, init_db

@pytest.fixture
def db_path(tmp_path):
    # Dùng database ở file tạm thời trong thư mục tmp để tránh hỏng DB thật
    db_file = tmp_path / "test_library.db"
    db_url = f"sqlite:///{db_file}"
    init_db(db_url)
    return db_url

@pytest.fixture
def book_model(db_path):
    return BookModel(db_path)

@pytest.fixture
def user_model(db_path):
    return UserModel(db_path)

def test_get_all_books(book_model):
    books = book_model.get_all()
    assert len(books) == 3
    assert isinstance(books, list)

def test_get_book_by_id(book_model):
    book = book_model.get_by_id(1)
    assert book is not None
    assert book['title'] == "To Kill a Mockingbird"

def test_get_book_not_found(book_model):
    book = book_model.get_by_id(999) # ID không tồn tại
    assert book is None

def test_add_valid_book(book_model):
    new_book = book_model.add(title="The Hobbit", author="J.R.R. Tolkien", published_year=1937)
    
    # Kiểm tra sách được trả về
    assert new_book['id'] == 4 # Max ID cũ là 3
    assert new_book['title'] == "The Hobbit"
    
    # Kiểm tra số lượng sách đã tăng
    assert len(book_model.get_all()) == 4

def test_add_invalid_book(book_model):
    # Cố ý không truyền title
    with pytest.raises(ValueError, match="Title and author are required"):
        book_model.add(title="", author="Unknown")

def test_update_book(book_model):
    updated = book_model.update(1, {"title": "Updated Title"})
    assert updated is not None
    assert updated['title'] == "Updated Title"
    
    # Kiểm tra author (không cập nhật) vẫn giữ nguyên
    assert updated['author'] == "Harper Lee"

def test_delete_book(book_model):
    success = book_model.delete(1)
    assert success is True
    
    # Xác minh lại xem sách đã thực sự bị xoá chưa
    assert book_model.get_by_id(1) is None
    assert len(book_model.get_all()) == 2

# ======= Test User Model =======

def test_get_all_users(user_model):
    users = user_model.get_all()
    assert len(users) == 2

def test_add_valid_user(user_model):
    new_user = user_model.add(name="Charlie", email="charlie@example.com")
    assert new_user['id'] == 3
    assert len(user_model.get_all()) == 3

def test_add_duplicate_email(user_model):
    with pytest.raises(ValueError, match="Email already exists"):
        user_model.add(name="Alice Clone", email="alice@example.com")
