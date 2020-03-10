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
    nalu_data_dir='/home/users/ryanhass/ME469_FinalProject/datFiles/baseline1'
    base_name = 'viscousPump.e'
    filename = nalu_data_dir + '/' + base_name
    dset = nc.Dataset(filename, mode='r')
    x = np.array(dset.variables['coordx'][:])
    y = np.array(dset.variables['coordy'][:])
#    var0 = np.array(dset.variables['vals_nod_var0'][-1])
    var1 = np.array(dset.variables['vals_nod_var1'][-1])
    var2 = np.array(dset.variables['vals_nod_var2'][-1])
    var3 = np.array(dset.variables['vals_nod_var3'][-1])
    var4 = np.array(dset.variables['vals_nod_var4'][-1])
    var5 = np.array(dset.variables['vals_nod_var5'][-1])
    var6 = np.array(dset.variables['vals_nod_var6'][-1])
    var7 = np.array(dset.variables['vals_nod_var7'][-1])
    u = np.array(dset.variables['vals_nod_var8'][-1])
    v = np.array(dset.variables['vals_nod_var9'][-1])

    triang = tri.Triangulation(x, y)
    xtri = x[triang.triangles].mean(axis=1)
    ytri = y[triang.triangles].mean(axis=1)
    triang.set_mask(np.hypot(xtri, ytri) < 1.0)
    ti_u = tri.LinearTriInterpolator(triang, u)
    ti_v = tri.LinearTriInterpolator(triang, v)

    # Find array sizes
    print("Size of triang.x = ", triang.x.shape)
    print("Size of triang.y = ", triang.y.shape)

    print("Size of x = ", x.shape)
    print("Size of y = ", y.shape)

    print("Size of u = ", u.shape)
    print("Size of v = ", v.shape)
    
#    print("triang.x lims:", [triang.x[0], triang.x[-1]])
#    print("triang.y lims:", [triang.y[0], triang.y[-1]])
#    
#    print("triang.x 0 to 155:", [triang.x[0], triang.x[155]])
#    print("triang.y 0 to 155:", [triang.y[0], triang.y[155]])
#    
#    print("triang.x 156 to 179:", triang.x[156:179])
#    print("triang.y 156 to 179:", triang.y[156:179])
    
    print("x lims:", [x[0], x[-1]])
    print("y lims:", [y[0], y[-1]])
    
    print("x 0 to 155:", [x[0], x[155]])
    print("y 0 to 155:", [y[0], y[155]])
    
    print("x 156 to 179:", x[156:179])
    print("y 156 to 179:", y[156:179])
    
#    print("triang.x 179 to 300:", triang.x[179:300])
    
if __name__=='__main__': main()
