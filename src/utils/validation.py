"""
Utilitários para validação de dados e entrada do usuário
"""

from typing import Any, Dict, List, Optional, Union
import pandas as pd
import numpy as np

def validate_numeric_input(value: Any, min_value: Optional[float] = None, 
                          max_value: Optional[float] = None) -> bool:
    """
    Valida se um valor é numérico e está dentro dos limites especificados
    
    Args:
        value: Valor a ser validado
        min_value: Valor mínimo permitido
        max_value: Valor máximo permitido
        
    Returns:
        True se válido, False caso contrário
    """
    try:
        num_value = float(value)
        
        if min_value is not None and num_value < min_value:
            return False
        
        if max_value is not None and num_value > max_value:
            return False
        
        return True
    except (ValueError, TypeError):
        return False

def validate_date_input(date_str: str, format: str = "%Y-%m-%d") -> bool:
    """
    Valida se uma string representa uma data válida
    
    Args:
        date_str: String com a data
        format: Formato esperado da data
        
    Returns:
        True se válido, False caso contrário
    """
    try:
        pd.to_datetime(date_str, format=format)
        return True
    except (ValueError, TypeError):
        return False

def validate_dataframe_columns(df: pd.DataFrame, 
                              required_columns: List[str],
                              optional_columns: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Valida se um DataFrame possui as colunas necessárias
    
    Args:
        df: DataFrame a ser validado
        required_columns: Lista de colunas obrigatórias
        optional_columns: Lista de colunas opcionais
        
    Returns:
        Dicionário com resultado da validação
    """
    result = {
        "is_valid": True,
        "missing_required": [],
        "missing_optional": [],
        "extra_columns": [],
        "errors": []
    }
    
    # Verificar colunas obrigatórias
    df_columns = set(df.columns)
    required_set = set(required_columns)
    
    missing_required = required_set - df_columns
    if missing_required:
        result["is_valid"] = False
        result["missing_required"] = list(missing_required)
        result["errors"].append(f"Colunas obrigatórias ausentes: {list(missing_required)}")
    
    # Verificar colunas opcionais
    if optional_columns:
        optional_set = set(optional_columns)
        missing_optional = optional_set - df_columns
        result["missing_optional"] = list(missing_optional)
    
    # Verificar colunas extras
    all_expected = required_set.union(set(optional_columns) if optional_columns else set())
    extra_columns = df_columns - all_expected
    if extra_columns:
        result["extra_columns"] = list(extra_columns)
    
    return result

def validate_data_types(df: pd.DataFrame, 
                       expected_types: Dict[str, Union[str, type]]) -> Dict[str, Any]:
    """
    Valida se as colunas do DataFrame possuem os tipos esperados
    
    Args:
        df: DataFrame a ser validado
        expected_types: Dicionário com nome da coluna e tipo esperado
        
    Returns:
        Dicionário com resultado da validação
    """
    result = {
        "is_valid": True,
        "type_mismatches": [],
        "errors": []
    }
    
    for column, expected_type in expected_types.items():
        if column not in df.columns:
            continue
        
        actual_type = str(df[column].dtype)
        
        # Mapeamento de tipos pandas para tipos Python
        type_mapping = {
            'int64': int,
            'int32': int,
            'float64': float,
            'float32': float,
            'object': str,
            'bool': bool,
            'datetime64[ns]': 'datetime',
            'category': 'category'
        }
        
        if expected_type in type_mapping:
            expected_type = type_mapping[expected_type]
        
        # Verificar se o tipo é compatível
        is_compatible = False
        
        if expected_type == int:
            is_compatible = pd.api.types.is_integer_dtype(df[column])
        elif expected_type == float:
            is_compatible = pd.api.types.is_float_dtype(df[column])
        elif expected_type == str:
            is_compatible = pd.api.types.is_object_dtype(df[column])
        elif expected_type == bool:
            is_compatible = pd.api.types.is_bool_dtype(df[column])
        elif expected_type == 'datetime':
            is_compatible = pd.api.types.is_datetime64_any_dtype(df[column])
        elif expected_type == 'category':
            is_compatible = pd.api.types.is_categorical_dtype(df[column])
        
        if not is_compatible:
            result["is_valid"] = False
            result["type_mismatches"].append({
                "column": column,
                "expected": str(expected_type),
                "actual": actual_type
            })
            result["errors"].append(
                f"Coluna '{column}': tipo esperado {expected_type}, tipo atual {actual_type}"
            )
    
    return result

def validate_data_range(df: pd.DataFrame, 
                       column_ranges: Dict[str, Dict[str, Union[float, int]]]) -> Dict[str, Any]:
    """
    Valida se os valores das colunas estão dentro dos intervalos especificados
    
    Args:
        df: DataFrame a ser validado
        column_ranges: Dicionário com nome da coluna e limites
        
    Returns:
        Dicionário com resultado da validação
    """
    result = {
        "is_valid": True,
        "range_violations": [],
        "errors": []
    }
    
    for column, ranges in column_ranges.items():
        if column not in df.columns:
            continue
        
        if 'min' in ranges:
            min_val = ranges['min']
            below_min = df[column] < min_val
            if below_min.any():
                result["is_valid"] = False
                result["range_violations"].append({
                    "column": column,
                    "limit": "min",
                    "value": min_val,
                    "count": below_min.sum()
                })
                result["errors"].append(
                    f"Coluna '{column}': {below_min.sum()} valores abaixo do mínimo {min_val}"
                )
        
        if 'max' in ranges:
            max_val = ranges['max']
            above_max = df[column] > max_val
            if above_max.any():
                result["is_valid"] = False
                result["range_violations"].append({
                    "column": column,
                    "limit": "max",
                    "value": max_val,
                    "count": above_max.sum()
                })
                result["errors"].append(
                    f"Coluna '{column}': {above_max.sum()} valores acima do máximo {max_val}"
                )
    
    return result

def validate_missing_values(df: pd.DataFrame, 
                           max_missing_percentage: float = 0.1) -> Dict[str, Any]:
    """
    Valida se há valores ausentes nas colunas
    
    Args:
        df: DataFrame a ser validado
        max_missing_percentage: Percentual máximo de valores ausentes permitido
        
    Returns:
        Dicionário com resultado da validação
    """
    result = {
        "is_valid": True,
        "columns_with_missing": [],
        "errors": []
    }
    
    for column in df.columns:
        missing_count = df[column].isna().sum()
        missing_percentage = missing_count / len(df)
        
        if missing_percentage > max_missing_percentage:
            result["is_valid"] = False
            result["columns_with_missing"].append({
                "column": column,
                "missing_count": missing_count,
                "missing_percentage": missing_percentage,
                "total_count": len(df)
            })
            result["errors"].append(
                f"Coluna '{column}': {missing_percentage:.1%} de valores ausentes "
                f"({missing_count}/{len(df)})"
            )
    
    return result

def validate_duplicates(df: pd.DataFrame, 
                       subset: Optional[List[str]] = None,
                       keep: str = 'first') -> Dict[str, Any]:
    """
    Valida se há linhas duplicadas no DataFrame
    
    Args:
        df: DataFrame a ser validado
        subset: Colunas para verificar duplicatas
        keep: Como tratar duplicatas ('first', 'last', False)
        
    Returns:
        Dicionário com resultado da validação
    """
    result = {
        "is_valid": True,
        "duplicate_count": 0,
        "duplicate_rows": None,
        "errors": []
    }
    
    duplicates = df.duplicated(subset=subset, keep=keep)
    duplicate_count = duplicates.sum()
    
    if duplicate_count > 0:
        result["is_valid"] = False
        result["duplicate_count"] = duplicate_count
        result["duplicate_rows"] = df[duplicates]
        result["errors"].append(
            f"Encontradas {duplicate_count} linhas duplicadas"
        )
    
    return result

def comprehensive_data_validation(df: pd.DataFrame,
                                required_columns: List[str],
                                expected_types: Dict[str, Union[str, type]],
                                column_ranges: Optional[Dict[str, Dict[str, Union[float, int]]]] = None,
                                max_missing_percentage: float = 0.1) -> Dict[str, Any]:
    """
    Executa validação completa dos dados
    
    Args:
        df: DataFrame a ser validado
        required_columns: Colunas obrigatórias
        expected_types: Tipos esperados para cada coluna
        column_ranges: Intervalos permitidos para valores
        max_missing_percentage: Percentual máximo de valores ausentes
        
    Returns:
        Dicionário com resultado completo da validação
    """
    results = {}
    
    # Validação de colunas
    results["columns"] = validate_dataframe_columns(df, required_columns)
    
    # Validação de tipos
    results["types"] = validate_data_types(df, expected_types)
    
    # Validação de intervalos
    if column_ranges:
        results["ranges"] = validate_data_range(df, column_ranges)
    
    # Validação de valores ausentes
    results["missing"] = validate_missing_values(df, max_missing_percentage)
    
    # Validação de duplicatas
    results["duplicates"] = validate_duplicates(df)
    
    # Resultado geral
    results["overall_valid"] = all(
        result.get("is_valid", True) 
        for result in results.values() 
        if isinstance(result, dict)
    )
    
    # Resumo de erros
    all_errors = []
    for result in results.values():
        if isinstance(result, dict) and "errors" in result:
            all_errors.extend(result["errors"])
    
    results["all_errors"] = all_errors
    results["error_count"] = len(all_errors)
    
    return results
