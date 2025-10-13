#!/usr/bin/env python3
"""
Script para carregar especificamente os dados do Espírito Santo
"""

import pandas as pd
import numpy as np

def load_es_data():
    """Carrega dados do Espírito Santo do arquivo do INEP"""
    
    print("🔍 Carregando dados do Espírito Santo...")
    
    # Carregar dados completos
    print("📁 Carregando microdados_ed_basica_2024.csv...")
    df = pd.read_csv('data/dados/microdados_ed_basica_2024.csv', 
                     sep=';', 
                     encoding='latin-1', 
                     low_memory=False)
    
    print(f"✅ Dados carregados: {df.shape[0]} registros, {df.shape[1]} colunas")
    
    # Filtrar dados do ES
    print("📍 Filtrando dados do Espírito Santo (CO_UF = 32)...")
    es_data = df[df['CO_UF'] == 32]
    
    print(f"✅ Dados do ES encontrados: {len(es_data)} registros")
    
    if len(es_data) > 0:
        print(f"🏙️ Municípios: {es_data['NO_MUNICIPIO'].nunique()}")
        print(f"🏫 Escolas: {es_data['CO_ENTIDADE'].nunique()}")
        
        # Mostrar alguns municípios
        print("\nPrimeiros municípios do ES:")
        municipios = es_data['NO_MUNICIPIO'].unique()[:10]
        for i, mun in enumerate(municipios, 1):
            print(f"  {i}. {mun}")
        
        # Análise de professores
        print("\n👨‍🏫 Análise de professores:")
        prof_cols = [col for col in es_data.columns if col.startswith('QT_DOC')]
        print(f"Colunas de professores: {prof_cols}")
        
        # Estatísticas de professores
        if 'QT_DOC_BAS' in es_data.columns:
            total_prof = es_data['QT_DOC_BAS'].sum()
            print(f"Total de professores (básica): {total_prof:,.0f}")
        
        if 'QT_DOC_FUND' in es_data.columns:
            total_fund = es_data['QT_DOC_FUND'].sum()
            print(f"Total de professores (fundamental): {total_fund:,.0f}")
        
        if 'QT_DOC_MED' in es_data.columns:
            total_med = es_data['QT_DOC_MED'].sum()
            print(f"Total de professores (médio): {total_med:,.0f}")
        
        # Análise por dependência
        print("\n🏫 Análise por dependência:")
        dep_analysis = es_data['TP_DEPENDENCIA'].value_counts()
        dep_names = {1: 'Federal', 2: 'Estadual', 3: 'Municipal', 4: 'Privada'}
        for dep_code, count in dep_analysis.items():
            dep_name = dep_names.get(dep_code, f'Código {dep_code}')
            print(f"  {dep_name}: {count} escolas")
        
        # Análise por localização
        print("\n🌍 Análise por localização:")
        loc_analysis = es_data['TP_LOCALIZACAO'].value_counts()
        loc_names = {1: 'Urbana', 2: 'Rural'}
        for loc_code, count in loc_analysis.items():
            loc_name = loc_names.get(loc_code, f'Código {loc_code}')
            print(f"  {loc_name}: {count} escolas")
        
        # Salvar dados do ES
        print("\n💾 Salvando dados do ES...")
        es_data.to_csv('data/dados/escolas_es_2024.csv', index=False, encoding='utf-8')
        print("✅ Dados do ES salvos em 'data/dados/escolas_es_2024.csv'")
        
        return es_data
    else:
        print("❌ Nenhum dado do ES encontrado!")
        return None

def load_es_technical_courses():
    """Carrega dados de cursos técnicos do ES"""
    
    print("\n🔧 Carregando cursos técnicos do ES...")
    
    try:
        df_tec = pd.read_csv('data/dados/suplemento_cursos_tecnicos_2024.csv', 
                            sep=';', 
                            encoding='latin-1')
        
        # Filtrar ES
        es_tec = df_tec[df_tec['CO_UF'] == 32]
        
        print(f"✅ Cursos técnicos do ES: {len(es_tec)} registros")
        
        if len(es_tec) > 0:
            print(f"🏙️ Municípios com cursos técnicos: {es_tec['NO_MUNICIPIO'].nunique()}")
            print(f"📚 Cursos únicos: {es_tec['NO_CURSO_EDUC_PROFISSIONAL'].nunique()}")
            
            # Análise de cursos
            print("\n📚 Principais cursos técnicos no ES:")
            cursos = es_tec['NO_CURSO_EDUC_PROFISSIONAL'].value_counts().head(10)
            for curso, count in cursos.items():
                print(f"  - {curso}: {count} ofertas")
            
            # Salvar dados
            es_tec.to_csv('data/dados/cursos_tecnicos_es_2024.csv', index=False, encoding='utf-8')
            print("✅ Cursos técnicos do ES salvos em 'data/dados/cursos_tecnicos_es_2024.csv'")
            
            return es_tec
        else:
            print("❌ Nenhum curso técnico do ES encontrado!")
            return None
            
    except Exception as e:
        print(f"❌ Erro ao carregar cursos técnicos: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Carregando dados do Espírito Santo para Sistema de Análise Educacional")
    print("=" * 60)
    
    # Carregar dados principais do ES
    es_escolas = load_es_data()
    
    # Carregar cursos técnicos do ES
    es_cursos = load_es_technical_courses()
    
    print("\n" + "=" * 60)
    print("✅ Carregamento concluído!")
    
    if es_escolas is not None:
        print(f"📊 Dados do ES carregados: {len(es_escolas)} escolas")
    if es_cursos is not None:
        print(f"🔧 Cursos técnicos do ES: {len(es_cursos)} ofertas")
