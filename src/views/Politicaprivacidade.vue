<template>
  <div class="privacy-page">
    <div class="glow-bg"></div>

    <div class="content-container">
      <header class="privacy-header">
        <h1 class="main-title">POLÍTICA DE <span class="text-red">PRIVACIDADE</span></h1>
        <p class="last-update">Última atualização: 1 de Abril de 2026</p>
        <div class="title-line"></div>
      </header>

      <section class="privacy-section">
        <div class="section-block">
          <h2 class="section-title">01. INFORMAÇÕES GERAIS</h2>
          <p>Esta Política de Privacidade descreve como os dados pessoais são recolhidos e tratados no âmbito do projeto fictício <strong>SL Benfica Fan Website</strong>. Este site é desenvolvido para fins exclusivamente educacionais e de portfólio.</p>
        </div>

        <div class="section-block">
          <h2 class="section-title">02. QUE DADOS RECOLHEMOS?</h2>
          <p>Recolhemos apenas os dados estritamente necessários para as funcionalidades do site:</p>
          <ul class="custom-list">
            <li><span class="bullet"></span> <strong>Dados de Contacto:</strong> Nome e endereço de e-mail através do formulário de contacto.</li>
            <li><span class="bullet"></span> <strong>Cookies de Navegação:</strong> Informações técnicas anónimas para melhorar a performance do site.</li>
          </ul>
        </div>

        <div class="section-block">
          <h2 class="section-title">03. FINALIDADE DO TRATAMENTO</h2>
          <p>Os seus dados são utilizados apenas para:</p>
          <ul class="custom-list">
            <li><span class="bullet"></span> Responder às mensagens enviadas através do formulário de contacto.</li>
            <li><span class="bullet"></span> Analisar o tráfego do site e melhorar a experiência do utilizador.</li>
          </ul>
        </div>

        <div class="section-block">
          <h2 class="section-title">04. COOKIES</h2>
          <p>Este site utiliza cookies para garantir que tenha a melhor experiência. Ao continuar a navegar, assume-se que aceita a nossa política de cookies. Pode desativar os cookies nas definições do seu navegador a qualquer momento.</p>
        </div>

        <div class="section-block">
          <h2 class="section-title">05. DIREITOS DO UTILIZADOR (RGPD)</h2>
          <p>De acordo com o RGPD em Portugal, o utilizador tem o direito de aceder, retificar, limitar ou solicitar a eliminação dos seus dados pessoais. Para exercer estes direitos, entre em contacto através do e-mail indicado na página de Contacto.</p>
        </div>
      </section>

      <div class="action-area">
        <router-link to="/" class="btn-back">
          <i class="fa-solid fa-arrow-left"></i> VOLTAR À HOME
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Montserrat:wght@400;600;700&display=swap');

.privacy-page {
  background-color: #050505;
  color: #ffffff;
  min-height: 100vh;
  padding: 120px 20px 80px;
  font-family: 'Montserrat', sans-serif;
  position: relative;
  overflow: hidden;
}

.glow-bg {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  height: 500px;
  background: radial-gradient(circle at top center, rgba(227, 6, 19, 0.1) 0%, transparent 70%);
  pointer-events: none;
}

.content-container {
  max-width: 900px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.privacy-header {
  text-align: center;
  margin-bottom: 60px;
}

.main-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 2.5rem;
  letter-spacing: 2px;
  margin-bottom: 10px;
}

.text-red { color: #E30613; }

.last-update {
  font-size: 0.85rem;
  opacity: 0.5;
  letter-spacing: 1px;
}

.title-line {
  width: 100px;
  height: 3px;
  background-color: #E30613;
  margin: 25px auto;
  box-shadow: 0 0 15px #E30613;
}

.section-block {
  margin-bottom: 45px;
  border-left: 2px solid rgba(227, 6, 19, 0.3);
  padding-left: 25px;
}

.section-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.1rem;
  color: #ffffff;
  margin-bottom: 20px;
  letter-spacing: 1.5px;
}

p {
  line-height: 1.8;
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
}

.custom-list {
  list-style: none;
  padding: 0;
  margin-top: 15px;
}

.custom-list li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 12px;
  color: rgba(255, 255, 255, 0.8);
}

.bullet {
  width: 6px;
  height: 6px;
  background: #E30613;
  border-radius: 50%;
  margin-top: 10px;
  box-shadow: 0 0 8px #E30613;
}

.action-area {
  text-align: center;
  margin-top: 60px;
}

.btn-back {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 15px 35px;
  background-color: #E30613;
  color: white;
  text-decoration: none;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: 4px;
  transition: all 0.3s ease;
  box-shadow: 0 5px 20px rgba(227, 6, 19, 0.3);
}

.btn-back:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(227, 6, 19, 0.5);
  filter: brightness(1.1);
}

@media (max-width: 768px) {
  .main-title { font-size: 1.8rem; }
  .section-block { padding-left: 15px; }
}
</style>