# 🍨 Scoop Bucket de Rowell (@Row0902)

[![CI](https://github.com/Row0902/scoop-bucket/actions/workflows/ci.yml/badge.svg)](https://github.com/Row0902/scoop-bucket/actions/workflows/ci.yml)
[![Excavator](https://github.com/Row0902/scoop-bucket/actions/workflows/excavator.yml/badge.svg)](https://github.com/Row0902/scoop-bucket/actions/workflows/excavator.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Repositorio personalizado de manifiestos para **[Scoop](https://scoop.sh)**, el instalador de paquetes por línea de comandos para Windows.

Aquí se distribuyen herramientas de desarrollo, utilidades de audio, editores y aplicaciones de escritorio empaquetadas para su instalación rápida y limpia sin instaladores gráficos intrusivos ni permisos de administrador.

---

## 🚀 Instalación y Uso

### 1. Prerrequisito: Instalar Scoop
Si aún no tienes Scoop instalado en Windows, abre **PowerShell** y corre:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

### 2. Agregar este Bucket
Añade este repositorio a tu lista de buckets de Scoop con el alias `row`:

```powershell
scoop bucket add row https://github.com/Row0902/scoop-bucket
```

### 3. Instalar Aplicaciones
Instala cualquiera de los paquetes disponibles:

```powershell
# Motor de versiones y releases SemVer
scoop install cutver

# Bloc de notas accesible en Rust con síntesis de voz
scoop install sonarpad

# Separación de fuentes de audio por IA (versión CPU)
scoop install music-separator-cpu
```

### 4. Actualizar Paquetes
Para mantener todas tus aplicaciones al día:

```powershell
# Actualiza los índices de los buckets
scoop update

# Actualiza una aplicación específica
scoop update cutver

# O actualiza todas tus aplicaciones instaladas
scoop update *
```

---

## 📦 Aplicaciones Disponibles

<!-- apps-table:start -->
| Nombre | Versión base | Última versión | Sitio oficial |
|---|---|---|---|
| cutver | 0.8.0 | 0.8.0 | https://github.com/cutver/cutver |
| music-separator-cpu | 1.6 | 1.6 | https://github.com/GianlucaApollaro/Music-Separator-GUI |
| music-separator-gpu | 1.6 | 1.6 | https://github.com/GianlucaApollaro/Music-Separator-GUI |
| sonarpad | 0.8.4 | 0.8.4 | https://github.com/Ambro86/Sonarpad |
| vetube | 3.94 | 3.94 | https://github.com/metalalchemist/VeTube |
<!-- apps-table:end -->

---

## 🤖 Mantenimiento Automático (Excavator)

* Este bucket cuenta con integración continua (**CI**) que valida la sintaxis y los esquemas de cada manifiesto con Pester y PowerShell.
* Los paquetes se actualizan automáticamente de forma desatendida mediante **Excavator**, que consulta los repositorios oficiales cada 4 horas y sincroniza las nuevas versiones y checksums SHA-256.

---

## 🐛 Reporte de Errores

Si encuentras algún hash desactualizado, un enlace roto o deseas solicitar la inclusión de una nueva aplicación, por favor abre un [Issue en GitHub](https://github.com/Row0902/scoop-bucket/issues).

---

## 📄 Licencia

Este repositorio se distribuye bajo la licencia [MIT](LICENSE). Cada aplicación instalada mantiene su propia licencia según se indica en su respectivo manifiesto.
