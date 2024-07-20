import pandas as pd
from interpolation import generate_interpolated_lagrange, spline_interpolation
from helpers import nodes_select, add_noise, plot_results, node_counts, noise_level

def analyze_file(filename, sep, prefix):
    data = pd.read_csv(filename, sep=sep, header=None)
    data.columns = ['Dystans', 'Wysokość']

    for count in node_counts:
        x_subset, y_subset = nodes_select(data, count)

        x_lagrange, y_lagrange = generate_interpolated_lagrange(x_subset, y_subset, 500)
        plot_results(data['Dystans'], data['Wysokość'], x_subset, y_subset, x_lagrange, y_lagrange, 'Lagrange Interpolation', f'{prefix}_lagrange_{count}_nodes.png')

        x_spline, y_spline = spline_interpolation(x_subset, y_subset, 50)
        plot_results(data['Dystans'], data['Wysokość'], x_subset, y_subset, x_spline, y_spline, 'Cubic Splines Interpolation', f'{prefix}_splines_{count}_nodes.png')

    for count in node_counts:
        x_subset, y_subset = nodes_select(data, count)
        y_subset_noisy = add_noise(y_subset, noise_level)

        x_lagrange_noisy, y_lagrange_noisy = generate_interpolated_lagrange(x_subset, y_subset_noisy, 500)
        plot_results(data['Dystans'], data['Wysokość'], x_subset, y_subset_noisy, x_lagrange_noisy, y_lagrange_noisy, 'Lagrange Interpolation z szumami', f'{prefix}_lagrange_noise_{count}_nodes.png')

        x_spline_noisy, y_spline_noisy = spline_interpolation(x_subset, y_subset_noisy, 50)
        plot_results(data['Dystans'], data['Wysokość'], x_subset, y_subset_noisy, x_spline_noisy, y_spline_noisy, 'Cubic Splines Interpolation z szumami', f'{prefix}_splines_noise_{count}_nodes.png')
