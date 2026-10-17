# Preparar el sistema para verificar vistas

Esta guía prepara Playwright CLI para recorridos puntuales del agente. La instalación se hace una vez; después, cada verificación reutiliza el entorno. Si la herramienta del agente exige su propio navegador y funciona, se utiliza ese navegador.

## Qué necesitas

Revisión de tu equipo el 17 de octubre de 2026:

| Componente | Tu sistema | Acción |
| --- | --- | --- |
| Node.js y npm | Node 24.12.0 y npm 11.6.2, mediante NVM | Ya disponibles |
| Navegador | Google Chrome 155 | Ya disponible |
| Playwright CLI | No se encontró el ejecutable | Instalar con el paso 1 |
| Python 3 | Necesario para el enlazador de Esquils | Comprobar si vas a usar el paso 3 |
| Docker y Compose | Docker 29.9.1 y Compose 5.6.0 | Disponibles para levantar Granolitos con Sail |

La [guía oficial de Playwright para agentes](https://github.com/microsoft/playwright/blob/main/docs/src/getting-started-cli.md) pide Node.js 20 o posterior. Tu versión cumple. Docker es un requisito del entorno Sail de Granolitos, no del navegador.

## 1. Instalar Playwright CLI

En una terminal de tu usuario:

```bash
npm install -g @playwright/cli@latest
playwright-cli --help
```

Esto instala la herramienta global según la [instrucción oficial](https://github.com/microsoft/playwright/blob/main/docs/src/getting-started-cli.md). No modifica las dependencias de Granolitos.

Tu prefijo global actual está en `/home/ronald/.nvm/versions/node/v24.12.0`; usa tu terminal con NVM cargado, sin `sudo`. Si cambias la versión activa de Node, vuelve a comprobar que `command -v playwright-cli` encuentra la herramienta. El proceso del agente también necesita ese directorio en su `PATH`; vuelve a abrir la aplicación del agente si conserva un entorno anterior.

## 2. Comprobar el navegador

Ejecuta desde una carpeta temporal para guardar allí las evidencias:

```bash
mkdir -p /tmp/esquils-browser-check
cd /tmp/esquils-browser-check
playwright-cli -s=setup-check open https://example.com --browser=chrome
playwright-cli -s=setup-check snapshot
playwright-cli -s=setup-check screenshot
playwright-cli -s=setup-check close
```

El snapshot debe mostrar «Example Domain» y la captura debe contener la página. La CLI permite seleccionar Chrome instalado y mantener una sesión con nombre, según su [referencia oficial](https://github.com/microsoft/playwright-cli/blob/main/README.md). La ejecución predeterminada no muestra una ventana; añade `--headed` al comando `open` si quieres verla desde tu escritorio.

Esta prueba confirma que el ejecutor funciona. Todavía falta comprobar el acceso a la aplicación desde el entorno donde trabaja el agente.

## 3. Hacer visible el skill de Esquils

Si todavía no está enlazado globalmente:

```bash
python3 --version
cd /home/ronald/code/esquils
python3 scripts/link-global-skills.py
```

El script enlaza todos los skills del repositorio en `~/.agents/skills` y `~/.claude/skills`. Conserva las entradas existentes e informa de los conflictos. Abre una sesión nueva del agente para que descubra el skill `verification-preflight`, ubicado en `skills/web/`.

## 4. Comprobar Granolitos

Desde el proyecto, levanta Sail si todavía no está activo:

```bash
cd /home/ronald/code/granolitos
./vendor/bin/sail up -d
```

Pide al agente que resuelva la URL mediante Laravel Boost y pruebe el acceso con el navegador seleccionado. Usa el endpoint que realmente responda en ese entorno: que una URL abra en tu navegador personal no demuestra que el navegador del agente pueda alcanzarla.

La comprobación debe mostrar una pantalla real de Granolitos, con sus estilos y recursos cargados. Si aparece una excepción de PostgreSQL, primero hay que reparar la conexión entre Laravel y la base de datos; reinstalar el navegador no corrige ese fallo.

Para validar formularios que crean o modifican datos, utiliza una instancia con base de datos y archivos aislados y un usuario de prueba. Comprueba la conexión efectiva del proceso web antes de preparar datos.

## Uso habitual

Puedes pedirlo así:

> Usa $verification-preflight y verifica este recorrido en el navegador: [pasos y resultado esperado]. Reutiliza el entorno disponible y captura evidencia del resultado.

La preparación de un entorno ya instalado tiene un presupuesto inicial de dos minutos. Si falla, el agente debe identificar la parte que bloquea el acceso y conservar lo comprobado. La instalación inicial y las reparaciones mayores se tratan como trabajo de entorno separado. Una vez listo, continúa directamente con el recorrido autorizado.

No necesitas instalar Puppeteer, crear una suite Playwright Test ni añadir un controlador propio para estos recorridos puntuales. Una suite repetible se prepara cuando el trabajo la requiere.
