import streamlit as st
from capture_face import capture_face, verify_face
from speech_to_text import speech_to_text
from sentiment_analysis import analyze_sentiment
from chatbot import generate_response

# Judul dan deskripsi aplikasi
st.title("Aplikasi Curhat Online dengan AI")
st.subheader("Fitur:")
st.write("""
- **Verifikasi Wajah:** Pastikan hanya pengguna yang valid dapat mengakses.
- **Curhat Berbasis Suara:** Rekam suara Anda, dan aplikasi akan mengubahnya menjadi teks.
- **Analisis Sentimen:** Analisis emosi atau sentimen dari curhat Anda.
- **Chatbot:** Dapatkan respons atau saran otomatis dari chatbot AI.
""")

# Verifikasi Wajah
st.header("1. Verifikasi Wajah")
if st.button("Mulai Verifikasi Wajah"):
    # Tangkap wajah pengguna
    st.info("Mengaktifkan kamera...")
    capture_face()
    # Periksa kecocokan wajah
    if verify_face("database/known_face.jpg", "database/captured_face.jpg"):
        st.success("Wajah terverifikasi! Silakan lanjut ke langkah berikutnya.")
    else:
        st.error("Wajah tidak dikenali. Akses ditolak.")

# Curhat Suara
st.header("2. Curhat Berbasis Suara")
if st.button("Mulai Curhat"):
    st.info("Silakan berbicara...")
    curhat_text = speech_to_text()  # Transkripsi suara menjadi teks
    if curhat_text:
        st.write("**Teks Curhat Anda:**", curhat_text)
        
        # Analisis Sentimen
        st.header("3. Analisis Sentimen")
        sentiment = analyze_sentiment(curhat_text)
        st.write("**Hasil Analisis Sentimen:**", sentiment)
        
        # Respons Chatbot
        st.header("4. Respons Chatbot")
        response = generate_response(curhat_text)
        st.write("**Chatbot Merespons:**", response)
    else:
        st.warning("Curhat tidak berhasil ditranskripsikan.")

# Informasi Footer
st.markdown("---")
st.caption("Dikembangkan menggunakan Python, Streamlit, dan model AI.")

