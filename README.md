![EmblemaFuegoControl](https://user-images.githubusercontent.com/38228291/67335050-6ba2c280-f523-11e9-93c5-928435fdd118.png)
# BlacHole-MasiveSun 
#### Introdution
In this project we will simulate the effect of accretion, accretion is the aggregation of matter to a body. For example, the accretion of mass by a star is the addition of mass to the star from interstellar matter or another star.


we will apply the accretion effect to a supermassive black hole that will drain the matter from the most giant star seen by the human, this star will be orbiting the black hole with some acceleration.

#### methodology

- first we import matplotlip and math in addition to adding copyright
- We start with the class **"def_particle()"** where we work with the particle and we define a constructor **"_init_()"** whitin the class.
- In the definition we do the function that will integrate the system by calculating the new position of "bhole." **"def_integrate()"**.
- We will calculate the kinetic energy of a particle with the method **"def_getkinecticEnergy()"**
- Now we create the "bhole" particle that will be the super massive "Sagittarius" black hole, in this class an object is being created and disappearing. Once created, we add elements of positioning, speed and mass **(0,0,7.38 M. M☉)**. because it is static. These will be the initial conditions of our particle
- Then we will make prints integrating the delta time **"bhole.integrate(dt)"** and we will test in a cycle **"for t in the range (450)"**, each iteration is a cycle.
-Now we will add the star "Canis" that will be increased by the black hole, we add the initial conditions of distance position of the black hole, speed and mass **(20e ^ 8 km, y = 5e ^ 5, 33.81 M. M☉)**.
- The force exerted between two particles is measured after obtaining the distance between the two masses to know at what point the black hole make accretion with respect to the super massive star.
- We get the value of **"r"** (r is the distance between two particles) which is **"r = √2"**
- We will calculate the distance r with the method **"def_computer ()"** in **"def_integrate ()"**.
- **"r"** will begin with a value of **20e ^ 8 km** away from "Canis", the distance will change with respect to the time it will be every thousand years. The distance changes will be calculated by the program since the change of "r" does not have a pattern because they depend on the black hole.
- We calculate a **"U"** vector, which is the direction for not obtaining opposing forces using the method **"def_computerU"**.
- we calculate the distance using the Pythagorean theorem
and we will be integrating the super massive star with respect to the black hole so that the direction of the path is correct.
- Things that are necessary to mention is that the cycle with which we are working serves to see the movement of the particles with the passage of the iterations and the graph that our programmer will show will be of three dimensions and we will not be working with an acceleration, only it will be the speed that we will include.
