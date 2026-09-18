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
# CSS ESTILOS E LIMPEZA DE TELA
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

/* Esconde menus, linhas de desenvolvimento e elementos do GitHub */
#MainMenu {visibility: hidden;}
.stDeployButton {display:none;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stDecoration"] {display: none;}
.viewerBadge_link__1S137, .styles_viewerBadge__1yB5_, [data-testid="stGitHubLink"] {display: none !important;}
iframe[title="Manage app"] {display: none !important;}

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

.floating-hearts span:nth-child(1) { left: 5%; font-size: 22px; animation-delay: 0s; }
.floating-hearts span:nth-child(2) { left: 14%; font-size: 16px; animation-delay: 3s; }
.floating-hearts span:nth-child(3) { left: 24%; font-size: 28px; animation-delay: 7s; }
.floating-hearts span:nth-child(4) { left: 34%; font-size: 18px; animation-delay: 2s; }
.floating-hearts span:nth-child(5) { left: 45%; font-size: 24px; animation-delay: 6s; }
.floating-hearts span:nth-child(6) { left: 55%; font-size: 18px; animation-delay: 10s; }
.floating-hearts span:nth-child(7) { left: 65%; font-size: 30px; animation-delay: 4s; }
.floating-hearts span:nth-child(8) { left: 74%; font-size: 17px; animation-delay: 8s; }
.floating-hearts span:nth-child(9) { left: 82%; font-size: 25px; animation-delay: 1s; }
.floating-hearts span:nth-child(10) { left: 90%; font-size: 20px; animation-delay: 5s; }
.floating-hearts span:nth-child(11) { left: 30%; font-size: 15px; animation-delay: 11s; }
.floating-hearts span:nth-child(12) { left: 78%; font-size: 27px; animation-delay: 9s; }

@keyframes heartsUp {
    0% { transform: translateY(0) scale(0.6) rotate(0deg); opacity: 0; }
    10% { opacity: 0.45; }
    50% { transform: translateY(-45vh) scale(1) rotate(12deg); opacity: 0.55; }
    80% { opacity: 0.30; }
    100% { transform: translateY(-110vh) scale(0.8) rotate(-12deg); opacity: 0; }
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    text-align: center;
    padding: 70px 20px 60px 20px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(255, 230, 235, 0.95), rgba(255, 248, 242, 0.98));
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

</style>
""", unsafe_allow_html=True)

# Adiciona o elemento visual dos corações flutuantes na estrutura da página
st.html("""
<div class="floating-hearts">
    <span>❤️</span><span>💖</span><span>💕</span><span>❤️</span>
    <span>💖</span><span>💕</span><span>❤️</span><span>💖</span>
    <span>💕</span><span>❤️</span><span>💖</span><span>💕</span>
</div>
""")

# Siga com a renderização do conteúdo principal do seu site a partir daqui...
