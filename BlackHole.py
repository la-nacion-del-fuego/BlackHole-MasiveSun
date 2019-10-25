#!/usr/bin/env python3
#
# n-body.py Solve the n-body problem using Newton
#
# Copyright (C) 2019  Victor De la Luz (vdelaluz@enesmorelia.unam.mx)
#                      
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

G=6.674e-11         #m^3kg^-1s^-2

class Particle:
   
    def __init__(self, p, v, m, dt=1):
        self.p = p #position distance in Parsecs
        self.v = v #velocity
        self.m = m #mass 
        self.dt = dt
        self.trajectory = [p]
        self.time = [0.0]

    def setdt(self,dt):
        self.dt = dt

    def computeR(self,p1):
        r = math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2)
        return r

    def computeU(self,p1):
        u=[0,0,0]
        i=0
        for a,b in zip(self.p,p1):
            u[i] = b - a
            i+=1
        return u
   
    def integrate(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]

       
        self.v[0] += Vx
        self.v[1] += Vy
        self.v[2] += Vz
       
        self.p = [self.p[0]+ (self.v[0]) *dt,self.p[1]+ (self.v[1])*dt,self.p[2]+ (self.v[2])*dt]

    def getPosition(self):
        return self.p

    def getVelocity(self):
        return self.v

    def getKineticEnergy(self):
        k= (1/2)*self.m*(math.sqrt( self.v[0]^2 +self.v[1]^2+self.v[2]^2))
        return k    

    def computeV(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]

        return [Vx,Vy,Vz]

    def updateV(self,v):
        self.v[0] += v[0]
        self.v[1] += v[1]
        self.v[2] += v[2]

    def updatePosition(self,time,save):        
        self.p = [self.p[0]+(self.v[0])*dt, self.p[1]+(self.v[1])*dt, self.p[2]+(self.v[2])*dt]
        if save:
            self.time.append(time)
            self.trajectory.append(self.p)
        
        #self.reduceMass(4.594781899714635140644109253974)

    def getTrajectory(self):
        return self.time, self.trajectory

    def updateMass(self,Particle1:"bhole",Particle2:"Canis"):
        distance = math.sqrt( math.pow(Particle2.p[0]-Particle1.p[0],2) + math.pow(Particle2.p[1] - Particle1.p[1],2) + math.pow(Particle2.p[2]-Particle1.p[2],2))
        
        if distance <= 3.2e10: # <--- intentar buscar la buena
            Particle1.m = Particle1.m + 4.4452577e+21
            Particle2.m = Particle2.m - 4.4452577e+21

        return Particle1.m,Particle2.m


class Potential:
   
    def __init__(self, system, dt):
        self.system = system #set of Particles
        self.dt = dt #set of Particles

    def integrate(self,time,save):
        for i,particle in enumerate(self.system):
            for other in self.system:
                if other != particle:
                    if(i == 0):
                        m1,m2 = other.updateMass(particle,other)
                        self.system[0].m = m1
                        self.system[1].m = m2
                        #print(m1,self.system[0].m)
                        mass_Sagitario.append(self.system[0].m)
                        mass_Canis.append(self.system[1].m)
                    velocity = particle.computeV(other)
                    particle.updateV(velocity)
        for particle in self.system:
            particle.updatePosition(time,save)
            

        return self.system

lenTime = 450000 # 1 -> 100 años 
#lenTime = 900000
dt=10.0  #años

bhole=Particle([0.0, 0.0, 0.0] ,[0.0, 0.0, 0.0],7.359e30) # posicion[km],v[km/años],m[MasaSolar]: El agujero negro tiene una masa solar de 3.7masasSolares == (7.259x10^30)kg
Canis = Particle([20e8, 0.0, 0.0] ,[0.0, 5e5, 0.0],33.813e30) # posicion[km],v[km/años],m[MasaSolar]: La estrella Canis tiene una masa solar de 17masasSolares == (33.813x10^30)kg

n_steps = int(lenTime/dt)


particles = [bhole, Canis]
twoBody = Potential(particles,dt)

x=[]
y=[]

mass_Sagitario = [7.359e30]
mass_Canis = [33.813e30]

skip = 0
save = False
for t in range(1,n_steps):
    if skip == 10:
        skip = 0 
        save = True
    
    system = twoBody.integrate(float(t)*dt,save)
    save = False
    skip += 1
   



fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

i=0
c = ["black","cyan"]
for particle in particles:
    time, trajectory = particle.getTrajectory()
    for x, y in zip(time,trajectory):
        ax.scatter(y[0], y[1], y[2], marker='o',c=c[i])
        #ax.scatter(y[0], y[1], y[2], c=c[i])
    i=i+1


plt.show()

fig, axs = plt.subplots(2, 1, figsize=(6, 8),
                        constrained_layout=True)

ax = axs[0]
ax.plot([i for i in range(len(mass_Sagitario))], mass_Sagitario)
ax.set_xscale('log')
ax.set_title('Aumento de Masa en Sagitario')
ax.grid(True)

ax = axs[1]
ax.plot([i for i in range(len(mass_Canis))], mass_Canis)
ax.set_xscale('log')
ax.set_title('Disminucion de Masa en Canis')
ax.grid(True)
plt.show()