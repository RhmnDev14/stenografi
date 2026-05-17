# pyrefly: ignore [missing-import]
import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Steganografi LSB", page_icon="🕵️", layout="centered")

from stego import encode_image, decode_image

st.title("🕵️ Steganografi Gambar (LSB)")
st.write("Sembunyikan pesan rahasiamu ke dalam sebuah gambar dengan teknik *Least Significant Bit*.")

tab1, tab2 = st.tabs(["🔒 Encode (Sembunyikan Pesan)", "🔓 Decode (Baca Pesan)"])

with tab1:
    st.header("Sembunyikan Pesan")
    uploaded_file = st.file_uploader("Upload Gambar Sumber (JPG/PNG)", type=["jpg", "jpeg", "png"], key="encode_uploader")
    secret_message = st.text_area("Masukkan Pesan Rahasia", height=100)
    
    if uploaded_file and secret_message:
        if st.button("Encode & Sembunyikan Pesan", type="primary"):
            with st.spinner("Menyisipkan pesan..."):
                img = Image.open(uploaded_file)
                
                max_bytes = (img.width * img.height * 3) // 8
                if len(secret_message) + 5 > max_bytes:
                    st.error(f"Pesan terlalu panjang! Gambar ini hanya bisa menampung {max_bytes - 5} karakter.")
                else:
                    encoded_img = encode_image(img.copy(), secret_message)
                    
                    buf = io.BytesIO()
                    encoded_img.save(buf, format="PNG")
                    byte_im = buf.getvalue()

                    st.success("✅ Pesan berhasil disembunyikan!")
                    st.image(encoded_img, caption="Preview Gambar Hasil", width="stretch")
                    
                    st.download_button(
                        label="⬇️ Download Gambar Hasil (.png)",
                        data=byte_im,
                        file_name="hasil_rahasia.png",
                        mime="image/png"
                    )

with tab2:
    st.header("Baca Pesan Rahasia")
    st.info("⚠️ Pastikan gambar yang di-upload berformat PNG dan belum pernah dikompresi ulang.")
    decode_file = st.file_uploader("Upload Gambar Hasil (.png)", type=["png"], key="decode_uploader")
    
    if decode_file:
        if st.button("Decode & Baca Pesan", type="primary"):
            with st.spinner("Mengekstrak pesan..."):
                img = Image.open(decode_file)
                hidden_text = decode_image(img)
                
                if "Tidak ada pesan" not in hidden_text:
                    st.success("✅ Pesan Rahasia Ditemukan!")
                    st.code(hidden_text)
                else:
                    st.error("Pesan tidak ditemukan. Pastikan gambar ini memang menyimpan pesan rahasia dan formatnya belum berubah.")

st.markdown("---")
st.caption("Dibuat menggunakan [Streamlit](https://streamlit.io/) & Pillow")
