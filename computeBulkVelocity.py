# ME344 NALU Visualization Code
# Hang Song (songhang@stanford.edu)
# Summer 2019
import numpy as np
import netCDF4 as nc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.tri    as tri

def main():
    nalu_data_dir='/home/users/ryanhass/ME469_FinalProject/datFiles/baseline9'
    base_name = 'viscousPump.e'
    filename = nalu_data_dir + '/' + base_name
    dset = nc.Dataset(filename, mode='r')
    x = np.array(dset.variables['coordx'][:])
    y = np.array(dset.variables['coordy'][:])
    p = np.array(dset.variables['vals_nod_var7'][-1])
    u = np.array(dset.variables['vals_nod_var8'][-1])
    v = np.array(dset.variables['vals_nod_var9'][-1])

    triang = tri.Triangulation(x, y)
    xtri = x[triang.triangles].mean(axis=1)
    ytri = y[triang.triangles].mean(axis=1)
    triang.set_mask(np.hypot(xtri, ytri) < 1.0)
    ti_u = tri.LinearTriInterpolator(triang, u)
    ti_v = tri.LinearTriInterpolator(triang, v)
    ti_p = tri.LinearTriInterpolator(triang, p)
    
    # Create cartesian mesh
    ycart = np.linspace(-1.05,1.95,num=2000)
    xIn = -7.9*np.ones(ycart.shape)
    xOut = 7.9*np.ones(ycart.shape)
    
    uIn = ti_u(xIn,ycart)
    uOut = ti_u(xOut,ycart)
 
    umax = np.max(uIn)
    print("max u at inlet = ", umax)
 
    ubulkIn = np.trapz(uIn,ycart)/(ycart[-1]-ycart[0])
    ubulkOut = np.trapz(uOut,ycart)/(ycart[-1]-ycart[0])
    QIn = np.trapz(uIn,ycart)
    QOut = np.trapz(uOut,ycart)

    print("Bulk velocity at inlet = ", ubulkIn)
    print("Bulk velocity at outlet = ", ubulkOut)
    print("Inlet flow rate = ", QIn)
    print("Outlet flow rate = ", QOut)
   
    plt.figure(figsize=(8,4))
    plt.plot(uIn,ycart)
    plt.savefig('uInlet.png')
     
if __name__=='__main__': main()
