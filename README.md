![EmblemaFuegoControl](https://user-images.githubusercontent.com/38228291/67334009-ce935a00-f521-11e9-8351-6f28765d8f81.png)
# BlacHole-MasiveSun 
#### Introdution
In this project we will simulate the effect of accretion, accretion is the aggregation of matter to a body. For example, the accretion of mass by a star is the addition of mass to the star from interstellar matter or another star.


we will apply the accretion effect to a supermassive black hole that will drain the matter from the most giant star seen by the human, this star will be orbiting the black hole with some acceleration.

#### methodology

- first we import matplotlip and math in addition to adding copyright
- We start with the class "def_particle()" where we work with the particle and we define a constructor "_init_()" whitin the class.
- In the definition we do the function that will integrate the system by calculating the new position of "bhole." "def_integrate()".
- We will calculate the kinetic energy of a particle with the method "def_getkinecticEnergy()"
- Now we create the "bhole" particle that will be the super massive "Sagittarius" black hole, in this class an object is being created and disappearing. Once created, we add elements of speed, positioning and mass that will be (0,0,0) because it is static. These will be the initial conditions of our particle
