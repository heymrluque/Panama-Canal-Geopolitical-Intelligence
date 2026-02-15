# 🚢 Panama Canal Geopolitical Intelligence Miner
> **Extracción de Relaciones y Grafos de Conocimiento mediante Stanford CoreNLP (Pipeline 2026)**

![Status](https://img.shields.io/badge/Status-Completed-success)
![NLP](https://img.shields.io/badge/NLP-Stanford%20CoreNLP-blue)
![Topic](https://img.shields.io/badge/Topic-Geopolitics-red)

## 📌 Resumen del Proyecto
Este sistema automatiza la vigilancia informativa sobre la soberanía del **Canal de Panamá** frente a las políticas de la administración **Donald Trump**. Utilizando técnicas avanzadas de Procesamiento del Lenguaje Natural (PLN), transformamos noticias internacionales en un **Grafo de Conocimiento** estructurado.

## 🛠️ Metodología Técnica
El sistema implementa un pipeline de procesamiento profundo que incluye:
* **NER (Named Entity Recognition):** Identificación de actores clave (Trump, Mulino, CK Hutchison).
* **Coreference Resolution:** Vinculación de pronombres ("he", "his administration") a los sujetos correctos para evitar la pérdida de datos.
* **OpenIE (Open Information Extraction):** Extracción de tripletas dinámicas `(Sujeto - Relación - Objeto)` para mapear acciones diplomáticas y amenazas.

## 📊 Resultados Visuales
El sistema genera un grafo interactivo donde se visualiza la red de poder y tensión:
* **Nodos:** Actores políticos e infraestructuras.
* **Aristas (Flechas):** Acciones extraídas (ej. *threatened*, *invalidated*, *defended*).

> [!TIP]
> Puedes ver el grafo interactivo en la carpeta `/visualizations`.

## 🚀 Ejecución
Para reproducir el análisis, se utilizó el siguiente comando en CoreNLP 4.5.10:
```bash
java -Xmx8g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,depparse,natlog,openie,coref,kbp -file pln/noticias -outputFormat json -outputDirectory pln/output_json
