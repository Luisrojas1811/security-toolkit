# 02 — Hash Generator

## ¿Qué hace?
Genera hashes de textos usando MD5, SHA-1 y SHA-256, y permite comparar
dos textos para verificar si fueron modificados.

## Concepto de seguridad
El hashing es la base de la **integridad de datos** — el segundo pilar de la tríada CIA.
Un hash es una función de una sola vía: dado un texto siempre produce el mismo resultado,
pero es imposible revertirlo para obtener el texto original.

### ¿Por qué MD5 y SHA-1 están rotos?
- **MD5** (1991): Se pueden generar dos textos distintos con el mismo hash (colisión).
- **SHA-1** (1995): Google demostró una colisión real en 2017.
- **SHA-256** (2001): Estándar actual. Lo usan Bitcoin, SSL/TLS y firmas digitales.

## Casos de uso reales
- Verificar que un archivo descargado no fue alterado
- Guardar contraseñas en bases de datos (nunca en texto plano)
- Forense digital: probar que una evidencia no fue modificada

## Cómo correrlo
```bash
python3 hash_generator.py
```

## Ejemplo de salida
```
MD5    (inseguro): 4d186321c1a7f0f354b297e8914ab240
SHA-1  (inseguro): 99800b85d3383e3a2fb45eb7d0066a4879b9b175
SHA-256 (seguro) : 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```