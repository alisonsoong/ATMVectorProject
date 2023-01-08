# ATMVectorProject:
[Project Doc](https://docs.google.com/document/d/1fjGd2PhNvcNCRg_KGf5zmZXxd_bmBvlUH75HdrPXgrI/edit?usp=sharing)
# Proposal:
A piecewise vector function generator to create new Mario Kart circuits. Given the number of unique sections (curves), the generator should piece together randomized vector functions to create a single continuous and differentiable vector function. Users should be able to indicate how many curves of each type they want in the randomized circuit. Finally, there should be an option to export a circuit and redraw it later in 3D.
# Things to tackle:
- [x] Test concept with 2D vector functions, graph w/ program
- [x] Apply to 3D
- [x] Add more complex base functions
- [x] Show curvature with gradient dotted line along curve 
- [x] Presentation slides

# Things we ran out of time for:
- Export and redraw (deemed unecessary)
- "End" the loop (get back to (0,0,z(0))) -> ran out of time to implement in code, but should be in presentation?

# Progress
## January 7 (but at night, ha)
Finished implementing all curvature! Here is the final product:

<img width="708" alt="Curvature" src="https://user-images.githubusercontent.com/57238372/211185428-45538e56-dc59-47c4-9dba-19d2e1faed58.png">


https://user-images.githubusercontent.com/57238372/211185432-bc7a6803-2b3f-4359-8684-5bcc2f372dd8.mov



## January 7
Finished implementing the three complex loops. Final list of loops:

r(t) = <at^2 + b, ct^2 + d>

r(t) = <at^2 + b, ct^3 + d>

r(t) = <acos(1.5t) + b, ccos(1.5t)sin(t) + d>

r(t) = <at + b, csin^2(t) + dcos(t)>

r(t) = <at + b, csin(t)cos(t) + d>




https://user-images.githubusercontent.com/57238372/211143363-37abdfa8-7116-4bb7-80bc-b032ec4230ac.mov




## December 13
First loop! However, directions don't seem to align. Will have to check calculations + verify the start and end positions/directions for each function...
Current pushed code is really dead, but the issue is just math.
![loop](https://github.com/alisonsoong/ATMVectorProject/blob/main/GeneratedGraphs/12_13_22/Loop.png)


https://user-images.githubusercontent.com/57238372/207484562-4db9969f-58f1-4c14-b45b-e0c4bb6871c1.mp4

Yeah, the directions aren't correct for sure ^^

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








