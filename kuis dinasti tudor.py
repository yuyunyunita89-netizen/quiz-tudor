import streamlit as st
import random

# Set judul aplikasi
st.set_page_config(page_title="Kuis Sejarah Dinasti Tudor", layout="centered")
st.title("📜 Kuis Sejarah Dinasti Tudor")
st.write("Jawablah 15 soal pilihan ganda tentang Dinasti Tudor. Pilih A, B, C, atau D.")

# Daftar pertanyaan
questions = [
    {
        "question": "Siapa pendiri Dinasti Tudor yang mengklaim takhta setelah memenangkan Pertempuran Bosworth Field?",
        "options": ["A. Henry VII", "B. Henry VIII", "C. Edward VI", "D. Richard III"],
        "answer": "A"
    },
    {
        "question": "Berapa banyak istri yang dimiliki oleh Raja Henry VIII?",
        "options": ["A. Empat", "B. Lima", "C. Enam", "D. Tujuh"],
        "answer": "C"
    },
    {
        "question": "Reformasi Inggris dimulai di bawah pemerintahan raja Tudor mana?",
        "options": ["A. Henry VII", "B. Henry VIII", "C. Edward VI", "D. Mary I"],
        "answer": "B"
    },
    {
        "question": "Siapa istri pertama Henry VIII, yang ia ceraikan untuk menikah dengan Anne Boleyn?",
        "options": ["A. Catherine dari Aragon", "B. Anne dari Cleves", "C. Jane Seymour", "D. Catherine Howard"],
        "answer": "A"
    },
    {
        "question": "Siapa putri Henry VIII yang memerintah sebentar dan dikenal dengan julukan 'Ratu Sembilan Hari'?",
        "options": ["A. Mary I", "B. Elizabeth I", "C. Lady Jane Grey", "D. Anne Boleyn"],
        "answer": "C"
    },
    {
        "question": "Ratu yang dijuluki 'Bloody Mary' karena menganiaya umat Protestan adalah?",
        "options": ["A. Elizabeth I", "B. Mary I", "C. Anne Boleyn", "D. Jane Seymour"],
        "answer": "B"
    },
    {
        "question": "Siapa ratu Tudor yang memerintah selama 'Zaman Keemasan' Inggris dan mengalahkan Armada Spanyol?",
        "options": ["A. Mary I", "B. Elizabeth I", "C. Lady Jane Grey", "D. Catherine dari Aragon"],
        "answer": "B"
    },
    {
        "question": "Siapakah ibu dari Ratu Elizabeth I?",
        "options": ["A. Catherine dari Aragon", "B. Anne Boleyn", "C. Jane Seymour", "D. Catherine Parr"],
        "answer": "B"
    },
    {
        "question": "Pada tahun berapa Dinasti Tudor berakhir?",
        "options": ["A. 1547", "B. 1558", "C. 1603", "D. 1625"],
        "answer": "C"
    },
    {
        "question": "Siapa penguasa Tudor terakhir?",
        "options": ["A. Edward VI", "B. Henry VIII", "C. Elizabeth I", "D. Mary I"],
        "answer": "C"
    },
    {
        "question": "Siapa yang menggantikan Elizabeth I sebagai penguasa Inggris, mengakhiri Dinasti Tudor?",
        "options": ["A. James I", "B. Charles I", "C. Henry IX", "D. William dari Oranye"],
        "answer": "A"
    },
    {
        "question": "Tindakan Raja Henry VIII memisahkan diri dari Gereja Katolik Roma dikenal sebagai?",
        "options": ["A. Perang Saudara Inggris", "B. Reformasi Inggris", "C. Inkuisisi Inggris", "D. Skisma Agung"],
        "answer": "B"
    },
    {
        "question": "Kekalahan Armada Spanyol terjadi selama masa pemerintahan ratu Tudor mana?",
        "options": ["A. Mary I", "B. Elizabeth I", "C. Jane Seymour", "D. Catherine dari Aragon"],
        "answer": "B"
    },
    {
        "question": "Siapa satu-satunya putra Raja Henry VIII yang selamat, yang menjadi raja pada usia muda?",
        "options": ["A. Arthur", "B. Edward VI", "C. Henry IX", "D. Edward V"],
        "answer": "B"
    },
    {
        "question": "Pada masa pemerintahan raja Tudor manakah terjadi penghancuran biara-biara di Inggris?",
        "options": ["A. Henry VII", "B. Henry VIII", "C. Edward VI", "D. Elizabeth I"],
        "answer": "B"
    }
]

# Inisialisasi state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.answers = []
    random.shuffle(questions)
    st.session_state.questions = questions

# Fungsi untuk reset kuis
def reset_quiz():
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.answers = []
    random.shuffle(questions)
    st.session_state.questions = questions

# Tampilkan pertanyaan saat ini
if st.session_state.current_q < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.current_q]
    st.subheader(f"Soal {st.session_state.current_q + 1} dari {len(st.session_state.questions)}")
    st.write(q["question"])
    user_choice = st.radio("Pilih jawaban Anda:", q["options"], key=st.session_state.current_q)

    if st.button("Kirim Jawaban"):
        correct = user_choice.startswith(q["answer"])
        st.session_state.answers.append((q["question"], user_choice, q["answer"]))
        if correct:
            st.success("Jawaban Anda benar!")
            st.session_state.score += 1
        else:
            st.error(f"Jawaban salah. Jawaban yang benar adalah {q['answer']}.")

        st.session_state.current_q += 1
        st.experimental_rerun()

# Tampilkan hasil akhir
else:
    st.success("🎉 Kuis selesai!")
    st.write(f"Skor akhir Anda: **{st.session_state.score} / {len(st.session_state.questions)}**")

    with st.expander("📋 Lihat Jawaban Anda"):
        for idx, (question, user_ans, correct_ans) in enumerate(st.session_state.answers):
            st.write(f"**{idx+1}. {question}**")
            st.write(f"Jawaban Anda: {user_ans} | Jawaban Benar: {correct_ans}\n")

    if st.button("🔄 Main Lagi"):
        reset_quiz()
        st.experimental_rerun()
