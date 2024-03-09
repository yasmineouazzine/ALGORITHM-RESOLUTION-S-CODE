# ALGORITHM-RESOLUTION-S-CODE

# THE CODE PRESENT TRANSLATION OF THIS ALGORITHM:

                Début
                Ecrire la négation de F ;
                Mettre F sous forme d'un ensemble de 
                clauses ;
                Tant que la clause vide n'est pas rencontrée 
                et qu'il
                existe des paires réductibles faire
                Début
                Chercher des clauses résolvantes ;
                Ajouter ce résultat à la liste des clauses ;
                Fintantque ;
                Si on trouve la clause vide alors F est valide
                sinon F est invalide
                Finsi ;
                Fin ;




# Algorithm Explanation:

<p>The Propositional Logic Resolution algorithm is a fundamental method for determining the validity of logical formulas. Here's a breakdown of how the algorithm works:</p>


# 1-Negation and Conversion:

<p>.The input formula is first parsed to handle negations and convert it into a suitable form for resolution.</p>
<p>.Negations are processed, and literals are converted into integers for easier manipulation.</p>


# 2-Clause Formation:

<p>.The formula is split into clauses, where each clause represents a disjunction of literals.</p>
<p>.Clauses are organized to facilitate the resolution process.</p>

# 3-Resolution Rule:

<p>.The resolution rule is applied iteratively to derive new clauses from existing ones.</p>
<p>.The rule states that if two clauses contain complementary literals, they can be resolved to produce a new clause that is the union of the remaining literals from both clauses.</p>


# 4-Resolution Process:

<p>.The algorithm continues to apply the resolution rule until no new clauses can be derived or an empty clause is found.</p>
<p>.If an empty clause is found, the formula is considered invalid. Otherwise, it is valid.</p>


# PYTHON'S CODE :

# DESCRIPTION:

<p> This Python code implements the Propositional Logic Resolution algorithm using a graphical user interface (GUI) built with Tkinter. The algorithm resolves logical formulas to determine their validity. It provides a visual representation of the resolution steps and allows users to input their logical formulas for resolution.</p>


# USAGE:

# 1-Input Formulas:

<p>We can input logical formulas in a specific format using the GUI. The format should be like {¬P v ¬Q v R, ¬R, P, ¬T v Q, T} where ¬ represents negation, v represents disjunction (OR), and , separates clauses.</p>


# 2-Resolution: 

<p> Once a formula is entered, clicking the "Resolve" button triggers the resolution process. The algorithm will attempt to resolve the input formula and display whether the formula is valid or invalid.</p>


# 3-Output:

<p>The result of the resolution process is displayed in the GUI. If the formula is valid, it will display "F est valide". If the formula is invalid, it will display "F est invalide".</p>

# Functionality:

<p>.The algorithm parses the input formula, processes negations, and converts it into a suitable form for resolution.</p>
<p>.It iteratively applies the resolution rule to derive new clauses until no new clauses can be derived or an empty clause is found.</p>
<p>.The GUI provides a user-friendly interface for entering formulas, triggering resolution, and displaying results.</p>


# Purpose:

<p>This code is useful for demonstrating the application of the Propositional Logic Resolution algorithm in a visual and interactive manner. </p>


#  The function used to translate different parts of the resolution algorithm:


# 1-parse_formula_input(input_string):

<p>.This function takes an input string representing a logical formula.</p>
<p>.It extracts clauses from the input string and splits each clause into literals.</p>
<p>.The literals are processed to handle negation and converted into integers for easier manipulation.</p>
<p>.The function returns the processed clauses.</p>

# 2-negation(F):

<p>.This function handles negation in the formula.</p>
<p>.It negates each literal in the formula, maintaining the appropriate format.</p>
<p>.If the input is a list of clauses, it negates each literal within each clause.</p>
<p>.The function returns the negated formula.</p>

# 3-mettre_sous_forme_de_clauses(F):

<p>.This function organizes the formula into a list of clauses if it is not already in that form.</p>
<p>.It ensures that the formula is represented as an ensemble of clauses.</p>
<p>.If the input is already in clause form, it returns the input unchanged.</p>

# 4-chercher_clauses_resolvantes(clauses):

<p>.This function searches for resolvent clauses based on pairs of clauses containing complementary literals.</p>
<p>.It iterates through all pairs of clauses and literals, checking for complements.</p>
<p>.If complements are found, it constructs a resolvent clause by combining non-complementary literals from each clause.</p>
<p>.The function returns a list of resolvent clauses.</p>

# 5-resolution(F):

<p>.This is the main resolution algorithm.</p>
<p>.It negates the input formula, organizes it into clauses, and enters a loop.</p>
<p>.Inside the loop, it searches for resolvent clauses and adds them to the list of clauses.</p>
<p>.The loop continues until no new resolvent clauses can be found or an empty clause is encountered.</p>
<p>.If an empty clause is found, the formula is considered invalid; otherwise, it is valid.</p>
<p>.The function returns a string indicating the validity of the formula.</p>

# 6-handle_resolution():

<p>.This function is called when the user triggers the resolution process.</p>
<p>.It retrieves the formula input by the user, attempts to parse it, and invokes the resolution algorithm.</p>
<p>.The result of the resolution process is then displayed to the user.</p>

# 7-show_resolution_interface():

<p>.This function is called to switch from the welcome page to the resolution algorithm interface.</p>
<p>.It hides the welcome frame and displays the algorithm frame, allowing the user to interact with the resolution process.</p>


# Friendly-User Interface :

# First page (Welcome page ) :

<p>The appearance of the fist message :</p>
    <p>Welcome to the Resolution Algorithm </p>
    <p>created by Yasmine Ouazzine</p>
    
<p><b>The first page </b></p>

![First page](https://github.com/yasmineouazzine/ALGORITHM-RESOLUTION-S-CODE/assets/142170643/b45e6f21-5b4f-4239-8f46-9d8e6877c3a9)

 <p><b>The second page </b></p>


 ![Second page](https://github.com/yasmineouazzine/ALGORITHM-RESOLUTION-S-CODE/assets/142170643/286ed254-c67c-40b1-91a1-76bd2f3e744a)
