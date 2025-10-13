# 📚 App Streamlit - Sistema de Análise Educacional - ES

## 👨‍💻 Desenvolvedor
**Gustavo Pereira** - Projeto Acadêmico de Análise de Dados Educacionais

## 🎯 Tema do Projeto
**Sistema de Análise Educacional do Espírito Santo** - Análise e visualização de dados educacionais do Espírito Santo com dados oficiais do INEP/Censo Escolar 2024.

## 🏗️ Arquitetura do Projeto

### 📁 Estrutura de Diretórios
```
app_streamlit/
├── main.py                          # Ponto de entrada da aplicação
├── requirements.txt                 # Dependências do projeto
├── .streamlit/                      # Configurações do Streamlit
│   └── config.toml
├── src/                            # Código fonte principal
│   ├── components/                 # Componentes reutilizáveis
│   │   ├── header.py              # Cabeçalho da aplicação
│   │   └── sidebar.py             # Menu de navegação lateral
│   ├── pages/                     # Páginas da aplicação
│   │   ├── dashboard.py           # Dashboard principal
│   │   ├── formacao.py            # Análise de formação de professores
│   │   ├── estatisticas.py        # Estatísticas por região
│   │   ├── evolucao.py            # Evolução temporal
│   │   ├── comparativos.py        # Análises comparativas
│   │   └── bases_dados.py         # Informações sobre bases de dados
│   ├── services/                  # Serviços de negócio
│   │   ├── data_service.py        # Serviço de dados
│   │   └── analytics_service.py   # Serviço de análises
│   └── utils/                     # Utilitários e helpers
│       ├── data_helpers.py        # Funções auxiliares para dados
│       ├── chart_helpers.py       # Funções auxiliares para gráficos
│       └── validation.py          # Validação de dados
├── data/                          # Dados e arquivos de exemplo
│   └── sample_data.json           # Dados simulados para demonstração
└── docs/                          # Documentação adicional
    └── DEPLOY_INSTRUCTIONS.md     # Instruções de deploy
```

### 📱 Seções do App

#### 🏠 **Dashboard Principal**
- Visão geral dos indicadores principais
- Métricas em tempo real
- Gráficos de evolução temporal
- Indicadores de qualidade

#### 🎓 **Formação de Professores**
- Análise detalhada dos programas de formação
- Filtros por modalidade, área e período
- Estatísticas de participação
- Indicadores de satisfação e empregabilidade

#### 📍 **Estatísticas por Região**
- Análise geográfica dos dados
- Comparações entre municípios e regiões
- Mapas interativos (futuro)
- Correlações regionais

#### 📈 **Evolução Temporal**
- Séries temporais de indicadores
- Análise de tendências e sazonalidade
- Projeções futuras
- Comparações interanuais

#### 🔄 **Comparativos**
- Comparações entre períodos
- Análises entre regiões
- Benchmarking de indicadores
- Análises de correlação

#### 📚 **Bases de Dados**
- **INEP (Instituto Nacional de Estudos e Pesquisas Educacionais)**
  - Censo Escolar: Dados sobre escolas, professores e infraestrutura
  - Educacenso: Informações detalhadas sobre matrículas e docentes
  - Sinopse Estatística: Resumos consolidados e séries históricas
- **SEDU (Secretaria de Estado da Educação)**
  - Relatórios públicos de gestão
  - Dados sobre programas educacionais
  - Indicadores de desempenho e qualidade
- **Dados Simulados**
  - Dados para desenvolvimento e testes
  - Estrutura representativa dos dados reais
  - Conformidade com LGPD (apenas dados agregados)

## 🗄️ Bases de Dados Planejadas

### 📊 **Fontes Principais**
1. **INEP - Censo Escolar**
   - Frequência: Anual
   - Conteúdo: Estatísticas educacionais, perfil dos professores, infraestrutura escolar
   - Acesso: Público via portal de dados abertos

2. **INEP - Educacenso**
   - Frequência: Anual
   - Conteúdo: Dados detalhados sobre matrículas, docentes e gestores
   - Acesso: Público via APIs e downloads

3. **SEDU - Relatórios Institucionais**
   - Frequência: Trimestral/Anual
   - Conteúdo: Programas de formação, resultados, indicadores de qualidade
   - Acesso: Relatórios públicos de prestação de contas

4. **Dados Simulados para Desenvolvimento**
   - Frequência: Em tempo real
   - Conteúdo: Estrutura representativa dos dados reais
   - Propósito: Testes, validação e demonstração

### 🔒 **Conformidade e Segurança**
- **LGPD**: Apenas dados agregados e públicos
- **Anonimização**: Nenhuma informação individual
- **Transparência**: Fonte dos dados sempre documentada
- **Controle de Acesso**: Dados sensíveis não são expostos

## 🚀 Como Executar

### 📋 Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### ⚙️ Instalação
```bash
# Clone o repositório
git clone https://github.com/gustavosillva0256/app_streamlit.git
cd app_streamlit

# Instale as dependências
pip install -r requirements.txt
```

### ▶️ Execução
```bash
# Execute a aplicação
streamlit run main.py
```

A aplicação estará disponível em: `http://localhost:8501`

## 🌐 Deploy

### 📱 Streamlit Cloud
1. Conecte seu repositório GitHub ao Streamlit Cloud
2. Configure as variáveis de ambiente necessárias
3. Deploy automático a cada push para a branch main

### 📋 Instruções Detalhadas
Consulte o arquivo `DEPLOY_INSTRUCTIONS.md` para instruções completas de deploy.

## 🎯 Funcionalidades

### ✅ **Implementadas**
- ✅ Estrutura modular e escalável
- ✅ Dashboard principal com métricas
- ✅ Navegação entre seções
- ✅ Componentes reutilizáveis
- ✅ Dados simulados para demonstração
- ✅ Gráficos interativos com Plotly
- ✅ Validação de dados
- ✅ Documentação completa

### 🔄 **Em Desenvolvimento**
- 🔄 Integração com APIs oficiais
- 🔄 Pipeline de dados automatizado
- 🔄 Validação de qualidade em tempo real
- 🔄 Cache inteligente de dados

### 🚀 **Futuras Expansões**
- 🚀 Dashboard preditivo com ML
- 🚀 Indicadores de impacto educacional
- 🚀 Mapas interativos por região
- 🚀 Relatórios automatizados
- 🚀 API para integração externa

## 🛠️ Tecnologias Utilizadas

- **Frontend**: Streamlit (Python)
- **Visualização**: Plotly, Matplotlib
- **Manipulação de Dados**: Pandas, NumPy
- **Validação**: Pydantic (futuro)
- **Cache**: Streamlit Cache
- **Deploy**: Streamlit Cloud

## 📈 Roadmap

### 🎯 **Fase 1 (Atual)**
- ✅ Estrutura base da aplicação
- ✅ Componentes principais
- ✅ Dados simulados
- ✅ Deploy inicial

### 🎯 **Fase 2 (Próxima)**
- 🔄 Integração com dados reais do INEP
- 🔄 Pipeline de dados automatizado
- 🔄 Validação de qualidade
- 🔄 Cache inteligente

### 🎯 **Fase 3 (Futura)**
- 🚀 Dashboard preditivo
- 🚀 Machine Learning para projeções
- 🚀 APIs para integração externa
- 🚀 Relatórios automatizados

## 🤝 Contribuição

Este é um projeto acadêmico desenvolvido por Gustavo Pereira. Para contribuições ou dúvidas, entre em contato através do repositório GitHub.

## 📄 Licença

Projeto acadêmico - Uso educacional e de pesquisa.

---

**Desenvolvido com ❤️ para análise da educação brasileira**
