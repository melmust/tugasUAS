import streamlit as st

# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

# Kelas manajemen data
class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, nim, nama):
        self.data.append(Mahasiswa(nim, nama))

    def lihat(self):
        return self.data

    def hapus(self, index):
        del self.data[index]

    def ubah(self, index, nim, nama):
        self.data[index].nim = nim
        self.data[index].nama = nama

# Inisialisasi
if 'db' not in st.session_state:
    st.session_state.db = DataMahasiswa()
db = st.session_state.db

# UI
st.title("CRUD Mahasiswa (OOP Sederhana)")
menu = st.selectbox("Menu", ["Lihat", "Tambah", "Ubah", "Hapus"])

if menu == "Lihat":
    st.subheader("Daftar Mahasiswa")
    for i, m in enumerate(db.lihat()):
        st.write(f"{i+1}. NIM: {m.nim}, Nama: {m.nama}")

elif menu == "Tambah":
    nim = st.text_input("NIM")
    nama = st.text_input("Nama")
    if st.button("Tambah"):
        db.tambah(nim, nama)
        st.success("Data ditambahkan.")

elif menu == "Ubah":
    data = db.lihat()
    if data:
        idx = st.number_input("Index data (mulai dari 0)", 0, len(data)-1)
        nim = st.text_input("NIM Baru", data[idx].nim)
        nama = st.text_input("Nama Baru", data[idx].nama)
        if st.button("Ubah"):
            db.ubah(idx, nim, nama)
            st.success("Data diubah.")
    else:
        st.info("Tidak ada data.")

elif menu == "Hapus":
    data = db.lihat()
    if data:
        idx = st.number_input("Index data (mulai dari 0)", 0, len(data)-1)
        if st.button("Hapus"):
            db.hapus(idx)
            st.success("Data dihapus.")
    else:
        st.info("Tidak ada data.")
