# Monitoreo Colaborativo de Revistas Accesibles / Collaborative Monitoring of Accessible Journals

Esta página web muestra un listado de revistas académicas, indicando si son de acceso abierto, híbridas o si ofrecen opciones de publicación gratuita en acceso cerrado.  
This webpage displays a list of academic journals, showing whether they are open access, hybrid, or offer free closed-access publication options.

## Contenido / Contents

- `index.html` — Página principal con la tabla interactiva / Main page with the interactive table.  
- `styles/` — Estilos CSS de la página / CSS styles.  
- `js/` — Scripts JS, incluyendo DataTables / JS scripts, including DataTables.  
- `data/journals_normalized.csv` — Archivo CSV con la información de las revistas / CSV file containing journal data.  
- `html_generate.py` — Script Python que genera la tabla HTML a partir del CSV / Python script that generates the HTML table from the CSV.  

---

## Cómo actualizar la tabla / How to update the table

Existen **dos formas principales de agregar o actualizar información / There are two main ways to add or update information**:

### 1. Usando el formulario de colaboración / Using the collaboration form

1. Abre el formulario / Open the form: [Formulario de colaboración / Collaboration Form](https://docs.google.com/forms/d/e/1FAIpQLSexiJsU7BGfH8eN0xAHkp3X9M44Uj7J_tsFDkXMqOPiVGFvjQ/viewform?usp=preview)  
2. Completa los campos solicitados / Fill in the requested fields:
   - **Nombre de la revista / Journal Name**  
   - **Editorial / Publisher**  
   - **Factor de Impacto / Impact Factor** (Scimago o cifras oficiales / Scimago or official numbers)  
   - **¿Híbrida? / Hybrid?** (Sí/No / Yes/No)  
   - **¿Opción cerrada gratuita? / Free Closed-Access Option?** (Sí/No / Yes/No)  
   - **Link al sitio de la revista / Journal Website Link**  
   - **Área de la revista / Journal Area**  
   - **Comentarios / Comments** (opcional / optional)  
3. Envía el formulario / Submit the form.  
4. El administrador del proyecto agregará la nueva información al CSV y ejecutará `html_generate.py` para actualizar `index.html`.  
   The project administrator will add the new data to the CSV and run `html_generate.py` to update `index.html`.

---

### 2. Actualizando el archivo CSV mediante Pull Request / Updating the CSV via Pull Request

Para agregar o actualizar información de revistas, todo se hace a través de **Pull Requests (PRs)** en GitHub. No hay edición directa en el repositorio principal. / To add or update journal information, everything is done through **Pull Requests (PRs)** on GitHub. There is no direct editing in the main repository.

1. Hacer un **fork** del repositorio/ Make a fork:  
   - Ir a `https://github.com/SFBioinformaticsGroup/open_access_tracker` y hacer fork a tu cuenta.  
   - Clonar tu fork localmente:  
     ```bash
     git clone https://github.com/TU_USUARIO/open_access_tracker.git
     cd open_access_tracker
     ```

2. Abrir el archivo `data/journals_normalized.csv` y agregar nuevas filas siguiendo el formato de columnas/ open the  `data/journals_normalized.csv` file and add your new rows:

3. Guardar los cambios, hacer commit y push a tu fork / Save, commit, push and push:

```bash
git add data/journals_normalized.csv
git commit -m "Add new journal"
git push origin main
```

4. Abrir un Pull Request desde tu fork hacia el repositorio original (SFBioinformaticsGroup/open_access_tracker). GitHub mostrará automáticamente las diferencias. / Open a Pull Request from your fork to the original repository (SFBioinformaticsGroup/open_access_tracker). GitHub will automatically display the differences.

Tus aportes serán revisados por el equipo del SFBG para verificar que las columnas estén completas y que los enlaces sean correctos. / Your contributions will be reviewed by the SFBG team to ensure that the columns are complete and the links are correct.

Una vez aprobado el PR, tu nombre de usuario será aparecerá entre lxs colaboradorxs del proyecto. / 
Once the PR is approved, your username will appear among the project contributors.

¡GRACIAS POR TU APORTE!/ THANKS FOR HELPING!