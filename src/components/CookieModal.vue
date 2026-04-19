<template>
  <transition name="slide-up">
    <div v-if="isOpen" class="cookie-overlay">
      <div class="cookie-card">
        <div class="card-scanner"></div>

        <div class="cookie-content">
          <div class="cookie-header">
            <div class="icon-container">
              <i class="fa-solid fa-cookie-bite"></i>
            </div>
            <h3 class="cookie-title">POLÍTICA DE <span class="text-red">COOKIES</span></h3>
          </div>

          <p class="cookie-text">
            Olá, <span class="text-highlight">Benfiquista!</span> Este site utiliza cookies para otimizar a tua experiência de navegação e garantir a segurança dos teus dados.
          </p>

          <div class="cookie-actions">
            <button @click="closeModal" class="btn-secondary">DEFINIÇÕES</button>
            <button @click="closeModal" class="btn-primary">ACEITAR TODOS</button>
          </div>
        </div>
        
        <div class="status-light"></div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref } from 'vue';
const isOpen = ref(true);
const closeModal = () => { isOpen.value = false; };
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Montserrat:wght@400;600&display=swap');

.cookie-overlay {
  position: fixed;
  bottom: 30px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  z-index: 9999;
  padding: 0 20px;
}

.cookie-card {
  background: rgba(10, 10, 10, 0.95);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(227, 6, 19, 0.3);
  width: 100%;
  max-width: 600px;
  padding: 30px;
  border-radius: 4px; 
  position: relative;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), inset 0 0 20px rgba(227, 6, 19, 0.05);
}

.card-scanner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #E30613, transparent);
  box-shadow: 0 0 10px #E30613;
}

.cookie-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}

.icon-container {
  color: #E30613;
  font-size: 1.5rem;
  filter: drop-shadow(0 0 5px rgba(227, 6, 19, 0.5));
}

.cookie-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 1rem;
  letter-spacing: 2px;
  margin: 0;
}

.text-red { color: #E30613; }

.cookie-text {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  margin-bottom: 25px;
}

.text-highlight {
  color: #ffffff;
  font-weight: 600;
}

.cookie-actions {
  display: flex;
  gap: 15px;
  justify-content: flex-end;
}

button {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 12px 25px;
  cursor: pointer;
  border-radius: 2px;
  transition: all 0.3s ease;
  letter-spacing: 1px;
}

.btn-primary {
  background-color: #E30613;
  border: 1px solid #E30613;
  color: white;
  box-shadow: 0 0 15px rgba(227, 6, 19, 0.3);
}

.btn-primary:hover {
  background-color: #ff0a1a;
  box-shadow: 0 0 25px rgba(227, 6, 19, 0.6);
  transform: translateY(-2px);
}

.btn-secondary {
  background-color: transparent;
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
}

.btn-secondary:hover {
  border-color: #E30613;
  color: #E30613;
  background: rgba(227, 6, 19, 0.05);
}

.status-light {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 4px;
  height: 4px;
  background-color: #E30613;
  border-radius: 50%;
  box-shadow: 0 0 8px #E30613;
}

.slide-up-enter-active, .slide-up-leave-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}
.slide-up-enter-from, .slide-up-leave-to {
  transform: translateY(100px);
  opacity: 0;
}

@media (max-width: 600px) {
  .cookie-actions { flex-direction: column; }
  .cookie-card { padding: 20px; }
}
</style>