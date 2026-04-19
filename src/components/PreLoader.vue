<template>
  <Transition name="fade-out">
    <div v-if="progress < 100" class="preloader">
      <div class="loader-content">
        <h1 class="logo-benfica">SL BENFICA</h1>
        <div class="bar-container">
          <div class="bar" :style="{ width: progress + '%' }"></div>
        </div>
        <div class="status-text">A CARREGAR {{ progress }}%</div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, onMounted, defineEmits } from 'vue';

const progress = ref(0);
const emit = defineEmits(['finished']); 

onMounted(() => {
  const interval = setInterval(() => {
    if (progress.value < 100) {
      progress.value += Math.floor(Math.random() * 7) + 2;
    } else {
      progress.value = 100;
      clearInterval(interval);
      setTimeout(() => {
        emit('finished'); 
      }, 500); 
    }
  }, 100);
});
</script>

<style scoped>
.preloader {
  position: fixed; inset: 0; 
  background-color: #000;
  z-index: 9999; 
  display: flex; 
  align-items: center; 
  justify-content: center;
  color: #fff; 
  text-align: center;
}
.loader-content { 
  width: 300px; 

}
.logo-benfica { 
  font-size: 2.5rem; 
  color: #E10000; 
  margin-bottom: 20px; 
  font-weight: 900; 
}

.bar-container { 
  height: 2px; 
  background-color: #1a1a1a; 
  width: 100%; 
  border-radius: 10px; 
  overflow: hidden; 
}

.bar { 
  height: 100%; 
  background-color: #E10000; 
  transition: width 0.3s ease; 
}

.status-text { 
  margin-top: 10px; 
  font-size: 0.7rem; 
  opacity: 0.6; 
  letter-spacing: 2px; 
}

.fade-out-leave-active { 
  transition: all 0.6s ease; 
}

.fade-out-leave-to { 
  opacity: 0; 
  transform: scale(1.1); 
  filter: blur(10px); 
}
</style>