<template>
  <section class="match-hero-premium">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-effect"></div>
    </div>

    <div class="main-content-container">
      
      <div v-if="loading" class="loading-wrapper">
        <div class="spinner"></div>
      </div>

      <div v-else-if="proximoJogo" class="main-content-inner">
        <div class="match-header">
          <div class="location-badge">
            <span class="pulse-red"></span>
            {{ proximoJogo.estadio }}
          </div>
          <h1 class="match-main-title">PRÓXIMO <span class="text-red">JOGO</span></h1>
          <p class="match-subtitle">
            {{ proximoJogo.dataExtenso }} | {{ proximoJogo.hora }} | {{ proximoJogo.competicao }}
          </p>
        </div>

        <div class="battle-glass-container">
          <div class="team-card">
            <div class="crest-wrapper">
              <img :src="proximoJogo.homeLogo" :alt="proximoJogo.homeName" class="crest-img">
            </div>
            <h2 class="team-label">{{ proximoJogo.homeName }}</h2>
          </div>

          <div class="vs-orbital">
            <div class="vs-ring"></div>
            <div class="vs-energy"></div>
            <span class="vs-text">VS</span>
          </div>

          <div class="team-card">
            <div class="crest-wrapper">
              <img :src="proximoJogo.awayLogo" :alt="proximoJogo.awayName" class="crest-img" @error="handleImageError">
            </div>
            <h2 class="team-label">{{ proximoJogo.awayName }}</h2>
          </div>
        </div>

        <div class="actions-group">
          <router-link to="/bilheteira" class="btn-glass primary">COMPRAR BILHETE</router-link>
          <router-link to="/plantel" class="btn-glass secondary">VER PLANTEL</router-link>
        </div>
      </div>

      <div v-else class="main-content-inner">
        <div class="match-header">
          <h1 class="match-main-title">SEM JOGOS <span class="text-red">AGENDADOS</span></h1>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const BENFICA_ID = 1903; 
const proximoJogo = ref(null);
const loading = ref(true);

const fetchProximoJogo = async () => {
  try {
    loading.value = true;
    const response = await fetch(`${import.meta.env.VITE_API_URL}/jogos`);
    const allMatches = await response.json();
    const match = allMatches.find(m => 
      (m.status === 'TIMED' || m.status === 'SCHEDULED') && 
      (m.homeTeam.id === BENFICA_ID || m.awayTeam.id === BENFICA_ID)
    );

    if (match) {
      const dateObj = new Date(match.utcDate);
      const isHome = match.homeTeam.id === BENFICA_ID;
      
      proximoJogo.value = {
        homeName: match.homeTeam.nome.toUpperCase(),
        homeLogo: match.homeTeam.id === BENFICA_ID ? '/src/assets/slb-logo-new.svg' : match.homeTeam.logo,
        awayName: match.awayTeam.nome.toUpperCase(),
        awayLogo: match.awayTeam.id === BENFICA_ID ? '/src/assets/slb-logo-new.svg' : match.awayTeam.logo,
        estadio: isHome ? 'ESTÁDIO DA LUZ' : 'ESTÁDIO VISITANTE',
        dataExtenso: dateObj.toLocaleDateString('pt-PT', { day: '2-digit', month: 'long' }).toUpperCase(),
        hora: dateObj.toLocaleTimeString('pt-PT', { hour: '2-digit', minute: '2-digit' }),
        competicao: 'LIGA PORTUGAL BETCLIC'
      };
    }
  } catch (error) {
    console.error("Erro ao carregar o próximo jogo dinâmico:", error);
  } finally {
    loading.value = false;
  }
};

const handleImageError = (e) => {
  e.target.src = 'https://via.placeholder.com/150?text=LOGO';
};

onMounted(fetchProximoJogo);
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;900&display=swap');

.match-hero-premium {
  position: relative;
  min-height: 90vh; 
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #050505;
  color: white;
  font-family: 'Montserrat', sans-serif;
  overflow: hidden;
  padding: 60px 0;
}

.base-layer { 
position: absolute; 
inset: 0; 
z-index: 1; 
}

.grid-pattern {
  position: absolute; 
  inset: 0;
  background-image: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
  background-size: 50px 50px;
  mask-image: radial-gradient(circle, black, transparent 90%);
}

.glow-effect {
  position: absolute; 
  top: 50%; 
  left: 50%; 
  transform: translate(-50%, -50%);
  width: 100%; 
  height: 100%;
  background: radial-gradient(circle, rgba(227, 6, 19, 0.1) 0%, transparent 70%);
  pointer-events: none;
}

.main-content-container {
  position: relative; 
  z-index: 10; 
  width: 100%; 
  max-width: 1200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; 
  min-height: 90vh; 
}

.main-content-inner {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.match-header { 
margin-bottom: 30px; 
text-align: center; 
}

.match-main-title {
  font-family: 'Orbitron', sans-serif; 
  font-size: 3rem; 
  font-weight: 900;
  margin: 15px 0; 
  letter-spacing: 4px; 
  text-shadow: 0 0 20px rgba(255, 255, 255, 0.1);
}

.text-red {
  color: #E30613;
  text-shadow: 0 0 15px rgba(227, 6, 19, 0.5);
}

.location-badge {
  display: inline-flex; 
  align-items: center; 
  gap: 10px;
  background: rgba(255,255,255,0.07); 
  border: 1px solid rgba(255,255,255,0.1);
  padding: 8px 25px; 
  border-radius: 50px; 
  font-family: 'Orbitron', sans-serif;
  font-size: 0.8rem; 
  letter-spacing: 2px;
}

.match-subtitle { 
font-size: 1rem; 
color: #aaa; 
font-weight: 500; 
letter-spacing: 1px; 
}

.pulse-red {
  width: 8px; 
  height: 8px; 
  background-color: #E30613; 
  border-radius: 50%;
  box-shadow: 0 0 12px #E30613; 
  animation: blink 1.5s infinite;
}

.battle-glass-container {
  display: flex; 
  align-items: center; 
  justify-content: space-around;
  width: 90%; 
  background: rgba(255, 255, 255, 0.03); 
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.08); 
  border-radius: 24px;
  padding: 50px; 
  margin-bottom: 40px; 
  box-shadow: 0 40px 100px rgba(0,0,0,0.6);
}

.crest-wrapper {
  width: 160px; 
  height: 160px; 
  display: flex; 
  align-items: center; 
  justify-content: center;
  transition: transform 0.5s ease;
}

.crest-img { 
width: 100%; 
filter: drop-shadow(0 0 15px rgba(255, 255, 255, 0.1)); 
}

.team-card:hover .crest-wrapper { 
transform: scale(1.1) rotate(5deg); 
}

.team-label {
  margin-top: 25px; 
  font-family: 'Orbitron', sans-serif;
  font-weight: 900; 
  font-size: 1.8rem; 
  letter-spacing: 1px; 
  text-align: center;
}

.vs-orbital { 
  position: relative;
  width: 140px;
  height: 140px; 
  display: flex; 
  align-items: center; 
  justify-content: center; 
}

.vs-text {
  font-family: 'Orbitron', sans-serif; 
  font-size: 3.5rem; 
  color: #E30613;
  z-index: 5; 
  text-shadow: 0 0 30px rgba(227, 6, 19, 0.8);
}

.vs-ring {
  position: absolute; 
  width: 100%; 
  height: 100%;
  border: 2px dashed rgba(227, 6, 19, 0.4); 
  border-radius: 50%;
  animation: rotate 15s linear infinite;
}

.actions-group { 
  display: flex; 
  gap: 25px; 
}

.btn-glass {
  padding: 16px 40px; 
  font-weight: 900; 
  text-transform: uppercase;
  letter-spacing: 2px; 
  border-radius: 8px; 
  cursor: pointer;
  transition: 0.3s all cubic-bezier(0.4, 0, 0.2, 1);
  font-family: 'Montserrat', sans-serif; 
  font-size: 0.9rem;
  text-decoration: none; 
  display: inline-block;
}

.primary { 
  background-color: #E30613; 
  color: white; 
  border: none; 
  box-shadow: 0 8px 25px rgba(227, 6, 19, 0.4); 
}

.secondary { 
  background: rgba(255,255,255,0.05); 
  color: white; 
  border: 1px solid rgba(255,255,255,0.2); 
  backdrop-filter: blur(10px); 
}

.btn-glass:hover { 
  transform: translateY(-5px); 
  filter: brightness(1.2); }

.loading-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.spinner {
  width: 50px; 
  height: 50px; 
  border: 5px solid rgba(227, 6, 19, 0.1);
  border-top: 5px solid #E30613; 
  border-radius: 50%; 
  animation: rotate 1s linear infinite;
}

@keyframes blink { 50% { opacity: 0.4; } }

@keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

@media (max-width: 768px) {
  .match-hero-premium {
    padding: 100px 0 60px 0; 
    min-height: auto;
    display: block; 
  }

  .main-content-container {
    min-height: auto;
    padding-top: 20px;
  }

  .match-header {
    text-align: center;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .location-badge {
    margin-bottom: 20px;
    font-size: 0.7rem;
    padding: 6px 15px;
  }

  .match-main-title { 
    font-size: clamp(1.6rem, 8vw, 2.2rem); 
    line-height: 1.1;
    margin: 10px 0;
    text-align: center;
    width: 100%;
  }

  .match-subtitle {
    text-align: center;
    font-size: 0.8rem;
    padding: 0 10px;
    width: 100%;
  }

  .battle-glass-container { 
    flex-direction: column; 
    gap: 30px; 
    padding: 40px 15px;
    width: 92%;
    margin: 20px auto 30px auto;
    display: flex;
    align-items: center; 
    justify-content: center;
  }

  .team-card {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .crest-wrapper {
    width: 120px;
    height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .crest-img {
    width: 100%;
    object-fit: contain;
    filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.1));
  }

  .team-label {
    font-size: 1.2rem;
    margin-top: 15px;
    text-align: center;
    width: 100%;
    padding: 0 10px;
  }

  .vs-orbital {
    height: auto; 
    aspect-ratio: 1 / 1; 
    display: flex;
    align-items: center;
    justify-content: center;
    width: 90px; 
    max-width: 90px;
    padding: 0;
    margin: 0 auto; 
  }

  .vs-text { 
    font-size: 2rem; 
  }

  .vs-ring {
    width: 100%;
    height: 100%;
    border-radius: 50%; 
  }

 
  .actions-group { 
    flex-direction: column;
    width: 100%;
    padding: 0 25px;
    gap: 12px;
    display: flex;
    align-items: center;
  }

  .btn-glass {
    width: 100%;
    max-width: 320px; 
    text-align: center;
    padding: 14px 0;
    display: block;
  }
}
</style>