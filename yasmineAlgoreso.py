import tkinter as tk
from tkinter import messagebox
import re

def parse_formula_input(input_string):
    # Extract clauses from the input string
    clauses_match = re.findall(r'\{(.*?)\}', input_string)
    if not clauses_match:
        raise ValueError("Invalid input format. Please use the format {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}")

    # Split each clause into literals
    clauses = [re.split(r'\s*v\s*', clause) for clause in clauses_match[0].split(',')]

    # Process literals to handle negation (¬) and convert to integers
    processed_clauses = []
    for clause in clauses:
        processed_clause = []
        for literal in clause:
            literal = literal.strip()
            if literal.startswith("¬"):
                processed_clause.append(-ord(literal[1]) + ord("A") + 1)
            else:
                processed_clause.append(ord(literal) - ord("A") + 1)
        processed_clauses.append(processed_clause)

    return processed_clauses

def negation(F):
    if isinstance(F[0], list):
        return [[-literal for literal in clause] for clause in F]
    else:
        return [-F]

def mettre_sous_forme_de_clauses(F):
    return [F] if isinstance(F[0], int) else F

def chercher_clauses_resolvantes(clauses):
    result = []
    for i in range(len(clauses)):
        for j in range(i+1, len(clauses)):
            for literal_i in clauses[i]:
                for literal_j in clauses[j]:
                    if abs(literal_i) == abs(literal_j):  # Check if the literals are complementary
                        resolvant = [literal for literal in clauses[i] if literal != literal_i] + \
                                    [literal for literal in clauses[j] if literal != literal_j]
                        if resolvant not in result:  # Check if the resolvant is already present
                            result.append(resolvant)
    return result

def resolution(F):
    neg_F = negation(F)
    clauses = mettre_sous_forme_de_clauses(neg_F)
    while True:
        new_resolvantes = chercher_clauses_resolvantes(clauses)
        if not new_resolvantes:
            return "F est valide"

        # Add new resolvants to the clauses
        for resolvant in new_resolvantes:
            if all(lit not in clauses for lit in resolvant):  # Check if the resolvant is already present
                clauses.append(resolvant)

        # Check for an empty clause
        if [] in clauses:
            return "F est invalide"

def handle_resolution():
    formula_input = formula_entry.get()
    try:
        formula = parse_formula_input(formula_input)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    result = resolution(formula)
    result_label.config(text=result)

def show_resolution_interface():
    welcome_frame.pack_forget()
    algorithm_frame.pack(fill="both", expand=True)
    root.geometry("")  # Reset geometry to fit content

# Create the main application window
root = tk.Tk()
root.title("Propositional Logic Resolution")

# Set background and foreground colors
bg_color = "#66ccff"
root.config(bg=bg_color)
label_color = "#333333"
entry_color = "white"
button_color = "#008080"
button_text_color = "white"
result_text_color = "#009900"


# Create welcome page
welcome_frame = tk.Frame(root, bg=bg_color, width=400, height=300)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to the Resolution Algorithm\ncreated by Yasmine Ouazzine",
                         bg=bg_color, fg="white",  font=("Arial", 20))
welcome_label.pack(pady=20)

enter_button = tk.Button(welcome_frame, text="Enter to test it", command=show_resolution_interface,
                         bg=button_color, fg="white",  font=("Arial", 12))
enter_button.pack(pady=20)

# Create the resolution algorithm frame
algorithm_frame = tk.Frame(root, bg=bg_color)

# Create the input label and entry
formula_label = tk.Label(algorithm_frame, text="Enter the formula:", bg=bg_color, fg=label_color, font=("Arial", 10, "bold"))
formula_label.pack()

formula_entry = tk.Entry(algorithm_frame, width=50, bg=entry_color)
formula_entry.pack()

# Create the resolution button
resolve_button = tk.Button(algorithm_frame, text="Resolve", command=handle_resolution, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
resolve_button.pack()

# Create the output label
result_label = tk.Label(algorithm_frame, text="", bg=bg_color, fg=result_text_color, font=("Arial", 10, "bold"))
result_label.pack()

# Footer
footer_label = tk.Label(algorithm_frame, text="Created by Yasmine Ouazzine", bg=bg_color, fg=label_color, font=("Arial", 10, "bold"))
footer_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
