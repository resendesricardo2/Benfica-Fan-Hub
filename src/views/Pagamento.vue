<template>
  <div class="checkout-wrapper">
    <div class="base-layer">
      <div class="grid-pattern"></div>
      <div class="glow-bg"></div>
    </div>

    <div class="checkout-content">
      <header class="checkout-header">
        <h1 class="title">FINALIZAR <span class="text-red">PAGAMENTO</span></h1>
        <p class="subtitle">Escolhe o teu método de pagamento</p>
      </header>

      <div class="checkout-grid">
        <div class="payment-methods">
          <div 
            v-for="metodo in metodos" 
            :key="metodo.id" 
            class="method-card"
            :class="{ active: selectedMethod === metodo.id }"
            @click="selectedMethod = metodo.id">
            <div class="method-icon">{{ metodo.icon }}</div>
            <div class="method-info">
              <span class="method-name">{{ metodo.nome }}</span>
              <span class="method-desc">{{ metodo.desc }}</span>
            </div>
            <div class="method-radio"></div>
          </div>
        </div>

        <div class="summary-section">
          <div class="summary-card">
            <h3>RESUMO DA ENCOMENDA</h3>
            <div class="summary-row">
              <span>Quota / Bilhete</span>
              <span>25.00€</span>
            </div>
            <div class="summary-row">
              <span>Taxa Digital</span>
              <span>0.00€</span>
            </div>
            <hr class="divider">
            <div class="summary-row total">
              <span>TOTAL</span>
              <span class="text-red">25.00€</span>
            </div>

            <button @click="processarPagamento" class="btn-pay" :disabled="!selectedMethod">
              CONFIRMAR E PAGAR
            </button>
            <p class="secure-note">🔒 Pagamento 100% Seguro</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const selectedMethod = ref('mbway');

const metodos = ref([
  { id: 'mbway', nome: 'MB WAY', desc: 'Pagamento imediato via telemóvel', icon: '📱' },
  { id: 'multibanco', nome: 'Multibanco', desc: 'Entidade e Referência', icon: '🏧' },
  { id: 'cartao', nome: 'Cartão de Crédito', desc: 'Mastercard ou Visa', icon: '💳' }
]);

const processarPagamento = () => {
  alert(`A processar pagamento via ${selectedMethod.value.toUpperCase()}...`);
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@400;700&display=swap');

.checkout-wrapper {
  background-color: #050505; 
  color: white; 
  min-height: 100vh;
  font-family: 'Montserrat', sans-serif; 
  position: relative; 
  overflow-x: hidden;
}

.checkout-content { 
    position: relative; 
    z-index: 10; 
    max-width: 1000px; 
    margin: 0 auto; 
    padding: 100px 20px; 
}

.checkout-header { 
    text-align: center; 
    margin-bottom: 50px; 
}

.title { 
    font-family: 'Orbitron'; 
    font-size: 2.2rem; 
    font-weight: 900; 
    letter-spacing: 2px; 
}

.text-red { 
    color: #E30613; 
    text-shadow: 0 0 20px rgba(227, 6, 19, 0.4); 
}

.checkout-grid { 
    display: grid; 
    grid-template-columns: 1fr 350px; 
    gap: 30px; 
}

.payment-methods { 
    display: flex; 
    flex-direction: column; 
    gap: 15px; 
}

.method-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 20px; border-radius: 15px; cursor: pointer;
  display: flex; align-items: center; gap: 20px;
  transition: all 0.3s ease; position: relative;
}

.method-card:hover { 
    background: rgba(255, 255, 255, 0.05); 
    transform: translateX(5px); 
}

.method-card.active {
  border-color: #E30613;
  background: rgba(227, 6, 19, 0.05);
  box-shadow: 0 0 20px rgba(227, 6, 19, 0.1);
}

.method-icon { 
    font-size: 1.5rem;
}

.method-name { 
    display: block; 
    font-weight: 700; 
    font-size: 1.1rem; 
}

.method-desc { 
    font-size: 0.8rem; 
    color: rgba(255,255,255,0.5); 
}

.summary-card {
  background: rgba(255, 255, 255, 0.03);
  padding: 30px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.05);
  position: sticky; top: 100px;
}

.summary-card h3 { 
    font-family: 'Orbitron'; 
    font-size: 1rem; 
    margin-bottom: 25px; 
}

.summary-row { 
    display: flex; 
    justify-content: space-between; 
    margin-bottom: 15px; 
    font-size: 0.9rem; 
}

.divider { 
    border: 0; 
    border-top: 1px solid rgba(255,255,255,0.1); 
    margin: 20px 0; 
}

.total { 
    font-weight: 900; 
    font-size: 1.2rem; 
}

.btn-pay {
  width: 100%; 
  margin-top: 25px;
  background-color: #E30613; 
  color: white;
  border: none; 
  padding: 15px; 
  border-radius: 8px;
  font-family: 'Orbitron'; 
  font-weight: 900; 
  font-size: 0.9rem;
  cursor: pointer; 
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(227, 6, 19, 0.3);
}

.btn-pay:hover:not(:disabled) { 
    background-color: #ff0814; 
    transform: translateY(-2px); 
    box-shadow: 0 0 20px rgba(227, 6, 19, 0.5); 
}

.btn-pay:disabled { 
    opacity: 0.5; 
    cursor: not-allowed; 
}

.secure-note { 
    text-align: center; 
    font-size: 0.7rem; 
    color: rgba(255,255,255,0.3); 
    margin-top: 15px; 
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
    transform: translateX(-50%); 
    width: 100%; 
    height: 500px; 
    background: radial-gradient(circle, rgba(227, 6, 19, 0.08) 0%, transparent 70%); 
}

@media (max-width: 850px) {
  .checkout-grid { 
    grid-template-columns: 1fr; 
}

  .summary-section { 
    order: -1; 
}
}
</style>