<template>
  <div class="socio-wrapper">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-bg"></div>
    </div>

    <div class="main-content">
      <header class="header-section">
        <h1 class="main-title">CARTÃO DE <span class="text-red">SÓCIO</span></h1>
        <p class="subtitle">Gere o teu cartão digital e consulta os teus benefícios</p>
      </header>

      <div v-if="!isSocio && !showForm && !showLoginForm" class="join-container">
        <div class="join-card">
          <div class="benfica-logo-bg">
             <img src="/src/assets/slb-logo-new.svg" alt="SLB">
          </div>
          <h2>Torna-te Sócio Digital</h2>
          <p>Cria o teu cartão personalizado e acede a vantagens exclusivas no Estádio da Luz.</p>
          <div class="button-row">
    <button @click="showForm = true" class="btn-action">
      ADERIR AGORA
    </button>
    <button @click="showLoginForm = true" class="btn-socio">
      JÁ SOU SÓCIO
    </button>
  </div>
  </div>
  </div>

  <div v-else-if="!isSocio && showLoginForm" class="join-container">
        <div class="join-card form-card">
          <h2>Aceder ao Cartão</h2>
          <p>Introduz o teu número de sócio para gerar o cartão digital.</p>
          <div class="form-single-input">
            <input 
              v-model="loginNumeroSocio" 
              placeholder="Nº DE SÓCIO" 
              class="input-field highlight"
              type="text">
          </div>
          <div class="form-actions">
            <button @click="showLoginForm = false" class="btn-secondary">VOLTAR</button>
            <button @click="entrarComoSocio" class="btn-socio">ENTRAR</button>
          </div>
        </div>
      </div>

      <div v-else-if="!isSocio && showForm" class="join-container">
        <div class="join-card form-card">
          <h2>Dados do Sócio</h2>
          <div class="form-grid">
            <input v-model="form.nome" placeholder="Nome Completo" class="input-field">
            <input v-model="form.email" placeholder="Email" class="input-field">
            <input v-model="form.telemovel" placeholder="Telemóvel" class="input-field">
            <input v-model="form.morada" placeholder="Morada" class="input-field">
            <input v-model="form.localidade" placeholder="Localidade" class="input-field">
            <input v-model="form.cp" placeholder="Código Postal" class="input-field">
          </div>
          <div class="form-actions">
            <button @click="showForm = false" class="btn-secondary">CANCELAR</button>
            <button @click="tornarSocio" class="btn-action" :disabled="loading">
              {{ loading ? 'A PROCESSAR...' : 'CONFIRMAR ADESÃO' }}
            </button>
          </div>
        </div>
      </div>

      <div v-else class="card-display-container">
        <div class="member-card">
          <div class="card-inner">
            <div class="card-front">
              <div class="card-header">
                <div class="benfica-logo">
                  <img src="/src/assets/slb-logo-new.svg" alt="SLB" class="slb-crest">
                </div>
                <span class="card-type">{{ socioDados.tipo }}</span>
              </div>
              <div class="avatar-container">
                <label for="photo-upload" class="member-photo-placeholder">
                  <img v-if="userPhoto" :src="userPhoto" class="user-avatar" />
                  <span v-else class="upload-icon">👤</span>
                </label>
                <input id="photo-upload" type="file" @change="handlePhoto" hidden />
              </div>
              <div class="card-info">
                <div class="info-group">
                  <span class="label">NOME</span>
                  <span class="value">{{ nomeUtilizador }}</span>
                </div>
                <div class="info-row">
                  <div class="info-group">
                    <span class="label">Nº SÓCIO</span>
                    <span class="value">{{ socioDados.numero_socio }}</span>
                  </div>
                  <div class="info-group">
                    <span class="label">DESDE</span>
                    <span class="value">{{ socioDados.desde }}</span>
                  </div>
                </div>
              </div>
              <div class="qr-container">
                <div class="qr-code"></div>
                <span class="qr-label">SCAN PARA ENTRADA</span>
              </div>
            </div>
          </div>
        </div>

        <div class="stats-panel">
          <div class="stat-item">
            <span class="stat-label">QUOTAS</span>
            <span class="stat-value text-green">EM DIA</span>
          </div>
          <div class="stat-item">
            <span class="stat-label">PONTOS</span>
            <span class="stat-value">{{ socioDados.pontos }}</span>
          </div>
          <button class="btn-action">RENOVAR QUOTAS</button>
          <button class="btn-secondary" @click="downloadCartao">DOWNLOAD WALLET</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import html2canvas from 'html2canvas';

const isSocio = ref(false);
const showForm = ref(false);
const showLoginForm = ref(false);
const loading = ref(false);
const loginNumeroSocio = ref("");
const nomeUtilizador = ref("");
const userPhoto = ref(null);

const form = reactive({
  nome: '',
  email: '',
  telemovel: '',
  morada: '',
  localidade: '',
  cp: ''
});

const socioDados = ref({
  numero_socio: '',
  desde: '',
  tipo: 'SÓCIO RED',
  pontos: 0
});

async function tornarSocio() {
  if (!form.nome || !form.email) return alert("Preenche os dados obrigatórios!");
  
  loading.value = true;
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/socio/aderir`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form) 
    });
    
    const data = await res.json();
    
    if (res.ok) {
      isSocio.value = true;
      nomeUtilizador.value = form.nome;
      socioDados.value = {
        numero_socio: data.dados_cartao.numero_socio,
        desde: data.dados_cartao.desde,
        tipo: 'SÓCIO RED',
        pontos: data.dados_cartao.pontos
      };
    }
  } catch (err) {
    alert("Erro ao ligar ao servidor.");
  } finally {
    loading.value = false;
  }
}

async function entrarComoSocio() {
  if (!loginNumeroSocio.value) return alert("Por favor, introduz o teu número de sócio!");

  loading.value = true;
  try {
    const res = await fetch('http://localhost:5000/api/socio/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ numero_socio: loginNumeroSocio.value })
    });

    const data = await res.json();

    if (res.ok && data.status === "sucesso") {
      isSocio.value = true;
      nomeUtilizador.value = data.dados_cartao.nome;
      socioDados.value = {
        numero_socio: data.dados_cartao.numero_socio,
        desde: data.dados_cartao.desde,
        tipo: data.dados_cartao.tipo,
        pontos: data.dados_cartao.pontos
      };
      showLoginForm.value = false;
    } else {
      alert(data.mensagem || "Número de sócio não encontrado.");
    }
  } catch (err) {
    alert("Erro ao ligar ao servidor. Verifica se o Flask está ligado.");
  } finally {
    loading.value = false;
  }
}

async function downloadCartao() {
  const el = document.querySelector('.member-card');
  if (!el) return;

  try {
    const canvas = await html2canvas(el, {
      scale: 3,
      backgroundColor: null,
      useCORS: true,
      removeContainer: true, 
      logging: false
    });

    const dataUrl = canvas.toDataURL('image/png');
    
    const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

    if (isMobile && navigator.share) {

      const response = await fetch(dataUrl);
      const blob = await response.blob();
      const file = new File([blob], 'cartao-slb.png', { type: 'image/png' });

      await navigator.share({
        files: [file],
        title: 'Meu Cartão de Sócio SLB',
      });
    } else {

      const link = document.createElement('a');
      link.download = `cartao-slb-${socioDados.value.numero_socio || 'digital'}.png`;
      link.href = dataUrl;
      link.click();
    }
  } catch (err) {
    console.error("Erro ao gerar cartão:", err);
  }
}

function handlePhoto(e) {
  const file = e.target.files[0];
  if (file) userPhoto.value = URL.createObjectURL(file);
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;700&display=swap');

.form-card {
  max-width: 600px !important;
  background: rgba(10, 10, 10, 0.8) !important; 
  backdrop-filter: blur(20px); 
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 40px !important;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
}

.form-card h2 {
  font-family: 'Orbitron', sans-serif;
  letter-spacing: 2px;
  margin-bottom: 30px;
  text-transform: uppercase;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin: 30px 0;
}

.input-field {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 15px;
  border-radius: 12px;
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.input-field:focus {
  background: rgba(255, 255, 255, 0.05);
  border-color: #E30613;
  box-shadow: 0 0 15px rgba(227, 6, 19, 0.2);
  outline: none;
}

.input-field::placeholder {
  color: rgba(255, 255, 255, 0.3);
}

.form-actions {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-top: 10px;
}

.button-row {
  display: flex;
  gap: 15px;     
  justify-content: center;
  margin-top: 25px;
  width: 100%;
}

.btn-action {
  background-color: #E30613;
  color: white;
  border: none;
  padding: 15px 30px;
  font-family: 'Orbitron', sans-serif;
  font-weight: 900;
  border-radius: 10px;
  cursor: pointer;
  text-transform: uppercase;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(227, 6, 19, 0.3);
}

.btn-action:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(227, 6, 19, 0.5);
  background: #ff0717;
}

.btn-socio {
  background-color: #E30613;
  color: white;
  border: none;
  padding: 15px 30px;
  font-family: 'Orbitron', sans-serif;
  font-weight: 900;
  border-radius: 10px;
  cursor: pointer;
  text-transform: uppercase;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(227, 6, 19, 0.3);
}

.btn-socio:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(227, 6, 19, 0.5);
  background: #ff0717;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.03);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 15px 30px;
  font-family: 'Orbitron', sans-serif;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.3);
}

.socio-wrapper {
  background-color: #050505; 
  color: white;
  height: 100vh; 
  width: 100vw; 
  overflow: hidden;
  position: relative; 
  font-family: 'Montserrat', sans-serif;
}

.main-content {
  position: relative; 
  z-index: 10;
  display: flex; 
  flex-direction: column; 
  align-items: center;
  padding: 80px 20px 40px 20px; 
  height: 100%;
}

.header-section { 
    text-align: center; 
    margin-bottom: 40px; 
}

.main-title { 
    font-family: 'Orbitron'; 
    font-size: 2.5rem; 
    font-weight: 900; 
    letter-spacing: 2px; 
    margin: 15px 0; 
    line-height: 1.2;
    width: 100%;
    max-width: 100%;
}

.text-red { 
    color: #E30613; 
    text-shadow: 0 0 20px rgba(227, 6, 19, 0.6); 
}

.subtitle { 
    color: rgba(255,255,255,0.5); 
    font-size: 0.9rem; 
}

.location-badge {
  display: inline-flex; 
  align-items: center; 
  gap: 10px;
  background: rgba(255,255,255,0.03); 
  border: 1px solid rgba(255,255,255,0.1);
  padding: 8px 25px; 
  border-radius: 50px; 
  font-family: 'Orbitron'; 
  font-size: 0.7rem;
}

.join-container { 
    margin-top: 50px; 
    z-index: 20; 
}

.join-card {
  background: rgba(255,255,255,0.02); 
  border: 1px solid rgba(255,255,255,0.1);
  padding: 50px; 
  border-radius: 20px; 
  text-align: center; 
  max-width: 450px;
  backdrop-filter: blur(10px);
}

.benfica-logo-bg img { 
    width: 80px; 
    margin-bottom: 20px; 
    opacity: 0.8; 
}

.join-card h2 { 
    font-family: 'Orbitron'; 
    margin-bottom: 10px; 
    font-size: 1.5rem; 
}

.join-card p { 
    color: rgba(255,255,255,0.5); 
    margin-bottom: 30px; 
    font-size: 0.9rem; 
}

.card-display-container { 
    display: flex; 
    gap: 60px; 
    align-items: center; 
    animation: fadeIn 0.8s ease; 
}

.member-card {
  width: 450px; 
  height: 280px;
  background: linear-gradient(135deg, #1a1a1a 0%, #0a0a0a 100%);
  border-radius: 20px; 
  border: 1px solid rgba(255,255,255,0.1);
  box-shadow: 0 20px 50px rgba(0,0,0,0.5); 
  padding: 25px; 
  position: relative;
}

.card-header { 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    margin-bottom: 15px; 
}

.slb-crest { 
    width: 45px; 
}

.card-type { 
    font-family: 'Orbitron'; 
    font-weight: 900; 
    color: #E30613; 
    font-size: 1.1rem; 
}

.avatar-container { 
    margin-bottom: 15px; 
}

.member-photo-placeholder {
  width: 75px; 
  height: 75px; 
  border-radius: 50%;
  background: rgba(255,255,255,0.05); 
  border: 1px dashed rgba(255,255,255,0.2);
  display: flex; 
  align-items: center; 
  justify-content: center; 
  cursor: pointer; 
  overflow: hidden;
}

.user-avatar { 
    width: 100%; 
    height: 100%; 
    object-fit: cover; 
}

.upload-icon { 
    font-size: 1.8rem; 
    opacity: 0.3; 
}

.card-info .label { 
    display: block; 
    font-size: 0.6rem; 
    color: #666; 
    font-family: 'Orbitron'; 
}

.card-info .value { 
    font-size: 1.1rem; 
    font-weight: 700; 
    margin-bottom: 10px; 
    display: block; 
}

.info-row { 
    display: flex; 
    gap: 40px; 
}

.qr-container { 
    position: absolute; 
    right: 25px; 
    bottom: 25px; 
    text-align: center; 
}

.qr-code {
  width: 80px; 
  height: 80px; 
  background-color: white; 
  border-radius: 6px;
  background-image: url('https://api.qrserver.com/v1/create-qr-code/?size=80x80&data=SLB-MEMBER-RICARDO');
  background-size: cover;
}

.qr-label { 
    font-size: 0.5rem; 
    color: rgba(255,255,255,0.3); 
    margin-top: 5px; 
    display: block; 
}

.stats-panel { 
    display: flex; 
    flex-direction: column; 
    gap: 15px; 
    width: 300px; 
}

.stat-item {
  background: rgba(255,255,255,0.03); 
  border: 1px solid rgba(255,255,255,0.08);
  padding: 20px; 
  border-radius: 12px; 
  display: flex; 
  justify-content: space-between;
}

.stat-value { 
    font-family: 'Orbitron'; 
    font-weight: 900; 
}

.text-green { 
    color: #2ED573; 
}

.btn-action {
  background-color: #E30613; 
  color: white; 
  border: none; 
  padding: 18px;
  font-family: 'Orbitron'; 
  font-weight: 900; 
  border-radius: 8px; 
  cursor: pointer;
}

.btn-secondary {
  background-color: transparent; 
  border: 1px solid rgba(255,255,255,0.1);
  color: white; 
  padding: 15px; 
  font-family: 'Orbitron'; 
  border-radius: 8px; 
  cursor: pointer;
}

.base-layer { 
    position: absolute; 
    inset: 0; 
    z-index: 0; 
}

.grid-pattern {
  position: absolute; 
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}

.glow-bg {
  position: absolute; 
  top: -100px; 
  left: 50%; 
  transform: translateX(-50%);
  width: 100%; 
  height: 500px;
  background: radial-gradient(circle, rgba(227, 6, 19, 0.08) 0%, transparent 70%);
}

@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

@keyframes blink { 50% { opacity: 0.3; } }

@media (max-width: 768px) {
  .socio-wrapper {
    height: auto !important; 
    min-height: 100vh;
    display: flex !important;
    flex-direction: column;
    align-items: center;
    overflow-y: auto !important;
  }

  .main-content {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: flex-start;
    width: 100%;
    padding: 70px 15px 40px 15px !important; 
    box-sizing: border-box;
  }

  .header-section {
    width: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center; 
    margin-bottom: 25px;
  }

  .main-title {
    font-family: 'Orbitron', 'Montserrat', sans-serif !important; 
    font-size: 1.6rem !important; 
    line-height: 1.5 !important; 
    width: 100%;
    max-width: 320px; 
    margin: 10px auto !important; 
    text-transform: uppercase;
    color: white;
    display: block !important;
  }

  .main-title .text-red {
    display: inline-block;
    color: #E30613;
    font-family: inherit;
  }

  .form-card {
    width: 95% !important;
    max-width: 400px; 
    padding: 25px 15px !important;
    margin: 20px auto 0 auto !important; 
    box-sizing: border-box;
    display: block !important;
  }

  .form-grid {
    display: flex !important;
    flex-direction: column !important;
    gap: 15px;
    width: 100%;
  }

  .form-actions {
    display: flex !important;
    flex-direction: column !important; 
    gap: 12px;
    width: 100%;
    margin-top: 10px;
  }

  .btn-action, .btn-secondary {
    width: 100% !important; 
    padding: 16px !important;
    margin: 0 !important;
    box-sizing: border-box;
  }

   .button-row {
    flex-direction: column;
  }

  .card-display-container {
    display: flex !important;
    flex-direction: column;
    align-items: center !important;
    gap: 30px;
    width: 100%;
  }

  .member-card {
    width: 100%;
    max-width: 350px; 
    height: auto;
    aspect-ratio: 1.6 / 1;
    padding: 15px;
    margin: 0 auto;
  }
}
</style>