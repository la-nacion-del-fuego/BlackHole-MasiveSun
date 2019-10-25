![EmblemaFuegoControl](https://user-images.githubusercontent.com/38228291/67335050-6ba2c280-f523-11e9-93c5-928435fdd118.png)
# BlacHole-MasiveSun 

This is a fork of Implementation of N-Body System Code, De La Luz, V. https://github.com/itztli/n-body.git

#### How to run the program
- Before running the program make sure you have the necessary requirements.

- Once done, for usage:
>> - git clone https://github.com/la-nacion-del-fuego/BlackHole-MasiveSun.git
>> - cd BlackHole-MasiveSun-master
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
- We will also implement the updateMass class where we will work with the exchange of matter between Cagitario and Canis when it falls into its gravitational potential.
- Finally we will implement the **plot class** to trace the trajectory of "VY canis A *".
## Outcome and Prints
  
  
result: Now we know that due to the mass of both bodies they behave like a binary system that is slowly dying due to the passing of the years through the black hole is absorbing the mass of Canis.The mass of VY Canis Majoris is reduced approximately
6.9e^23 every 10 years and the Sagittarius earns the same amount of mass.

  
test 1: This graph exemplifies or shows that at the beginning both masses being incredibly gigantic are attracted and the sun being more massive the black hole tends to move faster than the sun, both pass close to each other and then move away but without losing their attraction.
>Variables:
>>- VCw := 33.813e^30          
>>- Sw := 7.359e^30
>>- dt := 10 años                          
>>- C:= 0                                
>>- T := 1,000,000 de años
>>The separation between Sagittarius and Canis is 5e^5km
![Intento1](https://user-images.githubusercontent.com/38228291/67534840-561ecb80-f6d0-11e9-9f21-13e10c374210.png)
  
  
test 2: In this graph the time was reduced to 900,000 years and it can be seen that it behaves in the same way as the previous one but by reducing the time it is simply distinguished as it moves away less.
>Variables:
>>- VCw :=  33.813e^30
>>- Sw := 7.359e^30
>>- dt := 10 años  
>>- T := 900000 años
>>- C:= 4.44714e^21
>>The separation between Sagittarius and Canis is 5e^5km
![Intento2](https://user-images.githubusercontent.com/38228291/67534850-646ce780-f6d0-11e9-90e3-5282e9db9aa0.png)
  
  
test 3: This image is exactly the same as the previous one in its initial conditions but seen from another angle.
>Variables:
>>- VCw :=  33.813e^30
>>- Sw := 7.359e^30
>>- dt := 10 años
>>- T := 900000 años
>>- C:= 4.44714e^21
>>The separation between Sagittarius and Canis is 5e^5km
![Intento2_1](https://user-images.githubusercontent.com/38228291/67534872-72226d00-f6d0-11e9-9002-db783d32be30.png)
  
  
test 4: In this last test, we decided to see what would happen once the hole has already completely consumed the sun.
The image shows a few moments before the sun disappears completely, where it generates a kind of small spiral just before obtaining its future trajectory.
>Variables:
>>- VCw := 33.813e^30
>>- Sw := 7.359e^30
>>- dt := 10 años
>>- T := 900000 años
>>- C:= 15e^28
>>The separation between Sagittarius and Canis is 5e^5km
![image (1)](https://user-images.githubusercontent.com/38228291/67534901-8a928780-f6d0-11e9-88cb-b17de4cddccd.png)
  
  
Loss and increase of matter:
  
  
![image](https://user-images.githubusercontent.com/38228291/67534881-7c446b80-f6d0-11e9-8abc-59aec6c1fe18.png)
- this image complements the loss and gain of matter from the previous graph
![complemento image](https://user-images.githubusercontent.com/38228291/67544392-8b89e000-f6f5-11e9-82f2-7de63698a12c.png)
#### Bibliography
- [Implementation of N-Body System] De La Luz, V. GitHub.com. https://github.com/itztli/n-body.git

- [definition of accretion](https://www.astromia.com/glosario/acrecion.htm)

- [image and acrettion information](https://www.nsf.gov/news/mmg/mmg_disp.jsp?med_id=66143)

- [Accretion of a black hole](https://edition.cnn.com/2019/09/26/world/black-hole-shredding-star-scn/index.html)

- [Mass of a particle](https://en.wikipedia.org/wiki/Solar_wind)

- [Markdow support in Spanish](https://markdown.es/sintaxis-markdown/#links)

- [fire nation image](https://es.wikipedia.org/wiki/Naci%C3%B3n_del_Fuego#/media/Archivo:EmblemaFuegoControl.png)

