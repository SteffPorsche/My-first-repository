from graphviz import Digraph

def create_system_model():
    dot = Digraph("Förderbandsystem", format="png")
    
    # Komponenten
    dot.node("E", "Eingangssensor", shape="ellipse", style="filled", fillcolor="lightblue")
    dot.node("A", "Ausgangssensor", shape="ellipse", style="filled", fillcolor="lightblue")
    dot.node("F", "Förderband", shape="box", style="filled", fillcolor="lightgray")
    dot.node("S", "Steuerungssystem", shape="diamond", style="filled", fillcolor="lightgreen")
    dot.node("N", "Notfallmechanismus", shape="parallelogram", style="filled", fillcolor="orange")
    dot.node("L", "Logging-Modul", shape="parallelogram", style="filled", fillcolor="yellow")
    
    # Verbindungen
    dot.edge("E", "S", label="Bauteil erkannt")
    dot.edge("S", "F", label="Starte Transport")
    dot.edge("F", "A", label="Bauteil bewegt sich")
    dot.edge("A", "S", label="Bauteil verlassen")
    dot.edge("S", "L", label="Protokollierung")
    dot.edge("S", "N", label="Fehlermeldung bei Sensorausfall")
    dot.edge("N", "S", label="Notfallreaktion")
    
    return dot

# Erstellen des Diagramms
model = create_system_model()
model.render("foerderbandsystem", view=True)
