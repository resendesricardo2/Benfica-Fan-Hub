<template>
  <div class="classificacao-wrapper">
    <div class="glow-bg"></div>

    <div class="header-section">
      <h1 class="main-title">CLASSIFICAÇÃO <span class="text-red">LIGA PORTUGAL BETCLIC</span></h1>
      <div class="update-badge">
        <span class="pulse-dot"></span> Atualizado em: {{ dataHoje }}
      </div>
      <div class="title-line"></div>
    </div>

    <div v-if="carregando" class="loading-state">
  <div class="loader-content">
    <div class="modern-spinner">
      <span></span>
      <span></span>
      <span></span>
    </div>
    <p class="loading-text">A CARREGAR DADOS DA LIGA</p>
  </div>
</div>

    <div v-else class="main-container">
      <div class="table-card">
        <table class="tabela-moderna">
          <thead>
            <tr>
              <th class="col-pos">POS</th>
              <th class="col-clube text-left">CLUBE</th>
              <th>J</th>
              <th>V</th>
              <th>E</th>
              <th>D</th>
              <th class="desktop-only">GM</th>
              <th class="desktop-only">GS</th>
              <th>DG</th>
              <th class="col-pts">PTS</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="equipa in listaEquipas" :key="equipa.pos" :class="{'row-benfica': equipa.nome.includes('Benfica')}">
              <td class="pos-num" :class="getPosClass(equipa.pos)">{{ equipa.pos }}º</td>
              <td class="clube-info">
                <div class="logo-container">
                  <img :src="equipa.logo" class="escudo-img" :alt="equipa.nome" />
                </div>
                <span class="clube-nome">{{ equipa.nome }}</span>
              </td>
              <td class="stat-num">{{ equipa.jogos }}</td>
              <td class="stat-num">{{ equipa.vitorias }}</td>
              <td class="stat-num">{{ equipa.empates }}</td>
              <td class="stat-num">{{ equipa.derrotas }}</td>
              <td class="stat-num desktop-only">{{ equipa.gm }}</td>
              <td class="stat-num desktop-only">{{ equipa.gs }}</td>
              <td class="stat-num dg-val" :class="{'text-green': equipa.diff > 0, 'text-red': equipa.diff < 0}">
                {{ equipa.diff > 0 ? '+' + equipa.diff : equipa.diff }}
              </td>
              <td class="pts-bold">{{ equipa.pontos }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="legendas-container">
        <div class="legendas-grid">
          <span class="legenda-item"><i class="dot blue"></i> Liga dos Campeões</span>
          <span class="legenda-item"><i class="dot blue-light"></i> Play-Off Champions</span>
          <span class="legenda-item"><i class="dot orange"></i> Liga Europa</span>
          <span class="legenda-item"><i class="dot green"></i> Liga Conferência</span>
          <span class="legenda-item"><i class="dot red-light"></i> Play-Off Despromoção</span>
          <span class="legenda-item"><i class="dot red"></i> Despromoção</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const listaEquipas = ref([]);
const carregando = ref(true);
const dataHoje = new Date().toLocaleDateString('pt-PT');

const getPosClass = (pos) => {
  if (pos === 1) return 'pos-champions';
  if (pos === 2) return 'pos-champions-playoff';
  if (pos === 3) return 'pos-uefa';
  if (pos === 4) return 'pos-uefa-coferencia';
  if (pos === 16) return 'pos-relegation-playoff';
  if (pos >= 17) return 'pos-relegation';
  return '';
};

const fetchClassificacao = async () => {
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/classificacao`);
    const data = await response.json();
    listaEquipas.value = data;
  } catch (error) {
    console.error("Erro ao carregar classificação:", error);
  } finally {
    carregando.value = false;
  }
};

onMounted(fetchClassificacao);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;600;800&display=swap');

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px; 
  width: 100%;
}

.loader-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.modern-spinner {
  position: relative;
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modern-spinner span {
  position: absolute;
  width: 100%;
  height: 100%;
  border: 4px solid transparent;
  border-top-color: #E30613;
  border-radius: 50%;
  animation: spin-modern 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
}

.modern-spinner span:nth-child(1) { 
  border-top-color: #E30613; 
  animation-delay: -0.45s; 
}

.modern-spinner span:nth-child(2) { 
  border-top-color: #fff; 
  width: 70%; 
  height: 70%; 
  animation-delay: -0.3s; 
}

.modern-spinner span:nth-child(3) { 
  border-top-color: rgba(227, 6, 19, 0.5); 
  width: 40%; height: 40%; 
  animation-delay: -0.15s; 
}

.loading-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.8rem;
  letter-spacing: 3px;
  color: #fff;
  text-transform: uppercase;
  animation: pulse-text 2s ease-in-out infinite;
}

@keyframes spin-modern {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse-text {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(0.95); }
}

.classificacao-wrapper {
  background-color: #050505;
  color: white;
  min-height: 100vh;
  padding: 100px 0;
  font-family: 'Montserrat', sans-serif;
  position: relative;
  overflow: hidden;
}

.glow-bg {
  position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 100%; height: 500px;
  background: radial-gradient(circle, rgba(227, 6, 19, 0.05) 0%, transparent 70%);
  pointer-events: none;
}

.main-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 2;
}

.header-section { 
text-align: center; 
margin-bottom: 50px; 
}

.main-title { 
font-family: 'Orbitron', sans-serif; 
font-size: 2.5rem; 
letter-spacing: 2px; 
margin: 0; 
}

.text-red { 
color: #E30613; 
text-shadow: 0 0 15px rgba(227, 6, 19, 0.3); 
}

.title-line { 
width: 80px; 
height: 4px; 
background-color: #E30613; 
margin: 20px auto; 
box-shadow: 0 0 15px #E30613; 
}

.update-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,0.05);
  padding: 6px 15px;
  border-radius: 20px;
  font-size: 0.75rem;
  color: #888;
  margin-top: 15px;
  border: 1px solid rgba(255,255,255,0.1);
}

.pulse-dot {
  width: 6px; 
  height: 6px; 
  background-color: #00ff88; 
  border-radius: 50%;
  box-shadow: 0 0 10px #00ff88;
  animation: pulse 2s infinite;
}

.table-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  overflow-x: auto;
}

.tabela-moderna {
  width: 100%;
  border-collapse: collapse;
  min-width: 800px;
}

.tabela-moderna thead tr {
  background: rgba(255, 255, 255, 0.03);
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.tabela-moderna th {
  padding: 20px;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
  color: #E30613;
  letter-spacing: 1px;
}

.tabela-moderna td {
  padding: 15px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.03);
  text-align: center;
}

.tabela-moderna tbody tr { 
  transition: 0.3s; 
}

.tabela-moderna tbody tr:hover { 
  background: rgba(255, 255, 255, 0.05); 
}

.row-benfica {
  background: rgba(227, 6, 19, 0.08) !important;
  position: relative;
}
.row-benfica::after {
  content: ''; 
  position: absolute; 
  left: 0; top: 0; 
  bottom: 0; 
  width: 4px; 
  background-color: #E30613; 
  box-shadow: 0 0 15px #E30613;
}

.row-benfica .clube-nome { 
  font-weight: 800; 
  color: #fff; 
}

.pos-num { 
  font-family: 'Orbitron', sans-serif; 
  font-weight: 900; 
  font-size: 1.1rem; 
}

.clube-info { 
  display: flex; 
  align-items: center; 
  gap: 15px; 
  text-align: left; 
}

.logo-container {
  width: 35px; 
  height: 35px; 
  background: rgba(255,255,255,0.03); 
  border-radius: 8px; 
  padding: 5px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
}

.escudo-img { 
  width: 100%; 
  height: 100%; 
  object-fit: contain; 
}

.clube-nome { 
  font-size: 0.95rem; 
  font-weight: 600; 
  color: #ccc; 
}

.stat-num { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 0.9rem; 
  color: #aaa; 
}

.pts-bold { 
  font-family: 'Orbitron', sans-serif; 
  font-weight: 900; 
  font-size: 1.2rem; 
  color: #fff; 
}

.pos-champions { 
  color: #3b82f6; 
  text-shadow: 0 0 10px rgba(59, 130, 246, 0.5); 
}

.pos-champions-playoff { 
  color: #7caaf3; 
}

.pos-uefa { 
  color: #f97316; 
}

.pos-uefa-coferencia { 
  color: #22c55e; 
}

.pos-relegation-playoff {
  color: #ce3f3f;
}

.pos-relegation { 
  color: #ef4444; 
}

.legendas-container { 
  margin-top: 30px; 
  padding: 20px; 
  background: rgba(0,0,0,0.3); 
  border-radius: 10px; 
}

.legendas-grid { 
  display: flex; 
  flex-wrap: wrap; 
  gap: 20px; 
  justify-content: center; 
}

.legenda-item { 
  display: flex; 
  align-items: center; 
  gap: 8px; 
  font-size: 0.7rem; 
  color: #666; 
  text-transform: uppercase; 
  font-weight: 600; 
}

.dot { 
  width: 8px; 
  height: 8px; 
  border-radius: 2px; 
}

.dot.blue { 
  background-color: #3b82f6; 
  box-shadow: 0 0 5px #3b82f6; 
}

.dot.blue-light { 
  background-color: #7caaf3; 
}

.dot.orange { 
  background-color: #f97316; 
}

.dot.green { 
  background-color: #22c55e; 
}

.dot.red { 
  background-color: #ef4444; 
}

.dot.red-light { 
  background-color: #ce3f3f; 
}

.text-green { 
  color: #22c55e; 
}

.text-red { 
  color: #ef4444; 
}

@keyframes pulse {
  0% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.2); }
  100% { opacity: 1; transform: scale(1); }
}

@media (max-width: 768px) {
  .desktop-only { 
  display: none; 
  }

  .main-title { 
  font-size: 1.5rem; 
  }

  .tabela-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin-bottom: 20px;
    border-radius: 12px;
  }

  .tabela-moderna {
    min-width: 600px; 
  }

  .tabela-moderna th, .tabela-moderna td { 
    padding: 10px 8px; 
    font-size: 0.85rem;
  }

  .col-hide-mobile {
    display: none;
  }
}
</style>