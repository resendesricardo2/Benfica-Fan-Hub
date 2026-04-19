import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue' 
import BilheteiraView from '../views/Bilheteira.vue'
import ClassificacaoView from '../views/Classificacao.vue'
import ConctactoView from '../views/Conctacto.vue'
import PoliticaprivacidadeView from '../views/Politicaprivacidade.vue'
import CalendarioView from '../views/Calendario.vue'
import SocioView from '../views/Socio.vue'
import PlantelView from '../views/Plantel.vue'
import PagamentoView from '../views/Pagamento.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/bilheteira', component: BilheteiraView },
  { path: '/classificacao', component: ClassificacaoView },
  { path: '/contacto', component: ConctactoView },
  { path: '/privacidade', component: PoliticaprivacidadeView },
  { path: '/calendario', component: CalendarioView },
  { path: '/socio', component: SocioView },
  { path: '/plantel', component: PlantelView },
  { path: '/pagamento', component: PagamentoView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router