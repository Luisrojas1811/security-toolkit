# 01 — Password Strength Checker

## ¿Qué hace?
Analiza una contraseña y devuelve un score del 0 al 100 con sugerencias de mejora.

## Concepto de seguridad
Las contraseñas débiles son la causa #1 de brechas de seguridad. Este módulo
aplica las reglas del **NIST SP 800-63B**, el estándar moderno para contraseñas seguras:
- Longitud mínima de 8 caracteres (idealmente 16+)
- Combinación de mayúsculas, números y caracteres especiales
- Mayor longitud = mayor entropía = más difícil de crackear por fuerza bruta

## Cómo correrlo
```bash
python password_checker.py
```

## Ejemplo de salida
```
Score: 80/100
Nivel: ✅ FUERTE
Sugerencias:
  ✅ Longitud excelente
```