<template>
  <div class="container">
    <div class="card">
      <h1 class="title">Calculadora de Procedimentos</h1>
      <p class="subtitle">Preencha os dados abaixo para calcular o valor do procedimento</p>
      <p class="subtitle">a logíca aplicada nesse calcúlo é a seguinte:</p>
      <p class="subtitle">vlr.procedimento + porte + vlr.uco + vlr.filme + Horário Especial + Acomodação</p>

      <div class="form-group">
        <label>Nome do Convênio</label>
        <input type="text" v-model="formulario.convenio" placeholder="Ex: Unimed, Amil...">
      </div>

      <div class="row">
        <div class="form-group">
          <label>Valor UCO (R$)</label>
          <input type="number" step="0.01" v-model="formulario.valor_uco_convenio">
        </div>
        <div class="form-group">
          <label>Valor Filme (R$)</label>
          <input type="number" step="0.01" v-model="formulario.valor_filme_convenio">
        </div>
      </div>

      <div class="divider">Dados do Procedimento</div>

      <div class="row">
        <div class="form-group">
          <label>Valor Procedimento</label>
          <input type="number" v-model="formulario.valor_procedimento">
        </div>
        <div class="form-group">
          <label>Porte</label>
          <input type="number" v-model="formulario.porte">
        </div>
      </div>

      <div class="row">
        <div class="form-group">
          <label>UCO do Procedimento</label>
          <input type="number" v-model="formulario.uco_procedimento">
        </div>
        <div class="form-group">
          <label>Filme do Procedimento</label>
          <input type="number" v-model="formulario.filme_procedimento">
        </div>
      </div>

      <div class="form-group">
        <label>Aditivo (%)</label>
        <input type="number" v-model="formulario.aditivo">
      </div>

      <div class="checkbox-group">
        <label class="checkbox-container">
          <input type="checkbox" v-model="formulario.acomodacao" true-value="S" false-value="N">
          <span class="checkmark"></span> Acomodação Apartamento?
        </label>
        <label class="checkbox-container">
          <input type="checkbox" v-model="formulario.horario_especial" true-value="S" false-value="N">
          <span class="checkmark"></span> Horário Especial?
        </label>
      </div>

      <button @click="enviarCalculo" class="btn-calculate">Calcular Valor Final</button>

      <div v-if="resultado !== null" class="result-box">
        <span>Resultado Final</span>
        <h3>R$ {{ resultado }}</h3>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const formulario = ref({
  convenio: '',
  valor_uco_convenio: 0,
  valor_filme_convenio: 0,
  valor_procedimento: 0,
  porte: 0,
  uco_procedimento: 0,
  filme_procedimento: 0,
  aditivo: 0,
  acomodacao: 'N',
  horario_especial: 'N'
})

const resultado = ref(null)

const enviarCalculo = async () => {
  try {
    const response = await axios.post('https://calculadora-faturamento-medico.onrender.com/api/calcular/', formulario.value)
    resultado.value = response.data.valor_final
  } catch (error) {
    alert("Erro ao realizar o cálculo. Verifique os dados inseridos.")
  }
}
</script>

<style scoped>
/* Estilo Base */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f0f7ff; /* Azul claríssimo */
  padding: 20px;
}

.card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  width: 100%;
  max-width: 500px;
}

.title {
  color: #0056b3; /* Azul padrão */
  margin-bottom: 5px;
  text-align: center;
}

.subtitle {
  color: #666;
  font-size: 14px;
  text-align: center;
  margin-bottom: 25px;
}

.divider {
  margin: 20px 0 15px;
  font-weight: bold;
  color: #0056b3;
  border-bottom: 2px solid #e1f0ff;
  padding-bottom: 5px;
}

/* Formulário */
.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

label {
  font-size: 13px;
  color: #333;
  margin-bottom: 5px;
  font-weight: 500;
}

input {
  padding: 10px;
  border: 1px solid #d1e3f8;
  border-radius: 6px;
  background-color: #85baf0;
}

input:focus {
  outline: none;
  border-color: #0056b3;
  box-shadow: 0 0 0 3px rgba(0, 86, 179, 0.1);
}

/* Botão */
.btn-calculate {
  width: 100%;
  padding: 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
  transition: background 0.3s;
}

.btn-calculate:hover {
  background-color: #0056b3;
}

/* Checkbox */
.checkbox-group {
  margin: 15px 0;
}

.checkbox-container {
  display: block;
  margin-bottom: 10px;
  cursor: pointer;
}

/* Resultado */
.result-box {
  margin-top: 25px;
  padding: 15px;
  background-color: #eef6ff;
  border-left: 5px solid #007bff;
  border-radius: 4px;
  text-align: center;
}

.result-box span {
  font-size: 12px;
  color: #0056b3;
  text-transform: uppercase;
  font-weight: bold;
}

.result-box h3 {
  margin: 5px 0 0;
  font-size: 24px;
  color: #333;
}
</style>