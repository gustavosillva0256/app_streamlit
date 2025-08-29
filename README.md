# 📚 App Streamlit - Fluxo de Formação de Professores (CEFOPE)

## 👨‍💻 Desenvolvedor
**Gustavo Pereira**

## 🎯 Tema do Projeto
Análise e visualização do fluxo de formação de professores através do CEFOPE (Centro de Formação de Professores).

## 🏗️ Arquitetura do Projeto

### Estrutura de Diretórios
```
app_streamlit/
├── src/
│   ├── pages/          # Páginas do aplicativo
│   ├── components/      # Componentes reutilizáveis
│   ├── services/        # Lógica de negócio e serviços
│   └── utils/          # Utilitários e helpers
├── data/               # Dados e datasets
├── requirements.txt    # Dependências do projeto
└── main.py            # Arquivo principal
```

### Seções do App (Expansão Futura)
1. **Dashboard Principal** - Visão geral dos indicadores
2. **Formação de Professores** - Análise do fluxo educacional
3. **Estatísticas por Região** - Dados geográficos
4. **Evolução Temporal** - Análise de tendências
5. **Comparativos** - Análises comparativas entre períodos/regiões

### Bases de Dados Planejadas
- Dados do CEFOPE (formação inicial e continuada)
- Censo Escolar
- Dados demográficos por região
- Indicadores educacionais
- Metas e resultados de formação

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/gustavosillva0256/app_streamlit.git
cd app_streamlit
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o aplicativo
```bash
streamlit run main.py
```

## 🌐 Deploy
O aplicativo está configurado para deploy no Streamlit Cloud.

## 📊 Funcionalidades
- Dashboard interativo
- Visualizações de dados educacionais
- Análise do fluxo de formação de professores
- Interface responsiva e intuitiva

## 🔧 Tecnologias Utilizadas
- **Streamlit** - Framework web para aplicações de dados
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas
- **Python** - Linguagem principal

## 📈 Roadmap
- [x] Estrutura base do projeto
- [x] Dashboard principal
- [ ] Integração com bases de dados reais
- [ ] Gráficos avançados e análises
- [ ] Sistema de filtros e busca
- [ ] Relatórios exportáveis
