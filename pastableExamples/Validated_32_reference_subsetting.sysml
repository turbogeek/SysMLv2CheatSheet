package ReferenceTests;

part def Library {
    part book[*];
}

part def Reader {
    // Reference to books (not owned)
    ref part borrowedBooks[*] references Library::book;
    
    // Subset relationship
    part favoriteBooks[*] subsets borrowedBooks;
}

part librarySystem {
    part library : Library;
    part reader : Reader;
}
