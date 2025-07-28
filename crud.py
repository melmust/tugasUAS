import streamlit as st

# Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}"

# Data disimpan di list session_state
if 'data_mahasiswa' not in st.session_state:
    st.session_state.data_mahasiswa = []

# Tampilan utama
st.title("Aplikasi CRUD Mahasiswa (OOP + Angka Menu)")

st.write("### Pilihan Menu:")
st.write("1. Lihat Data")
st.write("2. Tambah Data")
st.write("3. Ubah Data")
st.write("4. Hapus Data")

menu = st.text_input("Masukkan angka menu (1-4):")

# Fungsi menu
if menu == "1":
    st.subheader("📄 Daftar Mahasiswa")
    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa):
            st.write(f"{i+1}. {mhs}")
    else:
        st.info("Belum ada data.")

elif menu == "2":
    st.subheader("➕ Tambah Mahasiswa")
    nim = st.text_input("Masukkan NIM")
    nama = st.text_input("Masukkan Nama")
    if st.button("Simpan"):
        if nim and nama:
            mhs = Mahasiswa(nim, nama)
            st.session_state.data_mahasiswa.append(mhs)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")

elif menu == "3":
    st.subheader("✏️ Ubah Mahasiswa")
    data = st.session_state.data_mahasiswa
    

elif menu == "4":
    st.subheader("🗑️ Hapus Mahasiswa")
    

elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
