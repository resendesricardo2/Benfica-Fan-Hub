<script setup>
import { ref } from 'vue';
import PreLoader from './components/PreLoader.vue';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
import CookieModal from './components/CookieModal.vue'; 

const isPreloaderRunning = ref(true);
const cookieRef = ref(null); 
const onPreloaderDone = () => {
  isPreloaderRunning.value = false;
  if (cookieRef.value) {
    cookieRef.value.initBenficaCookies();
  }
};
</script>

<template>
  <PreLoader @finished="onPreloaderDone" />

  <div class="app-container" :class="{ 'hidden-content': isPreloaderRunning }">
    <Navbar />

    <main class="content">
      <router-view />
    </main>

    <Footer />
    
    <CookieModal ref="cookieRef" />
  </div>
</template>

<style>
html, body {
  margin: 0 !important;
  padding: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background-color: #050505 !important; 
  overflow-x: hidden; 
}

#app {
  width: 100%;
  margin: 0;
  padding: 0;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  transition: opacity 0.5s ease;
}

.hidden-content {
  opacity: 0;
  pointer-events: none; 
  height: 100vh;
  overflow: hidden;
}
</style>