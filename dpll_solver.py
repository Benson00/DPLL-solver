class DPLL_Solver:
    
    def __init__(self, formula):
        """Initialize the DPLL solver with the formula and empty assignments."""
        self.formula = formula  
        self.assignements = {}
        self.decision_stack = []  

    def unit_propagation(self):
        """Unit propagation, BCP (Boolean Constraint Propagation).

        Scans the clauses to find unit clauses (those containing only one literal).
        If a unit clause is found, a true or false value is assigned to the corresponding variable
        based on the sign of the literal. This helps deduce mandatory values for certain variables.
        """
        for clause in self.formula:
            if len(clause) == 1:
                self.assignements[abs(clause[0])] = (clause[0] > 0)
                print(f"Unit Clause Detected: {clause[0]:>3} | Assigned Value: {clause[0] > 0} | Variable: {abs(clause[0])}")

    def check_clause(self, clause):
        """Check if the given clause is satisfied with the current assignments."""
        return any(
            (lit < 0 and self.assignements.get(abs(lit), lit < 0) is False) or
            (lit > 0 and self.assignements.get(abs(lit), lit < 0) is True)
            for lit in clause
        )

    def check_satisfiability(self):
        """Check if the current formula is satisfiable with the current assignments."""
        return all(self.check_clause(clause) for clause in self.formula)

    def decision(self):
        """Make a decision by selecting the first unassigned literal in unsatisfied clauses."""
        for clause in self.formula:
            # Skip the clause if it is already satisfied
            if self.check_clause(clause):
                continue
            
            for lit in clause:
                print(f"Processing clause: {clause}")
                var = abs(lit)
                
                if var not in self.assignements:
                    self.assignements[var] = (lit > 0)
                    
                    self.decision_stack.append((var, self.assignements[var]))
                    
                    print(f"Decision: Variable {var} assigned {'True' if lit > 0 else 'False'}")
                    return True
        
        print("No decision is possible in this clause")
        
        if self.decision_stack:
            self.backtrack()
            return False
        
        print("No more decisions to make and no backtracking possible")
        return False

    def backtrack(self):
        """Backtrack by undoing the last decision."""
        if not self.decision_stack:
            print("No decisions to backtrack from")
            return
        
        var, value = self.decision_stack.pop()
        
        del self.assignements[var]
        
        new_value = not value
        self.assignements[var] = new_value
        self.decision_stack.append((var, new_value))
        
        print(f"Backtracking: Variable {var} reassigned to {'True' if new_value else 'False'}")

    def solve(self):
        """Main loop to solve the SAT problem using DPLL."""
    
        print("Running DPLL solver...")

        self.unit_propagation()

        while not self.check_satisfiability():
            if not self.decision():
                print("Current state:", self.assignements)  
                print("Final result: Unsatisfiable !!!")
                print("\n\n######################################################\n\n")
                return False

        print("SAT problem is satisfiable with the current assignments.")
        print("Final assignments:", self.assignements)  
        print("Final result: Satisfiable !!!")
        print("\n\n######################################################\n\n")

        return True



##############################################################################
if __name__ == "__main__":
    
    formula = [[1], [-2, 1], [3, -1], [-3]]  
    formula2 = [[1], [-2, 1], [4, -1], [-3]]  
    formula3 = [[1], [-4, -1], [4, -1], [-3]]  
    formula4 = [
        [1, -2, 3],    
        [-1, 2],       
        [2, -3],       
        [1, -3],       
        [-1, 3],       
        [-2],          
        [-3]           
    ]
    
    solver = DPLL_Solver(formula)
    result = solver.solve()
    solver = DPLL_Solver(formula2)
    result = solver.solve()
    solver = DPLL_Solver(formula3)
    result = solver.solve()
    solver = DPLL_Solver(formula4)
    result = solver.solve()