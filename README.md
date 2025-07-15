# 🗳️ Visualizador de Cotas Parlamentares – Ruckz

Projeto em Flask + Docker que permite visualizar, ordenar e baixar relatórios em PDF com os **gastos parlamentares por deputado federal (dados da Câmara dos Deputados)**.

🔗 Deploy online: [agendamentobeta-cotas-ruckz.tnrxuj.easypanel.host](https://agendamentobeta-cotas-ruckz.tnrxuj.easypanel.host/)

---

## 🚀 Funcionalidades

- ✅ Busca automática e diária dos dados oficiais (Câmara dos Deputados)
- ✅ Exibição em tabela ordenada por maior gasto
- ✅ Geração de PDF com os dados atuais
- ✅ Interface responsiva (mobile friendly)
- ✅ Deploy pronto com Docker e EasyPanel

---

## 📦 Tecnologias usadas

- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [FPDF](https://pyfpdf.github.io/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Gunicorn](https://gunicorn.org/)
- [Docker](https://www.docker.com/)
- Hospedado com [EasyPanel](https://easypanel.io/)

---

## ⚙️ Como rodar localmente

```bash
# Clone o projeto
git clone https://github.com/RuckzAuto/cotas-parlamentares.git
cd cotas-parlamentares

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
