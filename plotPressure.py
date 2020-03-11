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
    nalu_data_dir='/home/users/ryanhass/ME469_FinalProject/datFiles/baseline8'
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
    xcart = np.linspace(-8,8,num=2000)
    ytop = 1.949*np.ones(xcart.shape)
    ybot = -1.049*np.ones(xcart.shape)
    ycent = np.zeros(xcart.shape)
    
    pressTop = ti_p(xcart,ytop)
    pressBot = ti_p(xcart,ybot)
    pressCent = ti_p(xcart,ycent)
    
    plt.figure(figsize=(6,5))
    plt.plot(xcart,pressTop-pressTop[0])
    plt.plot(xcart,pressBot-pressBot[0])
    plt.plot(xcart,pressCent-pressCent[0])
    plt.xlabel('x')
    plt.ylabel('$p-p_i$')
    plt.title('Pressure profiles - Baseline8')
    plt.ylim((-20,20))
    plt.legend(['Top wall','Bottom wall','Center line'])
    plt.savefig('PressureProfiles.png', dpi=300)
    plt.close()

    plt.figure(figsize=(8,4))
    plt.tripcolor(triang, p, shading='gouraud', cmap='jet')
    plt.colorbar()
    plt.axis('image')
    plt.ylim(-1.1,2)
    plt.xlim(-8,8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pressure')
    plt.tight_layout()
    plt.savefig('PressContour.png', dpi=300)
    plt.close()
if __name__=='__main__': main()
