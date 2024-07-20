# Interpolation Analysis Project

## Overview
This project focuses on analyzing the impact of added noise on data for Lagrange and cubic spline interpolations. The provided scripts handle data processing, noise addition, and visualization of interpolation results.

## Functions

### Lagrange Interpolation
The Lagrange interpolation functions are used to interpolate data points based on the Lagrange polynomial formula.

- `calculate_lagrange_basis(x_points, idx, target_x, result=1)`: Calculates the basis polynomial for Lagrange interpolation.
- `interpolate_lagrange(x_points, y_points, target_x, interpolated_value=0)`: Interpolates a single point using the Lagrange method.
- `generate_interpolated_lagrange(x_points, y_points, total_points)`: Generates interpolated points using Lagrange interpolation.

### Cubic Spline Interpolation
Cubic spline interpolation functions calculate the coefficients for cubic spline interpolation and generate interpolated data points.

- `calculate_spline_coefficients(x_coords, y_coords)`: Calculates spline coefficients.
- `spline_interpolation(x_coords, y_coords, num_intervals)`: Interpolates data points using cubic splines.

### Helper Functions
- `nodes_select(data, count)`: Selects nodes for interpolation based on quantiles.
- `add_noise(y_values, noise_level)`: Adds noise to the data.
- `plot_results(x, y, x_nodes, y_nodes, x_interp, y_interp, method, filename)`: Plots the original data, interpolation nodes, and interpolated curve.

## Analysis
The analysis script `analyze_file` processes the input data, performs both Lagrange and cubic spline interpolations, adds noise to the data, and visualizes the results.
