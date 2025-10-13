#!/usr/bin/env python3
"""
Script para analisar os dados do INEP e identificar informações relevantes para Sistema de Análise Educacional - ES
"""

import pandas as pd
import numpy as np

def analyze_inep_data():
    """Analisa os dados do INEP para identificar informações relevantes para Sistema de Análise Educacional - ES"""
    
    print("🔍 Analisando dados do INEP...")
    
    # Carregar dados
    print("📁 Carregando microdados_ed_basica_2024.csv...")
    df = pd.read_csv('data/dados/microdados_ed_basica_2024.csv', 
                     sep=';', 
                     encoding='latin-1', 
                     nrows=10000)  # Primeiras 10k linhas para análise
    
    print(f"✅ Dados carregados: {df.shape[0]} registros, {df.shape[1]} colunas")
    
    # Verificar estados disponíveis
    print("\n🗺️ Estados disponíveis:")
    estados = df['SG_UF'].value_counts().head(10)
    print(estados)
    
    # Verificar se há dados do ES
    print(f"\n📍 Dados do Espírito Santo (CO_UF = 32):")
    es_data = df[df['CO_UF'] == 32]
    print(f"Registros do ES encontrados: {len(es_data)}")
    
    if len(es_data) > 0:
        print("✅ Dados do ES encontrados!")
        print(f"Municípios do ES: {es_data['NO_MUNICIPIO'].nunique()}")
        print(f"Primeiros municípios: {es_data['NO_MUNICIPIO'].unique()[:5].tolist()}")
    else:
        print("❌ Nenhum dado do ES encontrado nas primeiras 10k linhas")
        print("🔍 Verificando se ES está em outras partes do arquivo...")
        
        # Verificar códigos de UF
        print(f"\nCódigos de UF únicos: {sorted(df['CO_UF'].unique())}")
        
        # Verificar se 32 está na lista
        if 32 in df['CO_UF'].unique():
            print("✅ Código 32 (ES) encontrado no arquivo!")
        else:
            print("❌ Código 32 (ES) não encontrado")
    
    # Identificar colunas relevantes para professores
    print("\n👨‍🏫 Colunas relevantes para professores:")
    prof_cols = [col for col in df.columns if any(keyword in col.upper() for keyword in ['DOC', 'PROF', 'FORMACAO', 'ESCOLARIDADE'])]
    print(f"Total de colunas relacionadas a professores: {len(prof_cols)}")
    print("Primeiras 10 colunas:")
    for col in prof_cols[:10]:
        print(f"  - {col}")
    
    # Verificar colunas de dependência e localização
    print("\n🏫 Informações sobre escolas:")
    print(f"Dependências: {df['TP_DEPENDENCIA'].value_counts().to_dict()}")
    print(f"Localizações: {df['TP_LOCALIZACAO'].value_counts().to_dict()}")
    
    # Verificar se há dados de professores
    doc_cols = [col for col in df.columns if col.startswith('QT_DOC')]
    print(f"\n📊 Colunas de quantidade de docentes: {doc_cols}")
    
    if doc_cols:
        print("Amostra de dados de docentes:")
        sample_data = df[['NO_UF', 'NO_MUNICIPIO'] + doc_cols[:5]].head()
        print(sample_data)
    
    return df, es_data

def analyze_technical_courses():
    """Analisa os dados de cursos técnicos"""
    
    print("\n🔧 Analisando suplemento_cursos_tecnicos_2024.csv...")
    
    try:
        df_tec = pd.read_csv('data/dados/suplemento_cursos_tecnicos_2024.csv', 
                            sep=';', 
                            encoding='latin-1')
        
        print(f"✅ Dados de cursos técnicos carregados: {df_tec.shape[0]} registros")
        
        # Verificar dados do ES
        es_tec = df_tec[df_tec['CO_UF'] == 32]
        print(f"Registros do ES: {len(es_tec)}")
        
        if len(es_tec) > 0:
            print("✅ Dados de cursos técnicos do ES encontrados!")
            print(f"Municípios: {es_tec['NO_MUNICIPIO'].nunique()}")
            print(f"Cursos únicos: {es_tec['NO_CURSO_EDUC_PROFISSIONAL'].nunique()}")
            
            # Mostrar alguns cursos
            print("\nCursos técnicos no ES:")
            cursos_es = es_tec['NO_CURSO_EDUC_PROFISSIONAL'].value_counts().head(10)
            print(cursos_es)
        
        return df_tec, es_tec
        
    except Exception as e:
        print(f"❌ Erro ao carregar cursos técnicos: {e}")
        return None, None

if __name__ == "__main__":
    print("🚀 Iniciando análise dos dados do INEP para Sistema de Análise Educacional - ES")
    print("=" * 60)
    
    # Analisar dados principais
    df_main, es_main = analyze_inep_data()
    
    # Analisar cursos técnicos
    df_tec, es_tec = analyze_technical_courses()
    
    print("\n" + "=" * 60)
    print("✅ Análise concluída!")
    
    # Resumo
    print(f"\n📋 Resumo:")
    print(f"- Dados principais: {df_main.shape[0]} registros")
    print(f"- Dados do ES (principal): {len(es_main)} registros")
    print(f"- Dados do ES (técnicos): {len(es_tec) if es_tec is not None else 0} registros")
