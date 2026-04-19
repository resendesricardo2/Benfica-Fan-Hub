<template>
  <div class="bilheteira-wrapper">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-bg"></div>
    </div>

    <div class="main-content">
      <div class="header-section">
        <div class="location-badge">
          <span class="pulse-red"></span>
          ESTÁDIO DA LUZ - BILHETEIRA OFICIAL
        </div>
        <h1 id="title" class="main-title">BILHETEIRA <span class="text-red">ONLINE</span></h1>
        <p id="subtitle" class="subtitle">Selecione uma bancada no estádio para ver os lugares disponíveis</p>
      </div>

      <div class="interactive-container">
        <div id="vista-estadio" class="view-section active">
            <svg viewBox="0 0 1000 700" xmlns="http://www.w3.org/2000/svg" class="stadium-svg">
              <defs>
                <radialGradient id="gradienteCampo" cx="50%" cy="50%" r="50%">
                  <stop offset="0%" style="stop-color:#1e3a24" />
                  <stop offset="100%" style="stop-color:#050505" />
                </radialGradient>
              </defs>
              
              <rect x="100" y="50" width="800" height="600" rx="200" fill="rgba(255,255,255,0.01)" stroke="rgba(255,255,255,0.05)" stroke-width="1" />
              
              <g id="relvado">
                <rect fill="url(#gradienteCampo)" x="250" y="200" width="500" height="300" rx="2" stroke="rgba(255,255,255,0.2)" stroke-width="1" />
                
                <rect x="250" y="200" width="500" height="300" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                
                <line x1="500" y1="200" x2="500" y2="500" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                
                <circle cx="500" cy="350" r="45" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                <circle cx="500" cy="350" r="2" fill="rgba(255,255,255,0.3)" />
                
                <rect x="250" y="260" width="80" height="180" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                <rect x="250" y="310" width="30" height="80" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                
                <rect x="670" y="260" width="80" height="180" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
                <rect x="720" y="310" width="30" height="80" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
              </g>

              <path class="setor-path" d="M250,180 Q500,140 750,180 L820,80 Q500,20 180,80 Z" @click="irParaBancada('Norte')" />
              <text x="500" y="115" class="label-setor">BANCADA EMIRATES</text>

              <path class="setor-path" d="M250,520 Q500,560 750,520 L820,620 Q500,680 180,620 Z" @click="irParaBancada('Sul')" />
              <text x="500" y="605" class="label-setor">BANCADA BTV</text>

              <path class="setor-path" d="M770,200 Q830,350 770,500 L880,580 Q960,350 880,120 Z" @click="irParaBancada('Nascente')" />
              <text x="855" y="350" class="label-setor" transform="rotate(90, 855, 350)">MAIS VANTAGENS</text>

              <path class="setor-path" d="M230,200 Q170,350 230,500 L120,580 Q40,350 120,120 Z" @click="irParaBancada('Poente')" />
              <text x="145" y="350" class="label-setor" transform="rotate(-90, 145, 350)">BANCADA SAGRES</text>
            </svg>
        </div>

        <div id="vista-setores" class="view-section">
          <div class="navigation-bar">
            <button class="btn-back" @click="voltarPara('estadio')">← VOLTAR AO MAPA</button>
          </div>
          <div id="lista-setores" class="grid-setores"></div>
        </div>

        <div id="vista-lugares" class="view-section">
          <div class="navigation-bar">
            <button class="btn-back" @click="voltarPara('setores')">← SETORES</button>
            <div class="legenda-container">
              <span class="leg-item livre">LIVRE</span>
              <span class="leg-item ocupado">OCUPADO</span>
              <span class="leg-item selecionado">O TEU LUGAR</span>
            </div>
          </div>
          
          <div class="seat-map-wrapper">
            <div id="grid-lugares" class="lugares-grid-system"></div>
          </div>

          <div class="checkout-hud">
            <div class="selection-info">
              <span class="hud-label">LUGARES SELECIONADOS</span>
              <div class="hud-value"><span id="contador">0</span></div>
            </div>
            <button class="btn-checkout primary" @click="finalizarCompra">FINALIZAR RESERVA</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const config = {
  'Norte': [13, 14, 15, 16],
  'Sul': [1, 2, 3, 4, 5, 6],
  'Nascente': [17, '16A', '20'],
  'Poente': [9, 10, 11, '12']
};

let bancadaAtual = "";

function irParaBancada(nome) {
  bancadaAtual = nome;
  document.getElementById('title').innerHTML = `BANCADA <span class="text-red">${nome.toUpperCase()}</span>`;
  
  const lista = document.getElementById('lista-setores');
  lista.innerHTML = "";
  config[nome].forEach(s => {
    const div = document.createElement('div');
    div.className = "setor-card";
    div.innerHTML = `<span>SETOR</span><strong>${s}</strong>`;
    div.onclick = () => irParaLugares(s);
    lista.appendChild(div);
  });
  trocarVista('vista-setores');
}

function irParaLugares(setor) {
  document.getElementById('title').innerHTML = `SETOR <span class="text-red">${setor}</span>`;
  const grid = document.getElementById('grid-lugares');
  grid.innerHTML = "";
  
  grid.innerHTML += `<div></div>`; 
  for(let n=1; n<=40; n++) {
    grid.innerHTML += `<div class="num-header">${n}</div>`;
  }

  const letras = ['O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'];
  letras.forEach(letra => {
    const label = document.createElement('div');
    label.className = "letra-fila";
    label.innerText = letra;
    grid.appendChild(label);

    for(let num=1; num<=40; num++) {
      const isOcupado = Math.random() > 0.7; 
      const div = document.createElement('div');
      div.className = `lugar ${isOcupado ? 'ocupado' : ''}`;
      div.onclick = () => selecionarLugar(div);
      grid.appendChild(div);
    }
  });
  trocarVista('vista-lugares');
}

function selecionarLugar(el) {
  if(el.classList.contains('ocupado')) return;
  el.classList.toggle('selecionado');
  document.getElementById('contador').innerText = document.querySelectorAll('.lugar.selecionado').length;
}

function trocarVista(id) {
  document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function voltarPara(tipo) {
  if(tipo === 'estadio') {
    document.getElementById('title').innerHTML = `BILHETEIRA <span class="text-red">ONLINE</span>`;
    trocarVista('vista-estadio');
  } else {
    irParaBancada(bancadaAtual);
  }
}

const router = useRouter();

function finalizarCompra() {
  // Verifica quantos lugares têm a classe 'selecionado'
  const qtd = document.querySelectorAll('.lugar.selecionado').length;
  
  if (qtd > 0) {
    // Se houver lugares, avança para a página de pagamento
    router.push('/pagamento');
  } else {
    // Caso contrário, avisa o utilizador
    alert("Por favor, selecione pelo menos um lugar!");
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@300;400;700;900&display=swap');

.bilheteira-wrapper {
  background-color: #050505;
  color: white;
  min-height: 100vh;
  padding: 100px 0;
  font-family: 'Montserrat', sans-serif;
  position: relative;
  overflow: hidden;
}

.base-layer { 
  position: absolute; 
  inset: 0; 
  z-index: 1; 
}

.grid-pattern {
  position: absolute; 
  inset: 0;
  background-image: radial-gradient(circle, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(circle, black, transparent 80%);
}

.glow-bg {
  position: absolute; 
  top: 0%; left: 50%; 
  transform: translateX(-50%);
  width: 120%; 
  height: 600px;
  background: radial-gradient(circle, rgba(227, 6, 19, 0.08) 0%, transparent 70%);
  pointer-events: none;
}

.main-content { 
  position: relative; 
  z-index: 10; 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 0 20px; 
}

.header-section { 
  text-align: center; 
  margin-bottom: 60px; 
}

.main-title { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 3rem; 
  font-weight: 900; 
  letter-spacing: 4px; 
}

.text-red { 
  color: #E30613; 
  text-shadow: 0 0 20px rgba(227, 6, 19, 0.5); 
}

.subtitle { 
  color: rgba(255,255,255,0.5); 
  margin-top: 10px; 
}

.location-badge {
  display: inline-flex; 
  align-items: center; 
  gap: 10px;
  background: rgba(255,255,255,0.05); 
  border: 1px solid rgba(255,255,255,0.1);
  padding: 8px 25px; 
  border-radius: 50px; 
  font-family: 'Orbitron', sans-serif; 
  font-size: 0.7rem;
}

.pulse-red {
  width: 8px; 
  height: 8px; 
  background-color: #E30613; 
  border-radius: 50%;
  box-shadow: 0 0 10px #E30613; 
  animation: blink 1.5s infinite;
}

.setor-path { 
  fill: rgba(255, 255, 255, 0.03); 
  stroke: rgba(255, 255, 255, 0.1); 
  cursor: pointer; 
  transition: 0.3s; 
}

.setor-path:hover { 
  fill: rgba(227, 6, 19, 0.3); 
  stroke: #E30613; 
}

.label-setor { 
  fill: rgba(255, 255, 255, 0.4); 
  font-family: 'Orbitron', sans-serif; 
  font-size: 13px; 
  text-anchor: middle; 
  pointer-events: none; 
}

.grid-setores { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); 
  gap: 20px; 
}

:deep(.setor-card) {
  background: rgba(255, 255, 255, 0.03); 
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 40px 20px; 
  border-radius: 15px; 
  text-align: center; 
  cursor: pointer; 
  transition: 0.3s;
}

:deep(.setor-card:hover) { 
  border-color: #E30613; 
  background: rgba(227, 6, 19, 0.1); 
  transform: translateY(-5px); 
}

:deep(.setor-card span) { 
  display: block; 
  color: #E30613; 
  font-family: 'Orbitron', sans-serif; 
  font-size: 0.7rem; 
  margin-bottom: 8px; 
}

:deep(.setor-card strong) { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 2rem; 
}

.seat-map-wrapper { 
  background-color: #0a0a0a; 
  border: 1px solid rgba(255,255,255,0.05); 
  padding: 40px; 
  border-radius: 20px; 
  overflow-x: auto; 
  margin: 30px 0; 
}

.lugares-grid-system { 
  display: grid; 
  grid-template-columns: 40px repeat(40, 1fr); 
  gap: 4px; 
  min-width: 1000px; 
}

:deep(.lugar) { 
  aspect-ratio: 1/1; 
  background-color: #3be771; 
  border-radius: 2px; 
  cursor: pointer; 
  transition: 0.2s; 
}

:deep(.lugar.ocupado) { 
  background-color: #E30613; 
  opacity: 0.2; 
  cursor: not-allowed; 
}

:deep(.lugar.selecionado) { 
  background-color: #faec22; 
  box-shadow: 0 0 15px #faec22; 
  transform: scale(1.2); 
  z-index: 5; 
}

.num-header { 
  font-size: 0.6rem; 
  opacity: 0.3; 
  text-align: center; 
}

.letra-fila { 
  font-size: 0.8rem; 
  font-weight: 900; 
  opacity: 0.5; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
}

.checkout-hud { 
  background: rgba(255,255,255,0.02); 
  border-top: 2px solid #E30613; 
  padding: 30px 50px; 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  border-radius: 15px; 
}

.hud-label { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 0.7rem; 
  opacity: 0.5; 
}

.hud-value { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 2.5rem; 
  color: #E30613; 
  font-weight: 900; 
}

.btn-checkout { 
  background-color: #E30613; 
  color: white; 
  border: none; 
  padding: 18px 50px; 
  font-family: 'Orbitron', sans-serif; 
  font-weight: 900; 
  cursor: pointer; 
  transition: 0.3s; 
  border-radius: 8px; 
}

.btn-checkout:hover { 
  transform: translateY(-3px); 
  box-shadow: 0 10px 20px rgba(227,6,19,0.4); 
}

.navigation-bar { 
  margin-bottom: 20px; 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
}

.btn-back { 
  background-color: transparent; 
  border: 1px solid rgba(255,255,255,0.2); 
  color: white; 
  padding: 10px 20px; 
  border-radius: 5px; 
  cursor: pointer; 
  font-family: 'Orbitron', sans-serif; 
}

.btn-back:hover {
  background-color: #E30613;
}

.legenda-container { 
  display: flex; 
  gap: 20px; 
  font-size: 0.7rem; 
  font-family: 'Orbitron', sans-serif; 
}

.leg-item::before { 
  content: ""; 
  display: inline-block; 
  width: 10px; 
  height: 10px; 
  margin-right: 8px; 
  border-radius: 2px; 
}

.livre::before { 
  background-color: #3be771; 
}

.ocupado::before { 
  background-color: #E30613; 
}

.selecionado::before { 
  background-color: #faec22; 
}

@keyframes blink { 50% { opacity: 0.4; } }

.view-section { 
  display: none; 
}

.view-section.active { 
  display: block; 
  animation: slideUp(30px); 
}

@keyframes slideUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
</style>