<template>
  <nav class="navbar-modern">
    <div class="nav-blur-bg"></div>
    <div class="nav-container">
      
      <div class="nav-brand">
        <router-link to="/" class="brand-link">
          <div class="logo-wrapper">
            <img :src="logoUrl" alt="SL Benfica" class="logo-icon"/>
          </div>
          <div class="brand-text">
            <span class="brand-main">SL BENFICA</span>
            <span class="brand-sub">OFFICIAL SITE</span>
          </div>
        </router-link>
      </div>

      <button class="menu-toggle" @click="isMenuOpen = !isMenuOpen" :class="{ 'is-active': isMenuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <ul class="nav-menu" :class="{ 'nav-open': isMenuOpen }">
        <li><router-link to="/" class="nav-item" @click="isMenuOpen = false" active-class="active">HOME</router-link></li>
        <li><router-link to="/bilheteira" class="nav-item" @click="isMenuOpen = false" active-class="active">BILHETEIRA</router-link></li>
        <li><router-link to="/classificacao" class="nav-item" @click="isMenuOpen = false" active-class="active">CLASSIFICAÇÃO</router-link></li>
        <li><router-link to="/calendario" class="nav-item" @click="isMenuOpen = false" active-class="active">CALENDÁRIO</router-link></li>
        <li><router-link to="/contacto" class="nav-item" @click="isMenuOpen = false" active-class="active">CONTACTO</router-link></li>
        <li class="mobile-only">
          <router-link to="/socio" class="btn-member" @click="isMenuOpen = false">SÓCIO ONLINE</router-link>
        </li>
      </ul>

      <div class="nav-actions desktop-only">
        <router-link to="/socio" class="btn-member" active-class="active">SÓCIO ONLINE</router-link>
      </div>

    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import logoUrl from '../assets/slb-logo-new.svg'
const isMenuOpen = ref(false)
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Montserrat:wght@400;700;900&display=swap');

.navbar-modern {
  width: 100%;
  height: 80px;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 2000;
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.nav-blur-bg {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  z-index: -1;
}

.nav-container {
  max-width: 1400px;
  width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
}

.nav-brand .brand-link {
  display: flex;
  align-items: center;
  gap: 15px;
  text-decoration: none;
}

.logo-icon {
  height: 45px;
  width: auto;
}

.brand-text {
  display: flex;
  flex-direction: column; 
}

.brand-main {
  color: #ffffff;
  font-family: 'Montserrat', sans-serif;
  font-weight: 900;
  font-size: 1.2rem;
  letter-spacing: -0.5px;
  line-height: 1;
}

.brand-sub {
  color: #E30613; 
  font-family: 'Orbitron', sans-serif;
  font-size: 0.6rem;
  letter-spacing: 2px;
}

.nav-menu {
  display: flex;
  list-style: none;
  gap: 35px;
  margin: 0;
  padding: 0;
}

.nav-item {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.7);
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  position: relative;
  padding: 10px 0;
}

.nav-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #E30613;
  transition: width 0.3s ease;
}

.nav-item:hover, .nav-item.active { 
  color: #ffffff; 
}

.nav-item:hover::after, .nav-item.active::after { 
  width: 100%; 
}

.btn-member {
  background-color: transparent;
  border: 1px solid #E30613;
  color: #ffffff;
  padding: 8px 20px;
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
  font-weight: 700;
  transition: all 0.3s ease;
  border-radius: 2px;
  text-decoration: none;
}

.btn-member:hover {
  background-color: #E30613;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  gap: 6px;
  background: transparent;
  border: none;
  cursor: pointer;
  z-index: 2100;
}

.menu-toggle span {
  width: 25px;
  height: 2px;
  background-color: #fff;
  transition: 0.3s;
}

.mobile-only { display: none; }

@media (max-width: 1024px) {
  .nav-container { 
    padding: 0 20px; 
  }

  .desktop-only { 
    display: none; 
  }

  .mobile-only { 
    display: block; 
  }
  
  .menu-toggle { 
    display: flex; 
  }

  .menu-toggle.is-active span:nth-child(1) { 
    transform: translateY(8px) rotate(45deg); 
  }

  .menu-toggle.is-active span:nth-child(2) { 
    opacity: 0; 
  }

  .menu-toggle.is-active span:nth-child(3) { 
    transform: translateY(-8px) rotate(-45deg); 
  }

  .nav-menu {
    position: fixed;
    top: 0;
    right: -100%;
    width: 280px;
    height: 100vh;
    background-color: #000;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: 0.4s;
    border-left: 1px solid rgba(227, 6, 19, 0.3);
  }

  .nav-menu.nav-open { 
    right: 0; 
  }
  
  .nav-item { 
  font-size: 1.1rem; 
}
}
</style>