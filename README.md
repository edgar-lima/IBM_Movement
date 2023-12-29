Individual-based model to simulate home range movement.  
=======================================================
## The present simulation model it's part of my Ph.D. thesis in Ecology.

Here we have six Python scripts, one represent a superclass that has attributes  
common to all navigation capacity classes, and three subclasses of each navigation  
capacity model.  

### Individuals classes
1. **Individual**  
    Individual superclass.

2. **IndNoriented**  
    Individual class that represents random walk movement model.

3. **IndOriented**  
   Individual class that represents oriented walk movement model,
   the individuals collect information of landscape to chosse where to move.

4. **IndMemory**  
    Individuals class that represents memory movement model,
   the memory is built using reforcement-based learning.  

   Also, we have two others scripts, first is the metamodel that run all ecological dinamics
   and second is supports scripts.
   
By: Ph.D. Edgar Luiz de Lima  
e-mail: edgarluizdelima@gmail.com  
Research Gate: [Edgar Luiz de Lima](https://www.researchgate.net/profile/Edgar-Luiz-De-Lima)
