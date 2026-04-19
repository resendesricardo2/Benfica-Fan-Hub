<template>
  <div class="socio-wrapper">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-bg"></div>
    </div>

    <div class="main-content">
      
      <header class="header-section">
        <div class="location-badge">
          <span class="pulse-red"></span>
          CENTRAL DE JOGOS
        </div>
        
        <h1 class="main-title">
          <span class="text-white">BENFICA</span> 
          <span class="text-red">JOGOS</span>
        </h1>
        
        <p class="subtitle">Acompanha os últimos resultados e os próximos confrontos do SL Benfica</p>
      </header>

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>A CARREGAR CALENDÁRIO...</p>
      </div>

      <section v-else class="calendar-section">
        
        <div class="section-group">
          <div class="section-header">
            <span class="history-indicator">● ÚLTIMOS RESULTADOS</span>
            <h2 class="calendar-title">HISTÓRICO <span class="text-red">RECENTE</span></h2>
          </div>
          
          <div class="results-grid">
            <div v-for="res in resultadosAnteriores" :key="res.id" class="result-card">
              <div class="res-meta">{{ res.competicao }} | {{ res.data }}</div>
              <div class="res-score-row">
                <span class="res-team">SLB</span>
                <span class="score-box" :class="res.resultado">
                  {{ res.golosSLB }} - {{ res.golosOpp }}
                </span>
                <span class="res-team">{{ res.siglaOpp }}</span>
              </div>
              <div class="res-opp-name">{{ res.oponente }}</div>
            </div>
          </div>
        </div>

        <div class="section-group" style="margin-top: 60px;">
          <div class="section-header">
            <div class="live-indicator"><span class="dot"></span> EM DESTAQUE</div>
            <h2 class="calendar-title">PRÓXIMOS <span class="text-red">ENCONTROS</span></h2>
          </div>
          
          <div class="matches-grid">
            <div v-for="jogo in proximosJogos" :key="jogo.id" class="match-card">
              <div class="match-date">
                <span class="day">{{ jogo.dia }}</span>
                <span class="month">{{ jogo.mes }}</span>
              </div>
              
              <div class="match-teams">
                <div class="team">
                  <img :src="jogo.isHome ? '/src/assets/slb-logo-new.svg' : jogo.oponenteLogo" 
                       class="team-logo" @error="handleImageError">
                  <span class="team-name">{{ jogo.nomeCasa }}</span>
                </div>
                
                <span class="vs">VS</span>
                
                <div class="team">
                  <img :src="!jogo.isHome ? '/src/assets/slb-logo-new.svg' : jogo.oponenteLogo" 
                       class="team-logo" @error="handleImageError">
                  <span class="team-name">{{ jogo.nomeFora }}</span>
                </div>
              </div>
              
              <div class="match-info">
                <div class="info-item"><span>📍</span> {{ jogo.estadio }}</div>
                <div class="info-item"><span>🕒</span> {{ jogo.hora }}</div>
                <router-link to="/bilheteira" class="btn-ticket">BILHETEIRA</router-link>
              </div>
            </div>
          </div>
        </div>

      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const BENFICA_ID = 1903;
const resultadosAnteriores = ref([]);
const proximosJogos = ref([]);
const loading = ref(true);

const formatDate = (dateStr) => {
  const d = new Date(dateStr);
  return d.toLocaleDateString('pt-PT', { day: '2-digit', month: 'short' }).toUpperCase().replace('.', '');
};

const fetchDados = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${import.meta.env.VITE_API_URL}/jogos`);
    const allMatches = await response.json();

    resultadosAnteriores.value = allMatches
      .filter(m => m.status === 'FINISHED' && (m.homeTeam.id === BENFICA_ID || m.awayTeam.id === BENFICA_ID))
      .slice(-4)
      .map(m => {
        const isHome = m.homeTeam.id === BENFICA_ID;
        const slbGoals = isHome ? m.score.home : m.score.away;
        const oppGoals = isHome ? m.score.away : m.score.home;
        let resClass = slbGoals > oppGoals ? 'vitoria' : (slbGoals < oppGoals ? 'derrota' : 'empate');

        return {
          id: m.id,
          data: formatDate(m.utcDate),
          competicao: 'LIGA PORTUGAL',
          oponente: isHome ? m.awayTeam.nome : m.homeTeam.nome,
          siglaOpp: isHome ? m.awayTeam.tla : m.homeTeam.tla,
          golosSLB: slbGoals,
          golosOpp: oppGoals,
          resultado: resClass
        };
      }).reverse();

    proximosJogos.value = allMatches
      .filter(m => (m.status === 'TIMED' || m.status === 'SCHEDULED') && (m.homeTeam.id === BENFICA_ID || m.awayTeam.id === BENFICA_ID))
      .slice(0, 2)
      .map(m => {
        const isHome = m.homeTeam.id === BENFICA_ID;
        const d = new Date(m.utcDate);
        const rawTime = d.toLocaleTimeString('pt-PT', { hour: '2-digit', minute: '2-digit' });
        const finalTime = rawTime === '00:00' ? 'A DEFINIR' : rawTime;

        return {
          id: m.id,
          dia: d.getDate().toString().padStart(2, '0'),
          mes: d.toLocaleString('pt-PT', { month: 'short' }).toUpperCase().replace('.', ''),
          isHome: isHome,
          nomeCasa: m.homeTeam.nome.toUpperCase(),
          nomeFora: m.awayTeam.nome.toUpperCase(),
          oponenteLogo: isHome ? m.awayTeam.logo : m.homeTeam.logo,
          estadio: isHome ? 'ESTÁDIO DA LUZ' : (m.venue ? m.venue.toUpperCase() : `ESTÁDIO DO ${m.homeTeam.nome.toUpperCase()}`),
          hora: finalTime
        };
      });

  } catch (error) {
    console.error("Erro ao carregar dados:", error);
  } finally {
    loading.value = false;
  }
};

const handleImageError = (e) => {
  e.target.src = 'https://via.placeholder.com/50?text=?';
};

onMounted(fetchDados);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;700&display=swap');

.socio-wrapper {
  background-color: #050505; 
  color: white; 
  min-height: 100vh; 
  width: 100%;
  position: relative; 
  font-family: 'Montserrat', sans-serif; 
  overflow-x: hidden;
}

.main-content { 
  position: relative; 
  z-index: 10; 
  display: flex; 
  flex-direction: column; 
  align-items: center; 
  padding: 100px 20px 60px; 
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
  transform: translateX(-50%); width: 100%; 
  height: 500px; 
  background: radial-gradient(circle, rgba(227, 6, 19, 0.08) 0%, transparent 70%); 
}

.header-section { 
  text-align: center; 
  margin-bottom: 70px; 
}

.main-title { 
  font-family: 'Orbitron'; 
  font-size: 3.5rem; 
  letter-spacing: 4px; 
  margin: 15px 0; 
  font-weight: 900; 
  text-transform: uppercase; 
}

.text-red { 
  color: #E30613; 
  text-shadow: 0 0 25px rgba(227, 6, 19, 0.7); 
}

.subtitle { 
  color: rgba(255,255,255,0.7); 
  font-size: 1rem; 
  max-width: 600px; 
  margin: 0 auto; 
}

.location-badge { 
  display: inline-flex; 
  align-items: center; 
  gap: 8px; 
  background: rgba(255,255,255,0.03); 
  border: 1px solid rgba(255,255,255,0.1); 
  padding: 8px 20px; 
  border-radius: 50px; 
  font-family: 'Orbitron'; 
  font-size: 0.7rem; 
}

.calendar-section { 
  width: 100%; 
  max-width: 1100px; 
}

.results-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
  gap: 15px; 
  margin-top: 20px; 
}

.result-card { 
  background: rgba(255,255,255,0.02); 
  border-left: 4px solid #E30613; 
  padding: 25px 20px; 
  border-radius: 12px; 
  display: flex; 
  flex-direction: column; 
  gap: 8px; 
}

.res-score-row { 
  display: grid; 
  grid-template-columns: 1fr auto 1fr; 
  align-items: center; gap: 10px; 
}

.score-box { 
  background-color: rgba(0,0,0,0.5); 
  padding: 4px 12px; 
  border-radius: 6px; 
  font-family: 'Orbitron'; 
  font-size: 1.2rem; 
  border: 1px solid rgba(255,255,255,0.1); 
  text-align: center; 
}

.score-box.vitoria { 
  color: #2ED573; 
  border-color: #2ED573; 
}

.score-box.empate { 
  color: #ffa502; 
  border-color: #ffa502; 
}

.score-box.derrota { 
  color: #ff4757; 
  border-color: #ff4757; 
}

.matches-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
  gap: 20px; 
  margin-top: 20px; 
}

.match-card { 
  background: rgba(255,255,255,0.02); 
  border: 1px solid rgba(255,255,255,0.05); 
  border-radius: 20px; 
  padding: 25px; 
  position: relative; 
  transition: 0.3s; 
  backdrop-filter: blur(10px); 
}

.match-card:hover { 
  border-color: #E30613; 
  transform: translateY(-5px); 
}

.match-date { 
  position: absolute; 
  top: 20px; 
  right: 20px; 
  background: rgba(227,6,19,0.1); 
  padding: 10px; 
  border-radius: 12px; 
  text-align: center; 
}

.match-date .day { 
  display: block; 
  font-family: 'Orbitron'; 
  color: #E30613; 
  font-weight: 900; 
  font-size: 1.2rem; 
}

.match-teams { 
  display: flex; 
  align-items: center; 
  justify-content: space-around; 
  margin: 30px 0; 
}

.team { 
  display: flex; 
  flex-direction: column; 
  align-items: center; 
  gap: 10px; 
  width: 40%; 
}

.team-logo { 
  width: 60px; 
  height: 60px; 
  object-fit: contain; 
}
.team-name { 
  font-size: 0.8rem; 
  font-weight: 700; 
  text-align: center; 
}

.vs { 
  font-family: 'Orbitron'; 
  color: #E30613; 
  font-size: 0.8rem; 
  opacity: 0.3; 
}

.match-info { 
  border-top: 1px solid rgba(255,255,255,0.05); 
  padding-top: 15px; 
}

.info-item { 
  font-size: 0.85rem; 
  color: rgba(255,255,255,0.8); 
  margin-bottom: 8px; 
  display: flex; 
  align-items: center; 
  gap: 10px; 
}

.btn-ticket { 
  display: block; 
  width: 100%; 
  margin-top: 15px; 
  text-align: center; 
  border: 1px solid #E30613; 
  color: #E30613; padding: 12px 0; 
  border-radius: 8px;
   font-family: 'Orbitron'; 
   font-size: 0.8rem; 
   font-weight: 900; 
   text-decoration: none; 
   transition: 0.3s; 
  }

.btn-ticket:hover { 
  background-color: #E30613; 
  color: white; 
  box-shadow: 0 0 20px rgba(227,6,19,0.4); 
}

.spinner { 
  width: 40px; 
  height: 40px; 
  border: 4px solid rgba(227,6,19,0.1); 
  border-top: 4px solid #E30613; 
  border-radius: 50%; 
  animation: spin 1s linear infinite; 
  margin: 0 auto 20px; 
}

@keyframes spin { to { transform: rotate(360deg); } }

.pulse-red { 
  width: 6px; 
  height: 6px; 
  background-color: #E30613; 
  border-radius: 50%; display: inline-block; 
  animation: pulse 1.5s infinite; 
}

@keyframes pulse { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(2.5); opacity: 0; } }

@media (max-width: 768px) {
  .main-title { 
    font-size: clamp(1.8rem, 10vw, 2.5rem); 
    letter-spacing: 2px;
    line-height: 1.2;
    padding: 0 10px;
    margin-bottom: 10px;
  }

  .subtitle {
    font-size: 0.9rem;
    padding: 0 20px;
  }

  .header-section {
    margin-bottom: 40px;
  }

  .results-grid {
    grid-template-columns: 1fr; 
    gap: 10px;
  }

  .matches-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }

  .match-card {
    padding: 20px;
  }

  .match-date {
    top: 15px;
    right: 15px;
    padding: 6px;
  }

  .match-date .day {
    font-size: 1rem;
  }

  .match-teams {
    margin: 40px 0 20px;
    gap: 5px;
  }

  .team-logo {
    width: 50px;
    height: 50px;
  }

  .team-name {
    font-size: 0.75rem;
  }

  .calendar-title {
    font-size: 1.4rem;
  }
}
</style>