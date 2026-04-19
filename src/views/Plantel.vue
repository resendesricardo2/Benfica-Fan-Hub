<template>
  <div class="plantel-wrapper">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-bg"></div>
    </div>

    <div class="main-content">
      <header class="header-section">
        <div class="location-badge">LIGA PORTUGAL | PLANTEL OFICIAL</div>
        <h1 class="main-title">{{ matchName }}</h1>
      </header>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>A SINCRONIZAR SETORES...</p>
      </div>

      <div v-else class="squads-container">
        <div v-for="(plantel, nomeEquipa) in squads" :key="nomeEquipa" class="team-block">
          <h2 class="team-name-title">{{ nomeEquipa }}</h2>
          
          <div v-for="(jogadores, grupoID) in agrupar(plantel)" :key="grupoID" class="posicao-section">
            <h3 class="posicao-header">{{ traduzirGrupo(grupoID) }}</h3>
            
            <div class="players-grid">
              <div v-for="jogador in jogadores" :key="jogador.nome" class="player-card">
                <div class="player-info">
                  <span class="player-name">{{ jogador.nome }}</span>
                  <span class="player-nat">{{ jogador.nacionalidade || 'N/A' }}</span>
                </div>
                <div class="player-accent"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const squads = ref({});
const matchName = ref('A carregar confronto....');
const loading = ref(true);

const fetchDados = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${import.meta.env.VITE_API_URL}/plantel-match`);
    const data = await response.json();
    if (data.erro) throw new Error(data.erro);
    squads.value = data.squads;
    matchName.value = data.match;
  } catch (err) {
    console.error("Erro na ligação à API:", err);
  } finally {
    loading.value = false;
  }
};

const agrupar = (lista) => {
  const grupos = { 'GK': [], 'DEF': [], 'MID': [], 'OFF': [], 'EXTRA': [], 'COACH': [] };

  const FORÇAR_AVANÇADOS = ['Andreas Schjelderup', 'Franjo Ivanovic', 'Bruma'];
  const FORÇAR_MÉDIOS = ['João Rêgo', 'Fredrik Aursnes', 'Manu Silva', 'Leandro Barreiro Martins'];

  lista.forEach(j => {
    const nome = j.nome;
    const p = j.posicao || '';
    const role = j.role || 'PLAYER';

    if (FORÇAR_AVANÇADOS.includes(nome)) {
      grupos['OFF'].push(j);
    }
    else if (FORÇAR_MÉDIOS.includes(nome)) {
      grupos['MID'].push(j);
    }
    else if (role === 'COACH' || role === 'ASSISTANT_COACH' || p === 'Coach') {
      grupos['COACH'].push(j);
    } 
    else if (p.includes('Goalkeeper')) {
      grupos['GK'].push(j);
    } 
    else if (p.includes('Midfield')) {
      grupos['MID'].push(j);
    }
    else if (p.includes('Defen') || p.includes('Back')) {
      grupos['DEF'].push(j);
    } 
    else if (p.includes('Offence') || p.includes('Forward') || p.includes('Winger') || p.includes('Striker')) {
      grupos['OFF'].push(j);
    } 
    else {
      grupos['EXTRA'].push(j);
    }
  });

  const ordem = ['GK', 'DEF', 'MID', 'OFF', 'EXTRA', 'COACH'];
  const res = {};
  ordem.forEach(k => { if (grupos[k].length > 0) res[k] = grupos[k]; });
  return res;
};

const traduzirGrupo = (id) => {
  const t = { 
    'GK': 'GUARDA-REDES', 'DEF': 'DEFESAS', 'MID': 'MÉDIOS', 
    'OFF': 'AVANÇADOS', 'EXTRA': 'OUTROS', 'COACH': 'EQUIPA TÉCNICA' 
  };
  return t[id] || id;
};

onMounted(fetchDados);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;700&display=swap');

.plantel-wrapper {
  background-color: #050505;
  color: white;
  min-height: 100vh;
  position: relative;
  font-family: 'Montserrat', sans-serif;
  overflow-x: hidden;
}

.base-layer { 
  position: absolute; 
  inset: 0; 
  z-index: 1; 
  pointer-events: none; 
}

.grid-pattern { 
  position: absolute; 
  inset: 0; 
  background-image: radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px); 
  background-size: 40px 40px; 
}

.glow-bg { 
  position: absolute; 
  top: 0; 
  left: 50%; 
  transform: translateX(-50%); 
  width: 100%; 
  height: 600px; 
  background: radial-gradient(circle, rgba(227, 6, 19, 0.12) 0%, transparent 70%); 
}

.main-content { 
  position: relative; 
  z-index: 10; 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 100px 20px 60px;
}

.header-section { 
  text-align: center; 
  margin-bottom: 80px; 
}

.location-badge { 
  font-family: 'Orbitron'; 
  color: #E30613; 
  font-size: 0.8rem; 
  letter-spacing: 4px; 
  margin-bottom: 15px; 
}

.main-title { 
  font-family: 'Orbitron'; 
  font-size: 2.8rem; 
  letter-spacing: 6px; 
  text-transform: uppercase; 
}

.team-block { 
  margin-bottom: 100px; 
  background: rgba(255,255,255,0.02); 
  padding: 50px; 
  border-radius: 24px; 
  border: 1px solid rgba(255,255,255,0.05); 
}

.team-name-title { 
  font-family: 'Orbitron'; 
  font-size: 2rem; 
  color: #E30613; 
  border-left: 6px solid #E30613; 
  padding-left: 25px; 
  margin-bottom: 50px; 
}

.posicao-header { 
  font-family: 'Orbitron'; 
  color: #444; 
  font-size: 0.9rem; 
  letter-spacing: 4px; 
  margin-bottom: 25px; 
}

.players-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
  gap: 20px; 
}

.player-card { 
  background: rgba(255, 255, 255, 0.03); 
  border: 1px solid rgba(255, 255, 255, 0.08); 
  padding: 24px; 
  border-radius: 14px; 
  display: flex; 
  justify-content: space-between; 
  align-items: center;
  transition: 0.3s;
}

.player-card:hover { 
  border-color: #E30613; 
  background: rgba(227, 6, 19, 0.06); 
  transform: translateY(-4px); 
}

.player-name { 
  font-weight: 700; 
  font-size: 0.95rem; 
  text-transform: uppercase; 
}

.player-nat { 
  font-size: 0.75rem; 
  color: #888; 
  display: block; 
  margin-top: 5px; 
}

.player-accent { 
  width: 4px; 
  height: 22px; 
  background-color: #E30613; 
  border-radius: 2px; 
}

.loading-state { 
  text-align: center; 
  padding: 150px; 
  font-family: 'Orbitron'; 
  color: #E30613; 
}

.spinner { 
  width: 50px; 
  height: 50px; 
  border: 5px solid rgba(227, 6, 19, 0.1); 
  border-top-color: #E30613; 
  border-radius: 50%; 
  animation: spin 1s linear infinite; 
  margin: 0 auto 25px; 
}

@keyframes spin { to { transform: rotate(360deg); } }
</style>