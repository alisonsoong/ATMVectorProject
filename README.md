# ATMVectorProject:
[Project Doc](https://docs.google.com/document/d/1fjGd2PhNvcNCRg_KGf5zmZXxd_bmBvlUH75HdrPXgrI/edit?usp=sharing)
# Proposal:
A piecewise vector function generator to create new Mario Kart circuits. Given the number of unique sections (curves), the generator should piece together randomized vector functions to create a single continuous and differentiable vector function. Users should be able to indicate how many curves of each type they want in the randomized circuit. Finally, there should be an option to export a circuit and redraw it later in 3D.
# Things to tackle:
- [x] Test concept with 2D vector functions, graph w/ program
- [x] Apply to 3D
- [ ] Export and redraw
- [ ] Add more complex base functions
- [ ] "End" the loop (get back to (0,0,z(0)))
- [ ] Show curvature with gradient dotted line along curve 
- [ ] CAD model
- [ ] Presentation slides
# Progress
## Thursday, December 7
Circuit generator created! Randomized z func generator as well using shifted/scaled sin and cos functions. Also, only deg 2 and deg 3 polynomials used for now.
### all put together!
![Circuit generator](https://github.com/alisonsoong/ATMVectorProject/blob/main/GeneratedGraphs/12_7_22/CircuitGeneratorV2.png)
### random zline generator 
![Random z func generator](https://github.com/alisonsoong/ATMVectorProject/blob/main/GeneratedGraphs/12_7_22/RandomZFunc.png)
## Wednesday, December 6
Randomized junction with z func (just sin(t))
![xline, yline, zline](https://github.com/alisonsoong/ATMVectorProject/blob/main/GeneratedGraphs/12_6_22/RandomizedJunction.png)
## Monday, December 5
Finished implementing test case: parabola (in orange) to cubic polynomial (gray)
![Just xline and yline](https://github.com/alisonsoong/ATMVectorProject/blob/main/GeneratedGraphs/12_5_22/FirstJunctionProjection.png)








