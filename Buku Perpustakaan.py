library = []

def add_book():
    # fungsi untuk menambahkan buku ke dalam perpustakaan
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")
    
    book = {"title": title, "author": author, "year": int(year)}
    library.append(book)
    library.sort(key=lambda x: (x["title"].lower(), x["year"]))
    print(f"Buku '{title}' berhasil ditambahkan ke perpustakaan!")

def search_books(keyword):
    # fungsi untuk mencari buku berdasarkan kata kunci judul
    results = []
    for book in library:
        if keyword.lower() in book["title"].lower():
            results.append(book)
    return results

def delete_book(title):
    # fungsi untuk menghapus buku berdasarkan judul
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    print(f"Buku '{title}' berhasil dihapus dari perpustakaan!")

def get_book_year(title):
    # fungsi untuk mendapatkan tahun terbit buku berdasarkan judul
    for book in library:
        if book["title"].lower() == title.lower():
            return book["year"]
    return "Buku tidak ditemukan."

def display_books(books):
    # fungsi untuk menampilkan daftar buku
    if not books:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def display_all_books():
    # fungsi untuk menampilkan semua buku di perpustakaan
    if not library:
        print("Tidak ada buku di perpustakaan.")
    else:
        print("Daftar semua buku di perpustakaan:")
        for book in library:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambahkan Buku")
        print("2. Cari Buku")
        print("3. Hapus Buku")
        print("4. Tahun Buku")
        print("5. Tampilkan Semua Buku")
        print("6. Keluar")
        choice = input("Pilih menu (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            keyword = input("Masukkan kata kunci judul buku yang ingin dicari: ")
            results = search_books(keyword)
            display_books(results)
        elif choice == '3':
            title = input("Masukkan judul buku yang ingin dihapus: ")
            delete_book(title)
        elif choice == '4':
            title = input("Masukkan judul buku untuk mengetahui tahun terbit: ")
            year = get_book_year(title)
            print(f"Tahun terbit buku '{title}': {year}")
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            print("Terima kasih telah menggunakan perpustakaan!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
