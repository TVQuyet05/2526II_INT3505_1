import "@typespec/http";
import "@typespec/rest";
import "@typespec/openapi3";

using TypeSpec.Http;
using TypeSpec.Rest;

@service(#{
  title: "Simple Books API",
})
@server("http://localhost:5000", "Local development server")
namespace BooksService {
  model Book {
    id: string;
    title: string;
    author: string;
    publishedYear: int32;
    genre?: string;
  }

  model NewBook {
    title: string;
    author: string;
    publishedYear: int32;
    genre?: string;
  }

  @tag("Books")
  @route("/books")
  interface BooksAction {
    @get list(): Book[];

    @post create(@body book: NewBook): Book | { @statusCode statusCode: 201 };

    @route("/{id}")
    @get getBook(@path id: string): Book | { @statusCode statusCode: 404 };

    @route("/{id}")
    @put updateBook(@path id: string, @body book: NewBook): Book | { @statusCode statusCode: 404 };

    @route("/{id}")
    @delete deleteBook(@path id: string): { @statusCode statusCode: 204 } | { @statusCode statusCode: 404 };
  }
}
