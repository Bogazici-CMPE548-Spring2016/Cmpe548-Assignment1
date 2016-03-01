__author__ = 'Yasin Almalioglu'

import numpy as np
import matplotlib.pyplot as plt

# Yasin Almalioglu - 2015700018


def sample_from_unit_circle(N):
    """ Q1 """
    # Generate samples from Theta and R
    # By the inversion rule, u=F(r) and r=sqrt(u), u is in [0,1]
    # N=10000 #Number of samples to generate
    r = np.sqrt(np.random.rand(N))
    theta = np.random.rand(N) * 2 * np.pi

    # Convert (r,theta) to cartesian coordinates
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    plt.figure()
    # Plot the sample points
    plt.scatter(x, y)

    # Plot the unit circle
    unit_circle = plt.Circle((0, 0), 1, color='r', fill=False, linewidth=5)
    fig = plt.gcf()
    fig.gca().add_artist(unit_circle)
    # plt.show()

    return x, y


def make_p(p):
    return lambda x, y: np.power((np.power(np.abs(x), p) + np.power(np.abs(y), p)), 1. / p)


def sample_from_square(N):
    ''' Sample from square with length sqrt(2)
    :param N: Number of samples to generate
    :return: Uniform samples within the square
    '''
    x = np.random.rand(N) * np.sqrt(2) - np.sqrt(2) / 2
    y = np.random.rand(N) * np.sqrt(2) - np.sqrt(2) / 2
    return x, y


N = 10000
x, y = sample_from_unit_circle(N)  # Answer the 1. question

M = 1.
for p_norm in [1.5, 0.7]:
    p = make_p(p_norm)
    accepted = p(x, y) < 1

    # Display the acceptance ratio
    print 'Acceptance ratio for p=', p_norm, ': ', float(len(x[accepted])) / N

    # Draw sampled points
    plt.figure()
    plt.title("p=" + str(p_norm) + " norm ball")
    plt.scatter(x[accepted], y[accepted])

    # Draw unit ball of p=2
    unit_circle = plt.Circle((0, 0), 1, color='r', fill=False, linewidth=5)
    fig = plt.gcf()
    fig.gca().add_artist(unit_circle)

# More efficient sampling for p=0.7
# Sample from square with length sqrt(2) and rotate the sampled points 45 degrees
# anti-clockwise to get 1-norm unit ball
x, y = sample_from_square(N)
eff_samples = np.vstack((x, y))
angle = 45.
theta = (angle / 180.) * np.pi

rotMatrix = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
one_norm_unit_ball = np.dot(rotMatrix, eff_samples)
x = one_norm_unit_ball[0, :]
y = one_norm_unit_ball[1, :]

accepted = p(x, y) < 1

# Display the acceptance ratio
print 'Acceptance ratio for p=', p_norm, '(More efficient): ', float(len(x[accepted])) / N

# Draw sampled points
plt.figure()
plt.title("p=" + str(p_norm) + " norm ball")
plt.scatter(x[accepted], y[accepted])

plt.show()


# Bonus part
def sample_from_nd_hypercube(N, nd):
    '''
    :param N: Number of samples to generate
    :param nd: Dimensionality of hypercube
    :return: nd dimensional uniform sample points
    '''
    return np.random.rand(nd, N)*2-1


def nd_2_norm(x, nd):
    '''
    :param x: nd dimensional sample points
    :param nd: dimensionality of sample points
    :return: 2-norm of sample points
    '''
    sum=0
    for i in range(nd):
        sum += np.square(x[i,:])
    return np.sqrt(sum)

# Calculate acceptance ratios for the bonus part
for nd in range(3,6):
    x = sample_from_nd_hypercube(N, nd)
    accepted = nd_2_norm(x, nd) < 1
    # Display the acceptance ratio
    print 'Acceptance ratio for bonus part(dim=', nd, '): ', float(len(x[0,accepted])) / N
