export function getBooks() {
  let myHeaders = new Headers({ "Content-Type": "application/json" });
  var myInit = { method: 'GET', headers: myHeaders, mode: 'cors' };
  let promise = fetch("/books", myInit);
  return promise.then((response) => {
    return response.text();
  });
}

export function deleteBook(book) {
  let url = (book.id) ? "/books/" + book.id : "/books/" + book.isbn;
  let myHeaders = new Headers({ "Content-Type": "application/json" });
  var myInit = { method: 'DELETE', headers: myHeaders, mode: 'cors' };
  let promise = fetch(url , myInit);
  return promise.then((response) => {
    return response.text();
  });
}

export function addBook(book) {
  let url = "/books/";
  let myHeaders = new Headers({ "Content-Type": "application/json" });
  delete book.id;
  let body = JSON.stringify(book);
  var myInit = {
    method: 'POST',
    body: body,
    headers: myHeaders,
    mode: 'cors'
  };
  let promise = fetch(url, myInit);
  return promise.then((response) => {
    return response.text();
  });

}

export function updateBook(book) {
  let url = (book.id) ? "/books/" + book.id : "/books/" + book.isbn;
  let myHeaders = new Headers({ "Content-Type": "application/json" });
  let body = JSON.stringify(book);
  var myInit = {
    method: 'PUT',
    body: body,
    headers: myHeaders,
    mode: 'cors'
  };
  let promise = fetch(url, myInit);
  return promise.then((response) => {
    return response.text();
  });

}