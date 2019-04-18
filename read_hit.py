#Sample code that reads Hit file and reconstruct velocities.
#Alberto Vela-Martin, 2017
#
#
#VERSION LOG. Email any comments or bugs to albertovelam@gmail.com
#07/09/2017 - Original script.
#------------------------------------------------------------------------- 


import h5py as h5
from pylab import * 
 
N=1024 #Size of the box in points

Ny=N
Nx=N
Nz=N/2+1

filename='DIRECTORY/hit.1024.00001.h5' #File to read

f = h5.File(filename, 'r')

up= f['u'][:] #Read k_x=0 plane of u
v = f['v'][:] #Read v
w = f['w'][:] #Read w

up.dtype='c8'
v.dtype ='c8'
w.dtype ='c8'

u=zeros((N,N,N//2+1),dtype='c8')

#Fill the k_x=0 plane of u
u[0,:,:]=up;

#Read time, number of file and kinematic viscosity

time   = f['time'][:]
n_file = f['n_file'][:]
nu     = f['nu'][:]

#Generate wave-number vectors kx,ky and kz
k=r_[0:N//2,-N//2:0]
kx=k.reshape((-1, 1, 1))
ky=k.reshape(( 1,-1, 1))
kz=k[0:(N//2+1)].reshape(( 1, 1,-1))

#Reconstruct u
u[1:,...]=((-ky*v-kz*w)/kx)[1:,...]

#Transfor velocities to real space

u=irfftn(u)
v=irfftn(v)
w=irfftn(w)


# Copyright (C) 2017  Alberto Vela-Martin, albertovelam@gmail.com
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
