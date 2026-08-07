[README.md](https://github.com/user-attachments/files/30806725/README.md)
# Calculadora de Faturamento Médico

Uma aplicação web **Full Stack** desenvolvida para automatizar e otimizar o cálculo de precificação de procedimentos médicos com base em parâmetros de convênios (Unimed, Amil, etc.), valores de UCO, filme, portes e adicionais regulamentares.

---

## 🛠️ Tecnologias Utilizadas

### **Frontend**
* **Framework:** [Vue.js 3](https://vuejs.org/) (Composition API com `<script setup>`)
* **Requisições HTTP:** [Axios](https://axios-http.com/)
* **Estilização:** CSS3 puro e responsivo
* **Hospedagem / Deploy:** [Vercel](https://vercel.com/)

### **Backend**
* **Linguagem:** Python
* **Framework Web:** [Django](https://www.djangoproject.com/) / [Django REST Framework](https://www.django-rest-framework.org/)
* **Mapeamento de Rotas & CORS:** `django-cors-headers`
* **Hospedagem / Deploy:** [Render](https://render.com/)

---

## 💡 Regra de Negócio & Lógica de Cálculo

A aplicação realiza a soma e ponderação dos custos operacionais de um procedimento médico através da seguinte fórmula base:

$$\text{Valor Final} = \text{Valor Procedimento} + \text{Porte} + (\text{Valor UCO} \times \text{UCO Procedimento}) + (\text{Valor Filme} \times \text{Filme Procedimento})$$

### **Acréscimos Regras de Negócio:**
1. **Aditivo Percentual (%):** Recai sobre o subtotal acumulado.
2. **Acomodação (Apartamento):** Aplica acréscimo percentual adicional de internação.
3. **Horário Especial:** Aplica taxa adicional sobre procedimentos efetuados fora do horário comercial regular.

---

## 🚀 Como Executar o Projeto Localmente

### **Pré-requisitos**
* Node.js (v18+)
* Python (v3.10+)
* Git

---

### **1. Configurando e Rodando o Backend (Django)**

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/calculadora-faturamento-medico.git
cd calculadora-faturamento-medico/backend

# Crie e ative um ambiente virtual
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações do banco de dados
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

O servidor backend estará disponível na porta que ira aparecer no terminal

---

### **2. Configurando e Rodando o Frontend (Vue.js)**

```bash
# Navegue até a pasta do frontend
cd ../frontend

# Instale as dependências do Node
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

O aplicativo frontend estará disponível em `http://localhost:5173/`.

---

## 🔗 Endpoints da API

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/calcular/` | Recebe os dados do procedimento e convênio em formato JSON e retorna o `valor_final` calculado. |

### **Exemplo de Payload (POST `/api/calcular/`):**

```json
{
  "convenio": "Unimed",
  "valor_uco_convenio": 11.50,
  "valor_filme_convenio": 22.00,
  "valor_procedimento": 1500.00,
  "porte": 250.00,
  "uco_procedimento": 10,
  "filme_procedimento": 2,
  "aditivo": 10,
  "acomodacao": "S",
  "horario_especial": "N"
}
```

### **Exemplo de Resposta:**

```json
{
  "valor_final": 2518.20
}
```

---

## 👨‍💻 Autor

Desenvolvido por **Alex Lima**.  
Se você tiver dúvidas, sugestões ou quiser se conectar, entre em contato via LinkedIn ou GitHub!
