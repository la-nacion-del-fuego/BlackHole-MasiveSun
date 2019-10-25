![EmblemaFuegoControl](https://user-images.githubusercontent.com/38228291/67335050-6ba2c280-f523-11e9-93c5-928435fdd118.png)
# BlacHole-MasiveSun 
#### How to run the program
- Before running the program make sure you have the necessary requirements.

- Once done, run the program from the console using the command 
>> - python3 BlackHole.py


#### Introdution
In this project we will simulate the effect of accretion, accretion is the aggregation of matter to a body. For example, the accretion of mass by a star is the addition of mass to the star from interstellar matter or another star.


we will apply the accretion effect to a supermassive black hole that will drain the matter from the most giant star seen by the human, this star will be orbiting the black hole with some acceleration.

The following image is a clear example of the accretion effect that we will simulate between a black hole (Sagittarius) and a super massive sun or star (VY Canis A *)

<p align="center">
  <img width="230" height="160" src="https://user-images.githubusercontent.com/38228291/67441287-901e9d80-f5fc-11e9-8597-14014d006e4a.jpg">
</p>

Our goal to simulate being able to observe the behavior of "VY Canis" and "Sagittarius A *" if there were a case in which the gravitational ranges of both supermassive bodies coincided.

#### Methodology and Implementation

- First we import matplotlip and math in addition to adding copyright
- We start with the class **"def_particle()"** where we work with the particle and we define a constructor **"_init_()"** whitin the class.
- In the definition we do the function that will integrate the system by calculating the new position of "bhole." **"def_integrate()"**.
- We will calculate the kinetic energy of a particle with the method **"def_getkinecticEnergy()"**
- Now we create the "bhole" particle that will be the super massive "Sagittarius" black hole, in this class an object is being created and disappearing. Once created, we add elements of positioning, speed and mass **(0,0,33.813e^30 M. M☉)**. because it is static. These will be the initial conditions of our particle
- Then we will make prints integrating the delta time **"bhole.integrate(dt)"** and we will test in a cycle **"for t in the range (450)"**, each iteration is a cycle.
-Now we will add the star "Canis" that will be increased by the black hole, we add the initial conditions of distance position of the black hole, speed and mass **(20e ^ 8 km, y = 5e ^ 5km/years, 7.359e^30  M. M☉)**.
- The force exerted between two particles is measured after obtaining the distance between the two masses to know at what point the black hole make accretion with respect to the super massive star.
- We get the value of **"r"** (r is the distance between two particles) which is **"r = √2"**
- We will calculate the distance r with the method **"def_computer ()"** in **"def_integrate ()"**.
- **"r"** will begin with a value of **20e ^ 8 km** away from "Canis", the distance will change with respect to the time it will be every thousand years. The distance changes will be calculated by the program since the change of "r" does not have a pattern because they depend on the black hole.
- We calculate a **"U"** vector, which is the direction for not obtaining opposing forces using the method **"def_computerU"**.
- We calculate the distance using the Pythagorean theorem and we will be integrating the super massive star with respect to the black hole so that the direction of the path is correct.
- Things that are necessary to mention is that the cycle with which we are working serves to see the movement of the particles with the passage of the iterations and the graph that our programmer will show will be of three dimensions and we will not be working with an acceleration, only it will be the speed that we will include.
- we will have a trajectory change function called updateposition that will be in charge of updating the position with respect to the trajectory that is taking. The speed of "VY Canis Majoris" (super massive star) will always be the same when approaching and moving away from the black hole, its mass will only decrease due to the accretion effect.
- 
- Finally we will implement the plot class to trace the trajectory of "VY canis A *".
## Outcome and Prints
try 1: 
![Intento1](https://user-images.githubusercontent.com/38228291/67534840-561ecb80-f6d0-11e9-9f21-13e10c374210.png)
try 2:
![Intento2](https://user-images.githubusercontent.com/38228291/67534850-646ce780-f6d0-11e9-90e3-5282e9db9aa0.png)
try 3:
![Intento2_1](https://user-images.githubusercontent.com/38228291/67534872-72226d00-f6d0-11e9-9002-db783d32be30.png)
image 1:
![image](https://user-images.githubusercontent.com/38228291/67534881-7c446b80-f6d0-11e9-8abc-59aec6c1fe18.png)
image 2:
![image (1)](https://user-images.githubusercontent.com/38228291/67534901-8a928780-f6d0-11e9-88cb-b17de4cddccd.png)

#### Bibliography

- [definition of accretion](https://www.astromia.com/glosario/acrecion.htm)

- [image and acrettion information](https://www.nsf.gov/news/mmg/mmg_disp.jsp?med_id=66143)

- [Markdow support in Spanish](https://markdown.es/sintaxis-markdown/#links)

-  [fire nation image](https://es.wikipedia.org/wiki/Naci%C3%B3n_del_Fuego#/media/Archivo:EmblemaFuegoControl.png)
