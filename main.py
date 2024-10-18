from solver.dpll_solver import DPLL_Solver

formula = [[1], [-2, 1], [3, -1], [-3]]  

solver = DPLL_Solver(formula)
solver.solve()