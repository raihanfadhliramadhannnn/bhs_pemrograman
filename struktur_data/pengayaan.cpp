#include <iostream>
#include <stack>
#include <string>

using namespace std;

class PengolahKata {
private:
    string teksSaatIni;
    stack<string> tumpukanUndo;
    stack<string> tumpukanRedo;

public:
    PengolahKata() {
        teksSaatIni = "";
    }

    void ketik(const string& teks) {
        tumpukanUndo.push(teksSaatIni);  // Simpan teks saat ini ke dalam tumpukanUndo
        teksSaatIni += teks;             // Ketikkan teks baru ke dalam teksSaatIni
        tumpukanRedo = stack<string>();  // Kosongkan tumpukanRedo setelah ada perubahan
        cout << "Teks ditambahkan: " << teksSaatIni << endl;
    }

    void undo() {
        if (!tumpukanUndo.empty()) {
            tumpukanRedo.push(teksSaatIni);     // Simpan teks saat ini ke dalam tumpukanRedo
            teksSaatIni = tumpukanUndo.top();  // Kembalikan teks sebelumnya dari tumpukanUndo
            tumpukanUndo.pop();                 // Hapus teks yang digunakan dari tumpukanUndo
            cout << "Undo: " << teksSaatIni << endl;
        } else {
            cout << "Tidak ada yang bisa di-undo." << endl;
        }
    }

    void redo() {
        if (!tumpukanRedo.empty()) {
            tumpukanUndo.push(teksSaatIni);     // Simpan teks saat ini ke dalam tumpukanUndo
            teksSaatIni = tumpukanRedo.top();  // Ambil teks yang ada di tumpukanRedo
            tumpukanRedo.pop();                 // Hapus teks yang digunakan dari tumpukanRedo
            cout << "Redo: " << teksSaatIni << endl;
        } else {
            cout << "Tidak ada yang bisa di-redo." << endl;
        }
    }

    bool apakahTumpukanUndoKosong() const {
        return tumpukanUndo.empty();
    }

    bool apakahTumpukanRedoKosong() const {
        return tumpukanRedo.empty();
    }
};

int main() {
    PengolahKata editor;
    string operasi, teks;

    while (true) {
        // Menampilkan menu 
        cout << "===== Menu Pengolah Kata =====" << endl;
        cout << "1. Ketik teks baru" << endl;
        cout << "2. Undo" << endl;
        cout << "3. Redo" << endl;
        cout << "4. Cek apakah Tumpukan Undo kosong" << endl;
        cout << "5. Cek apakah Tumpukan Redo kosong" << endl;
        cout << "6. Keluar" << endl;
        cout << "==============================" << endl;
        cout << "Masukkan pilihan (1-6): ";
        
        // Menerima input dari pengguna
        cin >> operasi;

        // Pilihan berdasarkan input pengguna
        if (operasi == "1") {
            cout << "Masukkan teks yang ingin ditambahkan: ";
            cin.ignore(); // Membersihkan buffer input
            getline(cin, teks);
            editor.ketik(teks);
        } else if (operasi == "2") {
            editor.undo();
        } else if (operasi == "3") {
            editor.redo();
        } else if (operasi == "4") {
            if (editor.apakahTumpukanUndoKosong()) {
                cout << "Tumpukan Undo kosong." << endl;
            } else {
                cout << "Tumpukan Undo tidak kosong." << endl;
            }
        } else if (operasi == "5") {
            if (editor.apakahTumpukanRedoKosong()) {
                cout << "Tumpukan Redo kosong." << endl;
            } else {
                cout << "Tumpukan Redo tidak kosong." << endl;
            }
        } else if (operasi == "6") {
            cout << "Keluar dari program." << endl;
            break;
        } else {
            cout << "Pilihan tidak valid. Silakan masukkan angka dari 1 sampai 6." << endl;
        }

        cout << endl;
    }

    return 0;
}
