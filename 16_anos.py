import streamlit as st
from pathlib import Path
import base64


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="16 Anos de Amor ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ============================================================
# 🔐 TELA SECRETA — ACESSO À HOMENAGEM
# ============================================================

if "acesso_homenagem" not in st.session_state:
    st.session_state.acesso_homenagem = False


if not st.session_state.acesso_homenagem:

    st.markdown("""
    <style>

    .login-container {
    width: calc(100% - 30px);
    max-width: 550px;
    margin: 0px auto;
    text-align: center;
    padding: 35px 25px;
    background: rgba(255,255,255,0.92);
    border-radius: 30px;
    box-shadow: 0 20px 60px rgba(90,30,50,0.18);
    box-sizing: border-box;
    }

    .login-heart {
        font-size: 65px;
        margin-bottom: 15px;
    }

    .login-title {
        font-family: 'Great Vibes', cursive;
        font-size: 42px;
        color: #9b3158;
        margin-bottom: 15px;
    }

    .login-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 22px;
        color: #694451;
        line-height: 1.5;
        margin-bottom: 25px;
    }

    .login-secret {
        font-family: 'Cormorant Garamond', serif;
        font-size: 18px;
        color: #9b3158;
        font-style: italic;
        margin-top: 15px;
    }

    </style>
    """, unsafe_allow_html=True)


    st.html("""
    <div class="login-container">

        <div class="login-heart">
            ❤️
        </div>

        <div class="login-title">
            Uma surpresa espera por você...
        </div>

        <div class="login-text">
            Por favor, digite sua senha.
            <br><br>
            Só nós conhecemos essa senha... ela faz parte da nossa história. ❤️
        </div>

        <div class="login-secret">
            Uma senha de apenas 3 letras...
            <br>
            mas com um significado enorme. ❤️
        </div>

    </div>
    """)


    senha = st.text_input(
        "Senha",
        type="password",
        placeholder="Digite as 3 letras...",
        label_visibility="collapsed"
    )


    if st.button("Entrar ❤️", use_container_width=True):

        if senha.strip().upper() == "TAM":

            st.session_state.acesso_homenagem = True
            st.rerun()

        else:

            st.error(
                "💕 Essa não é a senha que o nosso amor conhece..."
            )

    st.stop()

# ============================================================
# CAMINHO PRINCIPAL DO PROJETO
# ============================================================

PASTA_PROJETO = Path(__file__).resolve().parent

PASTA_IMAGENS = PASTA_PROJETO / "imagem"
PASTA_MUSICA = PASTA_PROJETO / "musica"


# ============================================================
# DADOS DO CASAL
# ============================================================

NOME_ESPOSA = "Meu Amor"
NOME_ESPOSO = "Seu esposo"

ANO_INICIO = 2006
ANO_CASAMENTO = 2010
ANO_ATUAL = 2026

ANOS_CASAMENTO = ANO_ATUAL - ANO_CASAMENTO
ANOS_JUNTOS = ANO_ATUAL - ANO_INICIO


# ============================================================
# FOTOS
# ============================================================

FOTO_NAMORO = PASTA_IMAGENS / "01_namoro.jpg"
FOTO_CASAMENTO = PASTA_IMAGENS / "02_casamento.jpg"
FOTO_ISAQUE = PASTA_IMAGENS / "03_isaque.jpg"
FOTO_IANNY = PASTA_IMAGENS / "04_ianny.jpg"
FOTO_IGREJA = PASTA_IMAGENS / "05_igreja.jpg"
FOTO_FAMILIA = PASTA_IMAGENS / "06_familia.jpg"

MUSICA = PASTA_MUSICA / "Eu e Você.mp3"


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def imagem_existe(caminho):
    return caminho.exists() and caminho.is_file()


def arquivo_base64(caminho):
    """
    Converte um arquivo para Base64.
    Usado principalmente para a música,
    permitindo que o player fique incorporado na página.
    """

    if not caminho.exists():
        return None

    try:

        with open(caminho, "rb") as arquivo:
            dados = base64.b64encode(
                arquivo.read()
            ).decode("utf-8")

        return dados

    except Exception:
        return None


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Montserrat:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 210, 220, 0.35), transparent 35%),
        radial-gradient(circle at bottom right, rgba(255, 230, 200, 0.30), transparent 35%),
        #fffaf8;
}


/* ============================================================
   CORAÇÕES FLUTUANTES
   ============================================================ */

.floating-hearts {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100vh;
    pointer-events: none;
    overflow: hidden;
    z-index: 1;
}

.floating-hearts span {
    position: absolute;
    bottom: -60px;
    font-size: 22px;
    opacity: 0;
    animation: heartsUp 12s linear infinite;
}

.floating-hearts span:nth-child(1) {
    left: 5%;
    font-size: 22px;
    animation-delay: 0s;
}

.floating-hearts span:nth-child(2) {
    left: 14%;
    font-size: 16px;
    animation-delay: 3s;
}

.floating-hearts span:nth-child(3) {
    left: 24%;
    font-size: 28px;
    animation-delay: 7s;
}

.floating-hearts span:nth-child(4) {
    left: 34%;
    font-size: 18px;
    animation-delay: 2s;
}

.floating-hearts span:nth-child(5) {
    left: 45%;
    font-size: 24px;
    animation-delay: 6s;
}

.floating-hearts span:nth-child(6) {
    left: 55%;
    font-size: 18px;
    animation-delay: 10s;
}

.floating-hearts span:nth-child(7) {
    left: 65%;
    font-size: 30px;
    animation-delay: 4s;
}

.floating-hearts span:nth-child(8) {
    left: 74%;
    font-size: 17px;
    animation-delay: 8s;
}

.floating-hearts span:nth-child(9) {
    left: 82%;
    font-size: 25px;
    animation-delay: 1s;
}

.floating-hearts span:nth-child(10) {
    left: 90%;
    font-size: 20px;
    animation-delay: 5s;
}

.floating-hearts span:nth-child(11) {
    left: 30%;
    font-size: 15px;
    animation-delay: 11s;
}

.floating-hearts span:nth-child(12) {
    left: 78%;
    font-size: 27px;
    animation-delay: 9s;
}


@keyframes heartsUp {

    0% {
        transform: translateY(0) scale(0.6) rotate(0deg);
        opacity: 0;
    }

    10% {
        opacity: 0.45;
    }

    50% {
        transform: translateY(-45vh) scale(1) rotate(12deg);
        opacity: 0.55;
    }

    80% {
        opacity: 0.30;
    }

    100% {
        transform: translateY(-110vh) scale(0.8) rotate(-12deg);
        opacity: 0;
    }

}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    text-align: center;
    padding: 70px 20px 60px 20px;
    border-radius: 30px;
    background:
        linear-gradient(
            135deg,
            rgba(255, 230, 235, 0.95),
            rgba(255, 248, 242, 0.98)
        );
    box-shadow: 0 20px 60px rgba(100, 30, 50, 0.12);
    margin-bottom: 35px;
}

.hero-small {
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #9a536d;
    margin-bottom: 20px;
}

.hero h1 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(55px, 8vw, 105px);
    font-weight: 400;
    color: #9b3158;
    margin: 0;
    line-height: 1;
}

.hero h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(30px, 5vw, 52px);
    font-weight: 600;
    color: #542333;
    margin: 15px 0;
}

.hero p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 25px;
    color: #70404f;
    max-width: 750px;
    margin: auto;
    line-height: 1.5;
}

.big-heart {
    font-size: 60px;
    margin: 20px 0;
    animation: pulseHeart 1.8s infinite;
}

@keyframes pulseHeart {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.18);
    }
}


/* ============================================================
   VERSÍCULO
   ============================================================ */

.verse {
    text-align: center;
    max-width: 850px;
    margin: 50px auto;
    padding: 35px;
    border-left: 4px solid #c56b87;
    border-right: 4px solid #c56b87;
    background: rgba(255,255,255,0.7);
    border-radius: 20px;
}

.verse-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    font-style: italic;
    line-height: 1.5;
    color: #57303e;
}

.verse-ref {
    margin-top: 15px;
    font-weight: 600;
    color: #9b3158;
}


/* ============================================================
   CONTADORES
   ============================================================ */

.counter-container {
    display: flex;
    justify-content: center;
    gap: 25px;
    flex-wrap: wrap;
    margin: 40px auto;
}

.counter {
    width: 210px;
    padding: 25px 15px;
    text-align: center;
    background: white;
    border-radius: 22px;
    box-shadow: 0 10px 30px rgba(90, 30, 50, 0.10);
}

.counter-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 48px;
    font-weight: 700;
    color: #a33961;
}

.counter-label {
    font-size: 14px;
    color: #76505d;
    text-transform: uppercase;
    letter-spacing: 1px;
}


/* ============================================================
   TÍTULOS
   ============================================================ */

.section-title {
    text-align: center;
    margin: 70px 0 35px 0;
}

.section-title h2 {
    font-family: 'Great Vibes', cursive;
    font-size: 58px;
    font-weight: 400;
    color: #9b3158;
    margin: 0;
}

.section-title p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 23px;
    color: #76505d;
    margin-top: 5px;
}


/* ============================================================
   TIMELINE
   ============================================================ */

.timeline {
    max-width: 950px;
    margin: auto;
}

.timeline-item {
    display: flex;
    gap: 25px;
    margin-bottom: 30px;
    align-items: flex-start;
}

.timeline-year {
    min-width: 100px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    font-weight: 700;
    color: #a33961;
    text-align: right;
}

.timeline-content {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 25px rgba(90,30,50,0.08);
    flex: 1;
    border-left: 4px solid #d7839f;
}

.timeline-content h3 {
    margin: 0 0 10px 0;
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    color: #663144;
}

.timeline-content p {
    font-size: 15px;
    line-height: 1.8;
    color: #694f59;
    white-space: pre-line;
}


/* ============================================================
   FOTOS DA HISTÓRIA
   ============================================================ */

.story-photo {
    max-width: 950px;
    margin: 35px auto 55px auto;
    text-align: center;
}

.story-photo img {
    width: 80%;
    max-height: 500px;
    object-fit: cover;
    border-radius: 28px;
    box-shadow: 0 18px 50px rgba(90,30,50,0.15);
    display: block;
    margin: 0 auto;
}

.story-photo-title {
    font-family: 'Great Vibes', cursive;
    font-size: 45px;
    color: #9b3158;
    margin-top: 18px;
}

.story-photo-description {
    font-family: 'Cormorant Garamond', serif;
    font-size: 23px;
    color: #694451;
    margin-top: 4px;
}

/* ============================================================
   FOTOS DOS FILHOS - FORMATO VERTICAL
   ============================================================ */

.child-card img {
    width: 100%;
    height: 420px;
    object-fit: cover;
    object-position: center;
    border-radius: 24px;
    display: block;
}

/* ============================================================
   FILHOS
   ============================================================ */

.children-section {
    max-width: 1000px;
    margin: 65px auto 40px auto;
}

.children-intro {
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 25px;
    line-height: 1.6;
    color: #684452;
    max-width: 800px;
    margin: 0 auto 35px auto;
}

.children-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(250px, 1fr));
    gap: 30px;
    margin-top: 30px;
}

.child-card {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.98),
        rgba(255,239,244,0.95)
    );
    border-radius: 28px;
    padding: 30px 25px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(90,30,50,0.12);
    border: 1px solid rgba(190,100,130,0.12);
    transition: transform 0.3s ease;
}

.child-card:hover {
    transform: translateY(-6px);
}

.child-icon {
    font-size: 42px;
    margin-bottom: 10px;
}

.child-name {
    font-family: 'Great Vibes', cursive;
    font-size: 48px;
    color: #9b3158;
    margin: 10px 0;
}

.child-description {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    line-height: 1.5;
    color: #694451;
}

.child-photo-title {
    font-size: 14px;
    color: #9a536d;
    letter-spacing: 2px;
    text-transform: uppercase;
}


/* ============================================================
   CARTA
   ============================================================ */

.letter {
    max-width: 850px;
    margin: 50px auto;
    background: rgba(255,255,255,0.92);
    padding: 50px;
    border-radius: 28px;
    box-shadow: 0 15px 45px rgba(80,30,50,0.10);
}

.letter h3 {
    text-align: center;
    font-family: 'Great Vibes', cursive;
    font-size: 52px;
    font-weight: 400;
    color: #9b3158;
}

.letter p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 23px;
    line-height: 1.8;
    color: #59404a;
    text-align: justify;
}


/* ============================================================
   ORAÇÃO
   ============================================================ */

.prayer {
    max-width: 850px;
    margin: 60px auto;
    text-align: center;
    background: linear-gradient(
        135deg,
        #fff0f4,
        #fffaf5
    );
    padding: 45px 35px;
    border-radius: 30px;
}

.prayer h3 {
    font-family: 'Great Vibes', cursive;
    font-size: 52px;
    color: #9b3158;
    margin-bottom: 20px;
}

.prayer p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    line-height: 1.7;
    color: #60404c;
}


/* ============================================================
   MÚSICA
   ============================================================ */

.music-box {
    max-width: 850px;
    margin: 45px auto 100px auto;
    padding: 35px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(255,240,245,0.98),
        rgba(255,250,245,0.98)
    );
    border-radius: 30px;
    box-shadow: 0 15px 45px rgba(80,30,50,0.12);
    border: 1px solid rgba(190,100,130,0.12);
}

.music-heart {
    font-size: 48px;
    margin-bottom: 8px;
}

.music-title {
    font-family: 'Great Vibes', cursive;
    font-size: 45px;
    color: #9b3158;
}

.music-description {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    color: #694451;
    line-height: 1.5;
    margin-bottom: 22px;
}

.music-fixed {
    position: fixed;
    left: 50%;
    bottom: 15px;
    transform: translateX(-50%);
    width: min(700px, calc(100% - 30px));
    z-index: 9999;
    background: rgba(255, 248, 250, 0.97);
    border: 1px solid rgba(155,49,88,0.20);
    border-radius: 18px;
    padding: 8px 12px;
    box-shadow: 0 10px 35px rgba(60,20,40,0.20);
    backdrop-filter: blur(10px);
}

.music-fixed-title {
    text-align: center;
    font-family: 'Cormorant Garamond', serif;
    font-size: 17px;
    color: #7a4054;
    margin-bottom: 3px;
}


/* ============================================================
   FINAL
   ============================================================ */

.final-message {
    text-align: center;
    padding: 80px 20px;
}

.final-message h2 {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(55px, 8vw, 90px);
    font-weight: 400;
    color: #9b3158;
}

.final-message p {
    font-family: 'Cormorant Garamond', serif;
    font-size: 27px;
    color: #694451;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    padding: 40px 20px 100px 20px;
    color: #8b6570;
    font-size: 13px;
}

.footer-heart {
    font-size: 30px;
    margin-bottom: 10px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 700px) {

    .hero {
        padding: 50px 15px;
    }

    .hero p {
        font-size: 21px;
    }

    .timeline-item {
        flex-direction: column;
        gap: 8px;
    }

    .timeline-year {
        text-align: left;
    }

    .letter {
        padding: 30px 20px;
    }

    .letter p {
        font-size: 20px;
    }

    .children-grid {
        grid-template-columns: 1fr;
    }

    .child-name {
        font-size: 44px;
    }

    .story-photo-title {
        font-size: 38px;
    }

    .story-photo-description {
        font-size: 20px;
    }

    .music-box {
        padding: 25px 18px;
    }

}

</style>
""")


# ============================================================
# CORAÇÕES FLUTUANTES
# ============================================================

st.html("""
<div class="floating-hearts">

    <span>❤</span>
    <span>♡</span>
    <span>❤</span>
    <span>💕</span>
    <span>♡</span>
    <span>❤</span>
    <span>💗</span>
    <span>♡</span>
    <span>❤</span>
    <span>💕</span>
    <span>♡</span>
    <span>💖</span>

</div>
""")


# ============================================================
# HERO
# ============================================================

st.html(f"""
<div class="hero">

    <div class="hero-small">
        Uma história escrita por Deus
    </div>

    <h1>{ANOS_CASAMENTO} anos</h1>

    <h2>de casamento ❤️</h2>

    <div class="big-heart">
        ❤️
    </div>

    <p>
        Hoje celebramos não apenas uma data,
        mas uma história de amor, fé, companheirismo
        e uma família construída pelas mãos de Deus.
    </p>

</div>
""")


# ============================================================
# VERSÍCULO PRINCIPAL
# ============================================================

st.html("""
<div class="verse">

    <div class="verse-text">
        “Assim não são mais dois, mas uma só carne.
        Portanto, o que Deus ajuntou não o separe o homem.”
    </div>

    <div class="verse-ref">
        Mateus 19:6
    </div>

</div>
""")


# ============================================================
# CONTADORES
# ============================================================

st.html(f"""
<div class="counter-container">

    <div class="counter">
        <div class="counter-number">
            {ANOS_CASAMENTO}
        </div>
        <div class="counter-label">
            Anos de casamento
        </div>
    </div>

    <div class="counter">
        <div class="counter-number">
            {ANOS_JUNTOS}
        </div>
        <div class="counter-label">
            Anos de história
        </div>
    </div>

    <div class="counter">
        <div class="counter-number">
            ❤️
        </div>
        <div class="counter-label">
            Um só coração
        </div>
    </div>

    <div class="counter">
        <div class="counter-number">
            ∞
        </div>
        <div class="counter-label">
            Para sempre
        </div>
    </div>

</div>
""")


# ============================================================
# NOSSA HISTÓRIA
# ============================================================

st.html("""
<div class="section-title">

    <h2>Nossa História</h2>

    <p>
        Uma história que Deus começou a escrever
        e que ainda estamos vivendo.
    </p>

</div>
""")


# ============================================================
# LINHA DO TEMPO
# ============================================================

timeline = [

    (
        str(ANO_INICIO),
        "🌱 O começo",
        """
        Tudo começou com duas pessoas que ainda não
        imaginavam quantas páginas Deus escreveria
        através da história delas.

        Desde então, nossa caminhada começou a ganhar
        significado, sonhos e muitos momentos
        que guardamos no coração.
        """
    ),

    (
        str(ANO_CASAMENTO),
        "💍 O casamento",
        """
        O dia em que dissemos “sim” um ao outro
        e também assumimos diante de Deus
        o compromisso de caminhar juntos.

        Começava ali uma nova fase da nossa história.
        """
    ),

    (
        "Nossa família",
        "👨‍👩‍👧‍👦 O fruto do nosso amor",
        """
        E Deus nos presenteou com dois lindos filhos,
        frutos desse amor que construímos juntos.

        Isaque, nosso primeiro filho,
        que chegou para transformar ainda mais
        a nossa história.

        E depois veio Ianny, trazendo ainda mais
        alegria, amor e vida para a nossa família.

        Eles são parte da nossa história,
        parte da nossa aliança e uma das maiores
        bênçãos que Deus nos permitiu viver.
        """
    ),

    (
        "Nossa caminhada",
        "🏠 Nossa família",
        """
        Foram muitos momentos.

        Alegrias, desafios, conquistas,
        lágrimas, risadas, sonhos realizados
        e sonhos que ainda estão sendo construídos.

        Em cada etapa, aprendemos que amar também
        é escolher permanecer, cuidar, perdoar
        e caminhar lado a lado.
        """
    ),

    (
        "Todos esses anos",
        "🙏 Deus conosco",
        """
        Olhando para trás, podemos perceber
        que não caminhamos sozinhos.

        Deus esteve presente em cada detalhe,
        sustentando nossa casa, nossa família
        e nosso casamento.
        """
    ),

    (
        "Hoje",
        "❤️ 16 anos de casamento",
        """
        Hoje celebramos 16 anos de casamento.

        Mas, acima de tudo, celebramos a graça
        de Deus que nos permitiu chegar até aqui
        juntos.

        E ainda temos muitos capítulos para escrever.
        """
    )

]


for ano, titulo, texto in timeline:

    st.html(f"""
    <div class="timeline">

        <div class="timeline-item">

            <div class="timeline-year">
                {ano}
            </div>

            <div class="timeline-content">

                <h3>
                    {titulo}
                </h3>

                <p>
                    {texto}
                </p>

            </div>

        </div>

    </div>
    """)


# ============================================================
# FOTO 01 — NAMORO
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        ❤️ Onde tudo começou
    </div>

    <div class="story-photo-description">
        Nosso tempo de namoro.
    </div>

</div>
""")

if imagem_existe(FOTO_NAMORO):

    foto_namoro_base64 = arquivo_base64(FOTO_NAMORO)

    st.html(f"""
    <div style="
        width: 300px;
        height: 500px;
        margin: 25px auto 55px auto;
        overflow: hidden;
        border-radius: 28px;
        box-shadow: 0 18px 50px rgba(90,30,50,0.15);
        background-color: rgba(255, 248, 242, 0.5);
        
    ">
        <img
            src="data:image/jpeg;base64,{foto_namoro_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: contain;                
                display: block;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/01_namoro.jpg"
    )

# ============================================================
# FOTO 02 — CASAMENTO
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        💍 O nosso "sim"
    </div>

    <div class="story-photo-description">
        O dia em que começamos uma nova etapa da nossa história.
    </div>

</div>
""")

if imagem_existe(FOTO_CASAMENTO):

    foto_casamento_base64 = arquivo_base64(FOTO_CASAMENTO)

    st.html(f"""
    <div style="
        width: 100%;
        max-width: 350px;
        margin: 25px auto 55px auto;
        overflow: hidden;
        border-radius: 28px;
        box-shadow: 0 18px 50px rgba(90,30,50,0.15);
    ">
        <img
            src="data:image/jpeg;base64,{foto_casamento_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
                display: block;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/02_casamento.jpg"
    )

# ============================================================
# OS FRUTOS DO NOSSO AMOR
# ============================================================

st.html("""
<div class="section-title">

    <h2>Os frutos do nosso amor</h2>

    <p>
        Dois presentes que Deus colocou em nossas vidas.
    </p>

</div>

<div class="children-section">

    <div class="children-intro">

        O nosso amor não ficou apenas entre nós dois.
        Deus permitiu que ele desse frutos e nos presenteou
        com duas vidas preciosas que hoje fazem parte
        da nossa história.

    </div>

    <div class="children-grid">

        <div class="child-card">

            <div class="child-icon">
                👦
            </div>

            <div class="child-photo-title">
                Nosso primeiro filho
            </div>

            <div class="child-name">
                Isaque
            </div>

            <div class="child-description">
                Nosso primeiro presente de Deus,
                que chegou para transformar para sempre
                a nossa história.
            </div>

        </div>

        <div class="child-card">

            <div class="child-icon">
                👧
            </div>

            <div class="child-photo-title">
                Nossa segunda bênção
            </div>

            <div class="child-name">
                Ianny
            </div>

            <div class="child-description">
                Mais uma linda bênção que Deus acrescentou
                à nossa família, trazendo ainda mais
                alegria e amor para nossas vidas.
            </div>

        </div>

    </div>

</div>
""")

# ============================================================
# FOTO 03 — ISAQUE
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        👦 Nosso primeiro presente
    </div>

    <div class="story-photo-description">
        Isaque, nosso filho mais velho.
    </div>

</div>
""")

if imagem_existe(FOTO_ISAQUE):

    foto_isaque_base64 = arquivo_base64(FOTO_ISAQUE)

    st.html(f"""
    <div style="
        width: 300px;
        height: 500px;
        margin: 25px auto 55px auto;
        overflow: hidden;
        border-radius: 28px;
        box-shadow: 0 18px 50px rgba(90,30,50,0.15);
    ">
        <img
            src="data:image/jpeg;base64,{foto_isaque_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
                display: block;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/03_isaque.jpg"
    )


# ============================================================
# FOTO 04 — IANNY
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        👧 Mais uma bênção
    </div>

    <div class="story-photo-description">
        Ianny, nossa filha.
    </div>

</div>
""")

if imagem_existe(FOTO_IANNY):

    foto_ianny_base64 = arquivo_base64(FOTO_IANNY)

    st.html(f"""
    <div style="
        width: 300px;
        height: 500px;
        margin: 25px auto 55px auto;
        overflow: hidden;
        border-radius: 28px;
        box-shadow: 0 18px 50px rgba(90,30,50,0.15);
    ">
        <img
            src="data:image/jpeg;base64,{foto_ianny_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
                display: block;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/04_ianny.jpg"
    )



# ============================================================
# FOTO 05 — IGREJA
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        ⛪ Nossa caminhada com Deus
    </div>

    <div class="story-photo-description">
        Nossa família na Casa do Senhor.
    </div>

</div>
""")

if imagem_existe(FOTO_IGREJA):

    foto_igreja_base64 = arquivo_base64(FOTO_IGREJA)

    st.html(f"""
    <div style="
        width: 300px;
        height: 500px;
        margin: 25px auto 55px auto;
        overflow: hidden;
        border-radius: 28px;
        box-shadow: 0 18px 50px rgba(90,30,50,0.15);
    ">
        <img
            src="data:image/jpeg;base64,{foto_igreja_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
                display: block;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/05_igreja.jpg"
    )


# ============================================================
# FOTO 06 — FAMÍLIA
# ============================================================

st.html("""
<div class="story-photo">

    <div class="story-photo-title">
        👨‍👩‍👧‍👦 Nossa família
    </div>

    <div class="story-photo-description">
        Tudo aquilo que Deus permitiu construir.
    </div>

</div>
""")

if imagem_existe(FOTO_FAMILIA):

    foto_familia_base64 = arquivo_base64(FOTO_FAMILIA)

    st.html(f"""
    <div style="
        width: 300px;
        height: 600px;
        margin: 30px auto 65px auto;
        padding: 8px;
        overflow: hidden;
        border-radius: 32px;
        background: linear-gradient(
            135deg,
            #f8d7e3,
            #ffffff,
            #f3c6d7
        );
        box-shadow:
            0 25px 70px rgba(90,30,50,0.28),
            0 0 0 1px rgba(155,49,88,0.12);
    ">
        <img
            src="data:image/jpeg;base64,{foto_familia_base64}"
            style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center;
                display: block;
                border-radius: 25px;
            "
        >
    </div>
    """)

else:

    st.warning(
        "Foto não encontrada: imagem/06_familia.jpg"
    )

# ============================================================
# VERSÍCULO SOBRE OS FILHOS
# ============================================================

st.html("""
<div class="verse">

    <div class="verse-text">
        “Eis que os filhos são herança do Senhor,
        e o fruto do ventre, o seu galardão.”
    </div>

    <div class="verse-ref">
        Salmos 127:3
    </div>

</div>
""")


# ============================================================
# CARTA DE AMOR
# ============================================================

st.html("""
<div class="section-title">

    <h2>Para você, meu amor</h2>

</div>

<div class="letter">

    <h3>Minha esposa...</h3>

    <p>
        Se eu pudesse voltar no tempo e encontrar
        aquele jovem que começou essa história,
        eu diria para ele não ter medo de viver
        tudo aquilo que Deus estava preparando.
    </p>

    <p>
        Porque ao seu lado eu descobri que o amor
        não é apenas sentimento.
        É escolha.
        É cuidado.
        É companheirismo.
        É permanecer quando os dias são difíceis
        e comemorar juntos quando os dias são bons.
    </p>

    <p>
        Ao longo desses anos, nós crescemos,
        mudamos, aprendemos e construímos.
        E Deus nos permitiu viver algo ainda maior:
        formar uma família.
    </p>

    <p>
        E como fruto desse amor, Deus nos presenteou
        com dois filhos maravilhosos: Isaque,
        nosso primeiro filho, e Ianny.
    </p>

    <p>
        Eles são parte da nossa história,
        parte do nosso amor e uma das maiores
        bênçãos que Deus colocou em nossas mãos.
    </p>

    <p>
        Quando olho para nossa família,
        vejo muito mais do que uma fotografia.
        Vejo uma história.
        Vejo oração.
        Vejo lágrimas.
        Vejo conquistas.
        Vejo cuidado.
        Vejo a fidelidade de Deus.
    </p>

    <p>
        Obrigado por caminhar comigo.
        Obrigado por ser minha esposa,
        minha companheira e parte tão importante
        da minha vida.
    </p>

    <p>
        Depois de todos esses anos,
        eu ainda escolheria você.
    </p>

    <p>
        E se Deus permitir que nossa história
        continue por muitos e muitos anos,
        quero continuar escrevendo cada capítulo
        ao seu lado.
    </p>

</div>
""")


# ============================================================
# PALAVRAS QUE REPRESENTAM NOSSA HISTÓRIA
# ============================================================

st.html("""
<div class="section-title">

    <h2>Palavras que representam nossa história</h2>

</div>
""")


versiculos = [

    (
        "O amor é paciente, o amor é bondoso...",
        "1 Coríntios 13:4"
    ),

    (
        "E, sobre tudo isto, revesti-vos de amor, que é o vínculo da perfeição.",
        "Colossenses 3:14"
    ),

    (
        "Melhor é serem dois do que um...",
        "Eclesiastes 4:9"
    ),

    (
        "As muitas águas não podem apagar este amor.",
        "Cantares 8:7"
    )

]


for texto, referencia in versiculos:

    st.html(f"""
    <div class="verse">

        <div class="verse-text">
            “{texto}”
        </div>

        <div class="verse-ref">
            {referencia}
        </div>

    </div>
    """)


# ============================================================
# MÚSICA
# ============================================================

st.html("""
<div class="section-title">

    <h2>Uma música para nós</h2>

    <p>
        Algumas histórias podem ser contadas com palavras.
        Outras precisam de uma canção.
    </p>

</div>

<div class="music-box">

    <div class="music-heart">
        🎵❤️
    </div>

    <div class="music-title">
        Nossa música
    </div>

    <div class="music-description">

        Essa música é para você.

        <br>

        Para lembrar que, depois de todos esses anos,
        eu ainda escolheria você.

    </div>

</div>
""")

# ============================================================
# PLAYER DE MÚSICA FIXO
# ============================================================

musica_base64 = arquivo_base64(MUSICA)

if musica_base64:

    st.html(f"""
        <div class="music-fixed">

        <div class="music-fixed-title">
            ❤️ Nossa música — clique para começar
        </div>

        <audio
            controls
            loop
            preload="metadata"
            style="width:100%;"
        >

            <source
                src="data:audio/mpeg;base64,{musica_base64}"
                type="audio/mpeg"
            >

            Seu navegador não suporta áudio.

        </audio>

    </div>
    """)

else:

    st.info(
        "Coloque o arquivo `Eu e Você.mp3` dentro da pasta `musica`."
    )

# ============================================================
# ORAÇÃO
# ============================================================

st.html("""
<div class="prayer">

    <h3>Uma oração</h3>

    <p>
        Senhor, obrigado por todos esses anos.
    </p>

    <p>
        Obrigado pela vida da minha esposa,
        pela nossa família e pelos nossos filhos,
        Isaque e Ianny.
    </p>

    <p>
        Continue sendo o centro da nossa casa.
        Ensina-nos a amar, perdoar,
        cuidar e permanecer juntos.
    </p>

    <p>
        Que nossos filhos possam crescer vendo
        em nós um exemplo de amor, respeito,
        companheirismo e fé.
    </p>

    <p>
        Que os próximos anos sejam ainda mais
        cheios da Tua presença.
    </p>

    <p>
        Em nome de Jesus.
        Amém. ❤️
    </p>

</div>
""")


# ============================================================
# FRASE FINAL
# ============================================================

st.html("""
<div class="final-message">

    <div class="big-heart">
        ❤️
    </div>

    <h2>
        Eu escolheria você novamente.
    </h2>

    <p>
        Hoje, amanhã e em todos os dias
        que Deus nos permitir viver.
    </p>

    <p>
        Porque a nossa história ainda não terminou.
        Ela continua sendo escrita.
    </p>

    <p>
        E eu quero continuar escrevendo
        cada capítulo ao seu lado.
    </p>

</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    <div class="footer-heart">
        ❤️
    </div>

    Feito com amor para celebrar uma história
    que Deus permitiu construir.

    <br><br>

    “O que Deus ajuntou não o separe o homem.”

</div>
""")
