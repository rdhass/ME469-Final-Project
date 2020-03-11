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
    nalu_data_dir='/home/users/ryanhass/ME469_FinalProject/datFiles/baseline7'
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
    ytop = 1.01*np.ones(xcart.shape)
    ybot = -1.01*np.ones(xcart.shape)
    ycent = np.zeros(xcart.shape)
    
    uVelTop = ti_u(xcart,ytop)
    uVelBot = ti_u(xcart,ybot)
    uVelCent = ti_u(xcart,ycent)
    
    vVelTop = ti_v(xcart,ytop)
    vVelBot = ti_v(xcart,ybot)
    vVelCent = ti_v(xcart,ycent)
    
    plt.figure(figsize=(8,4))
    plt.plot(xcart,uVelTop)
    plt.plot(xcart,uVelBot)
    plt.plot(xcart,uVelCent)
    plt.xlabel('x')
    plt.ylabel('$u$-velocity')
    plt.title('$u$-velocity profiles - Baseline7')
    plt.legend(['Top of cylinder','Bottom of cylinder','Center line'])
    plt.savefig('uVelProfiles.png', dpi=300)
    plt.close()

    plt.figure(figsize=(8,4))
    plt.plot(xcart,vVelTop)
    plt.plot(xcart,vVelBot)
    plt.plot(xcart,vVelCent)
    plt.xlabel('x')
    plt.ylabel('$v$-velocity')
    plt.title('$v$-velocity profiles - Baseline7')
    plt.legend(['Top of cylinder','Bottom of cylinder','Center line'])
    plt.savefig('vVelProfiles.png', dpi=300)
    plt.close()
    
    plt.figure(figsize=(8,4))
    plt.tripcolor(triang, v, shading='gouraud', cmap='jet')
    plt.colorbar()
    plt.axis('image')
    plt.ylim(-1.1,2)
    plt.xlim(-8,8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('v-velocity')
    plt.tight_layout()
    plt.savefig('vvelocity.png', dpi=300)
    plt.close()

    plt.figure(figsize=(8,4))
    plt.tripcolor(triang, u, shading='gouraud', cmap='jet')
    plt.colorbar()
    plt.axis('image')
    plt.ylim(-1.1,2)
    plt.xlim(-8,8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('u-velocity')
    plt.tight_layout()
    plt.savefig('uvelocity.png', dpi=300)
    plt.close()
if __name__=='__main__': main()
