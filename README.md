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

<img src="First page.png">

 <p><b>The second page </b></p>


<img src="Second page.png">

 # Test ( we will use some formula to test the code ):

# 1-Test 1 :
we will use this formula first : <p><b>{¬P ∧ ¬Q  v P}</b></p>

#  Truth table :
<p>. we will use the truth table to understand the result given by the code </p>
<img src="Truth table.png">


#  Analyse the Formula :

<p>.¬P ∧ ¬Q: This part of the formula represents the negation of P and the negation of Q, meaning both P and Q must be false for this part to be true.</p>
<p>.¬P ∧ ¬Q v P: The conjunction (¬P ∧ ¬Q) evaluates to true when both P and Q are false. The disjunction of (¬P ∧ ¬Q) with P will be true if either (¬P ∧ ¬Q) is true or if P is true. Given that (¬P ∧ ¬Q) can only be true when P is false, the formula becomes true only when P is false. This makes sense logically because if P is false, then the whole formula will evaluate to true regardless of the value of Q.</p>

<p><b>Therefore, the formula {¬P ∧ ¬Q v P} is valid because it is always true regardless of the truth values of P and Q.</b></p>

# we can visualize the steps thanks to the friendy-use interface :

<p>.we will insert the expression and click on Resolve to visualize the result:</p>

<img src="test de formule 3 qui est valide.png">

<p><b> Thanks to the Analyze and the Truth table we concluded that the expression is valid</b></p>

  <p><b>*WE WILL USE DIFFERENT FORMULA AND WE GET THE RESULT USING THE SAME STEPS</p></b> 
  <p><b> Let's visualize the result of each formula </b></p>

# 2-Test 2 :
we will this time use the expression : <p></b>{P}</p></b>

#  Analyse the Formula
<p>The formula {P}  contains only one clause, P. 
For the entire statement to be true, the value of  P  must be true. Since there are no conflicting clauses or conditions, and the only requirement is for  P  to be true, the formula is valid.
In essence, this formula asserts a single condition: P must be true, and there are no contradictory statements or additional requirements. Therefore, any truth assignment where P is true satisfies the formula, making it valid.</p>

<p>.we will insert the expression and click on Resolve to visualize the result:</p>
<img src="test de formule 2 qui est valide.png">


# 3- Test3:
we will this time use the expression : <p></b>{¬P v ¬Q v R, ¬R, P, ¬T v Q, T}</p></b>

#  Analyse the Formula

<p>To determine the validity of the formula {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}, let's analyze it:</p>

# 1. ¬P v ¬Q v R:
<p>This clause indicates that either  P  or  Q  or both must be false for the entire statement to be true. So, if both P  and  Q  are false, or if either  P  or  Q  is false and  R  is true, then this clause holds.</p>

# 2. ¬R:
 <p>This clause states that  R  must be false.</p>

# 3.P :
<p>This clause states that  P  must be true.</p>

# 4.¬T v Q :
<p>This clause indicates that either  T  must be false or  Q  must be true for the entire statement to be true.</p>

# 5.T :
<p>This clause states that  T  must be true.</p>

# the consistency of these clauses:

<p>- Clauses 1, 2, and 3 together imply that P  must be true, and  R  must be false.</p>
<p>- Clauses 4 and 5 together imply that T  must be true, and Q  must also be true.</p>

<p><b></b>However, if Q  is true and P  is true, clause 1 suggests that either ¬P  or  ¬Q  must be true, which contradicts our initial assumption that both  P  and  Q  are true. Therefore, the formula is invalid.</p></b>
<p>.we will insert the expression and click on Resolve to visualize the result:</p>
<img src="test de formule 1  qui est invalide.png">


# 4-Test 4 :
we will this time use the expression : <p></b>{P v Q , ¬Q , P} </p></b>
<p><b>Explination:</b></p>
<p>To determine the validity of the formula {P v Q , ¬Q , P}  , let's analyze it:</p>

<p>.The formula is invalid because it leads to a contradiction.

The first clause P v Q indicates that either P, or Q, or both must be true. However, the second clause ¬Q states that Q must be false. This creates a contradiction with the first clause because if Q must be false but also true (according to the first clause), there is a conflict.

Furthermore, the third clause P cannot resolve this contradiction because it does not affect the value of Q. Thus, there is no possible truth assignment that can make all the clauses true, rendering the formula invalid..</p>
<p>.we will insert the expression and click on Resolve to visualize the result:</p>
<img src="test de formule 4 qui est invalide.png">

# USAGE :
<p>1-Clone the repository to your local machine.</p>

<p>2-Navigate to the Project Directory.</p>

<p>3-Run the Application.</p>

<p>4-Input Formula: Enter the formula.</p>

<p>5-Submit and Check: Click the "Resolve" button to check the validity of the formula. The result will be displayed on the screen.</p>



