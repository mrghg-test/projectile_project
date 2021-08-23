from numpy import sign


def calculate_acceleration_x(v, k=0.0, mass=1.0):
    '''
    Calculate the acceleration based on combined forces from gravity and 
    air resistance.
    
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
    Returns:
        float : accelaration calculated for this time step
    '''
    force_air = -sign(v)*k*v**2
    a = force_air/mass
    
    return a


def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    '''
    Calculate the acceleration based on combined forces from gravity and 
    air resistance.
    
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2.
            Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a


def update_state(t, x, v, a, dt=0.1):
    '''
    Update each parameter for the next time step.
    
    Args:
        t, x, v, a (float) : 
            time (s), position (m) and velocity (m/s) and acceleration (m/s2) value for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float : Updated values for t, h, v after this time step
    '''
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v


def flying_mass(vx0, vy0, mass=1., k=0.0, dt=0.1):
    '''
    Model a flying mass.
    
    Simulates a projectile trajectory in two dimensions, accounting for air resistance.
    
    Args:
        vx0 (float) : 
            initial velocity (x).
        vy0 (float) : 
            initial velocity (y).
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) :
            Mass of the object. Only needed if k is not 0.
            Default = 1.0  (kg)
        dt (float, optional) : 
            Time interval for each time step in seconds.
            Default = 0.1
    
    Returns:
        list, list, list, list, list : Five lists containing the time, x, y, vx, vy
    '''
    # Fixed input values
    x0 = 0.
    y0 = 0.
    gravity = -9.81 # m/s2

    # Initial values for our parameters
    t0 = 0.0

    # Create empty lists which we will update
    t = []
    x = []
    y = []
    vx = []
    vy = []
    
    # Instantaneous values
    ti = t0
    xi = x0
    yi = y0
    vxi = vx0
    vyi = vy0
    
    # Keep looping while the object is still falling
    while yi >= 0:
        # Evaluate the state of the system - start by calculating the total force on the object
        ax = calculate_acceleration_x(vxi, k=k, mass=mass)
        ay = calculate_acceleration_y(vyi, k=k, mass=mass, gravity=gravity)

        # Append values to list and then update
        t.append(ti)
        x.append(xi)
        y.append(yi)
        vx.append(vxi)
        vy.append(vyi)

        # Update the state for time, x/y and velocity
        ti, xi, vxi = update_state(ti, xi, vxi, ax, dt=dt)
        ti, yi, vyi = update_state(ti, yi, vyi, ay, dt=dt)

    return t, x, y, vx, vy