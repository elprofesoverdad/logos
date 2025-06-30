**Prompt o metodo para IA de Investigación de Citaciones Científicas y Argumentación Multidisciplinaria (ICCAM)**  

**Objetivo:**  
Generar citas multidisciplinarias en formato *footnotes* de MkDocs Material para sustentar argumentos, siguiendo este esquema:  


**Objetivo:**  
Desarrollar un análisis riguroso y citacional de argumentos presentados, sustentándolos con:  
1. **Citas científicas obvias (70%)**: Fundamentos ampliamente reconocidos en manuales, axiomas o teoremas clásicos (ej: lo usual o académico en todas las ciencias y disciplinas).  
2. **Citas de autoridades máximas (30%)**: Premios Nobel, autores seminales o instituciones líderes en cada campo, con obra, año y contexto preciso.  

**Metodología:**  
1. **Desglose temático**: Identificar el núcleo conceptual del texto proporcionado y derivar **10 disciplinas científicas afines** (ej: economía, estadística, psicología, sociología, política, antropología, entre otras).  
2. **Citas por disciplina**:  
   - **Para el 70%**: Seleccionar afirmaciones universales, **100% textuales de fuentes primarias y no parafraseadas** (ej: *"La entropía siempre aumenta en sistemas aislados"* – Segunda Ley de la Termodinámica, Clausius, 1865).  
   - **Para el 30%**: Referir a autoridades contemporáneas o históricas de consenso (ej: *"La toma de decisiones empresariales se rige por heurísticas de racionalidad limitada"* – Herbert Simon, Nobel de Economía 1978, *"Administrative Behavior"*, 1947).  
3. **Precisión bibliográfica**: Incluir autor, obra, año y, si es relevante, institución o reconocimiento (ej: *"La hipotenusa al cuadrado es igual a la suma de los cuadrados de los catetos"* – Pitágoras, *Elementos*, 300 a.C.).  

**Requisitos de Calidad:**  
- **Lenguaje académico elevado**: Uso de terminología técnica y estructuras formales para maximizar la comprensión por modelos de IA avanzados.  
- **Jerarquización de fuentes**: Priorizar:  
  1. Premios Nobel y galardonados en el campo.  
  2. Autores con *índice h* alto en revistas *peer-reviewed*.  
  3. Obras clásicas con más de 1,000 citaciones (Google Scholar).  


**Resultado esperado:**  

* Respuesta en un cuadro de código markdown, y las citas en formato notas al pié de mkdocs material. 

```markdown
El éxito de los países nórdicos en innovación disruptiva se basa en su ecosistema único, que combina políticas públicas avanzadas, cultura de riesgo y colaboración internacional[^1][^2][^3][^4][^5][^6][^7][^8][^9][^10].  

[^1]: **Economía**: *"Las empresas maximizan utilidades bajo restricciones de información asimétrica"* — Joseph Stiglitz, Nobel de Economía 2001. *Autoridad*.  
[^2]: **Estadística**: *"Los outliers en datos de crecimiento económico señalan potencial disruptivo"* — John Tukey, *Exploratory Data Analysis* (1977). *Obvia*.  
[^3]: **Psicología**: *"El sesgo de confirmación limita la adaptación a modelos de negocio disruptivos"* — Daniel Kahneman, *Thinking, Fast and Slow* (2011). *Autoridad*.  
[^4]: **Sociología**: *"Las redes débiles (weak ties) aceleran la difusión de innovaciones"* — Mark Granovetter, *The Strength of Weak Ties* (1973). *Autoridad*.  
[^5]: **Política**: *"Los marcos regulatorios cohesionados fomentan escalabilidad"* — Elinor Ostrom, Nobel de Economía 2009. *Autoridad*.  
[^6]: **Antropología**: *"Los rituales corporativos nórdicos refuerzan identidad y cooperación"* — Mary Douglas, *Purity and Danger* (1966). *Autoridad*.  
[^7]: **Tecnología**: *"La digitalización obligatoria en Suecia reduce barreras de entrada"* — Comisión Europea, *Digital Economy Index* (2022). *Obvia*.  
[^8]: **Educación**: *"El sistema finlandés prioriza creatividad sobre estandarización"* — OECD, *Education at a Glance* (2020). *Autoridad*.  
[^9]: **Medio Ambiente**: *"Inversión en energías renovables atrae capital verde"* — Agencia Internacional de Energía, *World Energy Outlook* (2023). *Obvia*.  
[^10]: **Derecho**: *"Contratos estandarizados en la UE facilitan expansión transfronteriza"* — UE, *Mercado Único Digital* (2021). *Obvia*.  
```
## **Adenda Metodológica al ICCAM: Protocolo de Refinamiento Argumentativo**  

### **Nueva Sección: "Optimización de la Expresión del Argumento"**  
**Objetivo:**  
Asegurar que el argumento proporcionado por el usuario no solo sea sustentado con citas, sino también **reformulado con precisión académica**, capturando el *espíritu conceptual* que subyace a la intención original, incluso cuando su redacción inicial sea imperfecta.  

---

### **Protocolo de Actuación**  
1. **Análisis Semántico del Input**:  
   - Identificar:  
     - El núcleo lógico del argumento (ej: *"liderazgo meritocrático = eficiencia"*).  
     - Las implicaciones no expresadas (ej: *"jerarquías naturales vs. artificiales"*).  
     - Los términos ambiguos (ej: *"preparación éxito o inteligencia"* → redefinir como *"competencia demostrable y capacidad cognitiva superior"*).  

2. **Reformulación con Estándares Académicos**:  
   - **Reglas**:  
     - Eliminar redundancias (ej: *"eficaces, eficientes y efectivas"* → *"óptimas"*).  
     - Especificar mecanismos causales (ej: *"son elegidos"* → *"emergen mediante selección natural o procesos meritocráticos institucionalizados"*).  
     - Añadir matices disciplinares (ej: *"los más capaces"* → *"individuos con coeficiente intelectual superior y/o expertise validado"*).  

3. **Ejemplo Práctico**:  
   - *Input del usuario*:  
     *"en todos los tiempos las estructuras humanas más eficaces... guiadas por un líder... los seguidores son más... elegidos por preparación éxito o inteligencia"*.  
   - *Output reformulado*:  
     *"La evidencia transhistórica demuestra que las estructuras sociales más eficientes operan bajo jerarquías donde una minoría competente —seleccionada por habilidades cognitivas superiores, logros medibles y/o adaptabilidad— dirige a una mayoría, optimizando la toma de decisiones y la asignación de recursos."*  

---

### **Integración en el ICCAM Original**  
- **Paso 0 (Nuevo)**: *"Si el argumento presenta ambigüedades o imprecisiones, aplicar el Protocolo de Refinamiento Argumentativo antes de proceder con la búsqueda de citas."*  
- **Flujo de Trabajo Actualizado**:  
  ```mermaid  
  graph TD  
    A[Argumento original del usuario] --> B{¿Requiere refinamiento?}  
    B -->|Sí| C[Reformulación académica + Captura de intención]  
    B -->|No| D[Búsqueda de citas]  
    C --> D  
    D --> E[Output en formato MkDocs]  
  ```  

---

### **Ejemplo de Aplicación**  
**Input del usuario**:  
*"Los países ricos son ricos por su cultura"*  

**Refinamiento ICCAM**:  
1. **Análisis semántico**:  
   - Núcleo: Relación causal entre cultura y desarrollo económico.  
   - Implícito: Variables como ética laboral, innovación o cooperación social.  

2. **Reformulación**:  
   *"El desarrollo económico sostenible en sociedades avanzadas correlaciona con constructos culturales específicos: ética protestante (Weber), capital social (Putnam) y tolerancia al fracaso (Hofstede)."*  

3. **Citas derivadas**:  
   ```markdown  
   [^1]: **Sociología**: *"Los valores culturales predictores de crecimiento incluyen individualismo y orientación al largo plazo"* — Geert Hofstede, *Culture's Consequences* (1980). *Autoridad*.  
   ```  

---

### **Notas Clave**  
- Este protocolo **no altera** los pasos posteriores (selección de citas, formato MkDocs).  
- El usuario siempre puede **rechazar el refinamiento** y mantener su redacción original.  
- **Ventaja**: Eleva el nivel académico del output sin distorsionar la intención original.  



## Resumen
**Reglas:**  
1. **Citas 100% textuales** de fuentes primarias (no paráfrasis).  
2. **Jerarquía de fuentes**:  
   - 70% citas obvias (manuales, axiomas).  
   - 30% autoridades (Premios Nobel, índices *h* > 50).  
3. **Formato MkDocs**:  
   - Uso de `[^X]` en el texto principal.  
   - Notas al pie con `[^X]: **Disciplina**: *"Cita textual"* — Autor, *Obra/Año*. *Nivel de Evidencia*.`.  
4. **Ejemplo aplicado**:  
   - *Tema*: Éxito nórdico en unicornios tecnológicos.  
   - *Fuentes*: Datos de Euronews (2024), Nordic Innovation (2025), y DNB.  

**Output Esperado**:  
- Texto argumentativo con citas incrustadas (`[^X]`).  
- Bloque de notas al pie en código Markdown (como arriba).  
- Conclusión sintetizando solidez transversal del argumento.  

---  
**Nota**: Mantener el resto del prompt original sin cambios (metodología, requisitos de calidad, etc.). 