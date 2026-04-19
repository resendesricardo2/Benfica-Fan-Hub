<template>
  <section class="contact-section">
    <div class="tech-bg"></div>

    <div class="contact-container">
      <div class="contact-header">
        <h1 class="glitch-text">ENTRA EM <span class="highlight">CONTACTO</span></h1>
        <div class="red-divider"></div>
      </div>

      <div class="contact-grid">
        <div class="contact-card glass">
          <form>
            <div class="input-group">
              <label>NOME COMPLETO</label>
              <input type="text" id="nome" name="nome" v-model="nome" placeholder="Ex: João Silva" required />
              <div class="input-line"></div>
            </div>

            <div class="input-group">
              <label>E-MAIL</label>
              <input type="email" id="email" name="email" v-model="email" placeholder="exemplo@email.com" required />
              <div class="input-line"></div>
            </div>

            <div class="input-group">
              <label>MENSAGEM</label>
              <textarea rows="4" id="mensagem" name="mensagem" v-model="mensagem" placeholder="Como podemos ajudar?"></textarea>
              <div class="input-line"></div>
            </div>

            <button id="enviar" @click.prevent="enviar" class="btn-send">
              ENVIAR MENSAGEM
              <span class="btn-icon">→</span>
            </button>
          </form>
        </div>

        <div class="info-card glass">
          <div class="info-item">
            <h3 class="info-title">LOCALIZAÇÃO</h3>
            <p>Estádio do Sport Lisboa e Benfica</p>
            <a href="https://maps.app.goo.gl/AuYw4ieGNVnrqB6S8" target="_blank"><p>Av. Eusébio da Silva Ferreira, Lisboa</p></a>
          </div>

          <div class="info-item">
            <h3 class="info-title">LINHA BENFICA</h3>
            <p class="phone-number">217 219 500</p>
            <span class="phone-note">(*CHAMADA PARA A REDE FIXA NACIONAL)</span>
          </div>

          <a href="https://www.google.com/maps/search/?api=1&query=Estádio+da+Luz+Benfica" target="_blank" rel="noopener noreferrer"class="map-anchor">
          <div class="mini-map-placeholder">
          <div class="map-overlay">
          <span>VER NO MAPA</span>
          </div>
          </div>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"

const nome = ref("")
const email = ref("")
const mensagem = ref("")

const enviar = async () => {
  const response = await fetch("http://localhost:5000/enviar-formulario", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      nome: nome.value,
      email: email.value,
      mensagem: mensagem.value
    })
  })
  if (response.ok) {
    nome.value = ""
    email.value = ""
    mensagem.value = ""
    alert("Email enviado com sucesso! ✅")
  } else{
    alert("Ocorreu um erro ao enviar o ticket. ❌")
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;700;900&display=swap');

.contact-section {
  position: relative;
  min-height: 100vh;
  padding: 120px 20px 60px;
  background-color: #050505;
  color: white;
  font-family: 'Montserrat', sans-serif;
  overflow: hidden;
}

.tech-bg {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, rgba(227, 6, 19, 0.05) 1px, transparent 1px);
  background-size: 30px 30px;
  z-index: 1;
}

.contact-container {
  position: relative;
  z-index: 10;
  max-width: 1200px;
  margin: 0 auto;
}

.contact-header {
  text-align: center;
  margin-bottom: 60px;
}

.glitch-text {
  font-size: 3.5rem;
  font-weight: 900;
  font-family: 'Montserrat', sans-serif;
  font-style: italic;
  letter-spacing: -2px;
}

.highlight {
  color: #E30613;
  text-shadow: 0 0 20px rgba(227, 6, 19, 0.4);
}

.red-divider {
  width: 80px;
  height: 4px;
  background-color: #E30613;
  margin: 10px auto;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 30px;
}

.glass {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  padding: 40px;
}

.input-group {
  margin-bottom: 30px;
  position: relative;
}

.input-group label {
  display: block;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
  letter-spacing: 2px;
  color: #E30613;
  margin-bottom: 10px;
}

input, textarea {
  width: 100%;
  background-color: transparent;
  border: none;
  color: white;
  font-size: 1rem;
  padding: 10px 0;
  outline: none;
}

.input-line {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  width: 100%;
  transition: 0.3s;
}

input:focus + .input-line, 
textarea:focus + .input-line {
  background-color: #E30613;
  box-shadow: 0 0 10px #E30613;
}

.btn-send {
  width: 100%;
  background-color: #E30613;
  color: white;
  border: none;
  padding: 20px;
  font-family: 'Orbitron', sans-serif;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
  transition: 0.3s;
}

.btn-send:hover {
  background-color: #ff0000;
  box-shadow: 0 0 25px rgba(227, 6, 19, 0.4);
  transform: translateY(-2px);
}

.info-item a{
  margin-bottom: 40px;
  text-decoration: none;
  color: white;
}

.info-title {
  color: #E30613;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.9rem;
  margin-bottom: 15px;
}

.phone-number {
  font-size: 2.2rem;
  font-weight: 900;
  margin: 5px 0;
}

.phone-note {
  font-size: 0.65rem;
  opacity: 0.5;
}

.map-anchor {
  text-decoration: none;
  display: block; 
  color: inherit;
}

.mini-map-placeholder {
  height: 150px;
  background: url('https://images.unsplash.com/photo-1526778548025-fa2f459cd5ce?q=80&w=500') center/cover;
  border-radius: 2px;
  position: relative;
  cursor: pointer;
  filter: grayscale(1);
  transition: 0.3s;
}

.mini-map-placeholder:hover {
  transform: translateY(-3px); 
  border-color: #E30613;
  box-shadow: 0 10px 20px rgba(227, 6, 19, 0.2); 
}

.map-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
}

@media (max-width: 900px) {
  .contact-grid { grid-template-columns: 1fr; }
  .glitch-text { font-size: 2.2rem; }
}
</style>