<template>
  <footer class="footer-modern">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <div class="footer-blur-bg"></div>
    
    <div class="footer-container">
      <div class="footer-brand">
        <h2 class="brand-logo">SL <span class="text-red">BENFICA</span></h2>
        <p class="brand-mission">
          Onde a paixão pelo futebol une a nossa comunidade. <br>
          Juntos somos mais fortes.
        </p>
        
        <div class="social-links">
          <a href="https://www.facebook.com/SLBenfica/?locale=pt_PT" target="_blank" class="social-icon" aria-label="Facebook">
            <i class="fa-brands fa-facebook-f"></i>
          </a>
          <a href="https://www.instagram.com/slbenfica/" target="_blank" class="social-icon" aria-label="Instagram">
            <i class="fa-brands fa-instagram"></i>
          </a>
          <a href="https://x.com/SLBenfica?lang=pt" target="_blank" class="social-icon" aria-label="Twitter">
            <i class="fa-brands fa-x-twitter"></i>
          </a>
          <a href="https://www.youtube.com/slbenfica" target="_blank" class="social-icon" aria-label="YouTube">
            <i class="fa-brands fa-youtube"></i>
          </a>
        </div>
      </div>

      <div class="footer-links">
        <h3 class="footer-title">EXPLORAR</h3>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/bilheteira">Bilheteira</router-link></li>
          <li><router-link to="/classificacao">Classificação</router-link></li>
          <li><router-link to="/calendario">Calendário</router-link></li>
          <li><router-link to="/socio">Sócio Online</router-link></li>
          <li><router-link to="/contacto">Contacto</router-link></li>
        </ul>
      </div>

      <div class="footer-info">
        <h3 class="footer-title">ONDE ESTAMOS</h3>
        <div class="info-content">
          <p>Estádio da Luz</p>
          <a href="https://maps.app.goo.gl/AuYw4ieGNVnrqB6S8" target="_blank"><p>Av. Eusébio da Silva Ferreira, Lisboa</p></a>
          <a href="mailto:linhabenfica@slbenfica.pt" class="email-link">linhabenfica@slbenfica.pt</a>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="footer-bottom-wrapper">
        
        <div class="copyright-area">
          <p class="copyright-text">© 2026 SL BENFICA - TODOS OS DIREITOS RESERVADOS</p>
        </div>

        <div class="vertical-divider"></div>

        <div class="legal-area">
          <router-link to="/privacidade" class="legal-link">POLÍTICA DE PRIVACIDADE</router-link>
          <span class="dot-separator">•</span>
          <a href="https://www.livroreclamacoes.pt" target="_blank" class="legal-link">LIVRO DE RECLAMAÇÕES</a>
        </div>

      </div>
      <div class="tech-line-glow"></div>
    </div>
  </footer>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Montserrat:wght@400;700;900&display=swap');

.footer-modern {
  background-color: #050505;
  color: white;
  padding-top: 60px;
  font-family: 'Montserrat', sans-serif;
  border-top: 1px solid rgba(227, 6, 19, 0.2);
}

.footer-container {
  max-width: 1300px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 40px;
  padding: 0 40px 40px;
}

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  padding: 30px 40px;
  position: relative;
}

.footer-bottom-wrapper {
  max-width: 1300px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 25px;
}

.copyright-text {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.65rem;
  letter-spacing: 1px;
  opacity: 0.5;
  margin: 0;
}

.vertical-divider {
  width: 1px;
  height: 15px;
  background: rgba(227, 6, 19, 0.5);
}

.legal-area {
  display: flex;
  align-items: center;
  gap: 15px;
}

.legal-link {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.4);
  font-family: 'Orbitron', sans-serif;
  font-size: 0.65rem;
  letter-spacing: 1px;
  transition: 0.3s ease;
}

.legal-link:hover {
  color: #E30613;
}

.social-links { 
  display: flex; 
  gap: 12px; 
}

.social-icon {
  width: 38px; 
  height: 38px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex; 
  align-items: center; 
  justify-content: center;
  color: white; 
  border-radius: 4px; 
  transition: 0.3s;
  text-decoration: none;
}

.social-icon:hover { 
  background-color: #E30613; 
  border-color: #E30613; 
  box-shadow: 0 0 15px rgba(227, 6, 19, 0.5);
  transform: translateY(-3px);
}

.brand-logo { 
  font-size: 1.6rem; 
  font-weight: 900; 
  margin-bottom: 15px; 
}

.text-red { 
  color: #E30613; 
}

.brand-mission { 
  font-size: 0.85rem; 
  opacity: 0.6; 
  line-height: 1.5; 
  margin-bottom: 20px; 
}

.footer-title { 
  font-family: 'Orbitron', sans-serif; 
  font-size: 0.8rem; 
  letter-spacing: 2px; 
  margin-bottom: 20px; 
}

ul { 
  list-style: none; 
  padding: 0; 
}

ul li { 
  margin-bottom: 12px; 
}

ul li a { 
  text-decoration: none; 
  color: rgba(255, 255, 255, 0.5); 
  font-size: 0.85rem; 
  transition: 0.3s; 
}

ul li a:hover { 
  color: #E30613; 
  padding-left: 5px; 
}

.info-content p { 
  font-size: 0.85rem; 
  opacity: 0.6; 
  margin-bottom: 8px; 
}

.info-content a {
  text-decoration: none;
  color: inherit;
}

.email-link { 
  color: #E30613 !important; 
  text-decoration: none; 
  font-weight: 700; 
  font-size: 0.85rem; 
}

.tech-line-glow {
  width: 80px;
  height: 2px;
  background: #E30613;
  margin: 20px auto 0;
  box-shadow: 0 0 15px #E30613;
}

@media (max-width: 850px) {
  .footer-bottom-wrapper { flex-direction: column; gap: 15px; }
  .vertical-divider { display: none; }
  .footer-container { grid-template-columns: 1fr; text-align: center; }
  .social-links { justify-content: center; }
}
</style>