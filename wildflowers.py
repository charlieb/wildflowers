import flowers as flo
import dla
from math import pi
import svgwrite as svg
import time

def main():
    particle_radius = 1.
    particle_scaler = 0.9995
    nparticles = 3000
    particles = dla.generate_particles(nparticles, particle_radius, particle_scaler, start_angle_range=2*pi)
    leaves = dla.find_leaves(particles)

    npetals = 7
    petal_taper=1.5
    petal_fatness=2.
    flowers = []
    for i in leaves:
        flowers += flo.flower(particles[i][0], particles[i][1], npetals,
                particles[i][2]*1.5, # petal length = particle radius
                particles[i][2]*0.5, # petal width
                petal_taper,
                petal_fatness)

    line_width=0.1
    dwg = svg.Drawing('test.svg')
    dla.draw(particles, dwg, 
            circles=False, links=True, 
            circle_color='brown', link_color='green',
            line_width=line_width*2,
            prune=leaves)
    flo.draw(flowers, dwg, color='blue', line_width=line_width)
    dwg.save()


if __name__ == '__main__':
    t0 = time.time()
    main()
    t1 = time.time()

    print("Elapsed:", t1-t0)

