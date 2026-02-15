import json
import os
from pyvis.network import Network

# Configuración del grafo
net = Network(notebook=False, directed=True, bgcolor="#222222", font_color="white")
net.barnes_hut()

path_to_json = "../output_json/"
for file_name in os.listdir(path_to_json):
    if file_name.endswith(".json"):
        with open(os.path.join(path_to_json, file_name), 'r') as f:
            data = json.load(f)
            # Extraer tripletas de OpenIE
            for sentence in data['sentences']:
                for triple in sentence.get('openie', []):
                    subj = triple['subject']
                    obj = triple['object']
                    rel = triple['relation']
                    
                    # Añadir nodos y arista (flecha)
                    net.add_node(subj, label=subj, title=subj, color="#00ffcc")
                    net.add_node(obj, label=obj, title=obj, color="#ff0066")
                    net.add_edge(subj, obj, title=rel, label=rel)

# Guardar el resultado
net.save_graph("../visualizations/grafo_interactivo.html")
print("¡Grafo generado con éxito en la carpeta visualizations!")