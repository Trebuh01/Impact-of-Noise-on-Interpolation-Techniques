def compute_alpha_values(x_coords, y_coords, interval_lengths):
    num_points = len(x_coords)
    alpha_values = [0] * num_points
    for idx in range(1, num_points - 1):
        alpha_values[idx] = (3 / interval_lengths[idx] * (y_coords[idx + 1] - y_coords[idx]) - 3 / interval_lengths[idx - 1] * (y_coords[idx] - y_coords[idx - 1]))
    return alpha_values

def compute_l_mu_z_values(x_coords, interval_lengths, alpha_values):
    num_points = len(x_coords)
    mu_values = [0] * num_points
    l_values = [1] * num_points
    z_values = [0] * num_points
    for idx in range(1, num_points - 1):
        l_values[idx] = 2 * (x_coords[idx + 1] - x_coords[idx - 1]) - interval_lengths[idx - 1] * mu_values[idx - 1]
        mu_values[idx] = interval_lengths[idx] / l_values[idx]
        z_values[idx] = (alpha_values[idx] - interval_lengths[idx - 1] * z_values[idx - 1]) / l_values[idx]
    return l_values, mu_values, z_values

def compute_coefficients(x_coords, y_coords, interval_lengths, l_values, mu_values, z_values):
    a_coeffs = y_coords.copy()
    num_points = len(x_coords)
    c_coeffs = [0] * num_points
    b_coeffs = [0] * (num_points - 1)
    d_coeffs = [0] * (num_points - 1)
    l_values[-1] = 1
    z_values[-1] = 0

    for idx in range(num_points - 2, -1, -1):
        c_coeffs[idx] = z_values[idx] - mu_values[idx] * c_coeffs[idx + 1]
        b_coeffs[idx] = (a_coeffs[idx + 1] - a_coeffs[idx]) / interval_lengths[idx] - interval_lengths[idx] * (c_coeffs[idx + 1] + 2 * c_coeffs[idx]) / 3
        d_coeffs[idx] = (c_coeffs[idx + 1] - c_coeffs[idx]) / (3 * interval_lengths[idx])
    return a_coeffs, b_coeffs, c_coeffs, d_coeffs

def calculate_spline_coefficients(x_coords, y_coords):
    interval_lengths = [x_coords[i + 1] - x_coords[i] for i in range(len(x_coords) - 1)]
    alpha_values = compute_alpha_values(x_coords, y_coords, interval_lengths)
    l_values, mu_values, z_values = compute_l_mu_z_values(x_coords, interval_lengths, alpha_values)
    return compute_coefficients(x_coords, y_coords, interval_lengths, l_values, mu_values, z_values)

def spline_interpolation(x_coords, y_coords, num_intervals):
    a, b, c, d = calculate_spline_coefficients(x_coords, y_coords)
    interpolated_x = []
    interpolated_y = []
    for i in range(len(x_coords) - 1):
        x_interval = [x_coords[i] + step * (x_coords[i + 1] - x_coords[i]) / (num_intervals - 1) for step in range(num_intervals)]
        interpolated_x.extend(x_interval)
        for x in x_interval:
            delta_x = x - x_coords[i]
            y = a[i] + b[i] * delta_x + c[i] * delta_x**2 + d[i] * delta_x**3
            interpolated_y.append(y)
    return interpolated_x, interpolated_y

    return interpolated_x, interpolated_y

def calculate_lagrange_basis(x_points, idx, target_x, result = 1):
    for k in range(len(x_points)):
        if k != idx:
            result *= (target_x - x_points[k]) / (x_points[idx] - x_points[k])
    return result

def interpolate_lagrange(x_points, y_points, target_x,interpolated_value = 0):
    for idx, y_val in enumerate(y_points):
        interpolated_value += y_val * calculate_lagrange_basis(x_points, idx, target_x)
    return interpolated_value

def generate_interpolated_lagrange(x_points, y_points, total_points):
    x_generated = [x_points[0] + n * (x_points[-1] - x_points[0]) / (total_points - 1) for n in range(total_points)]
    y_generated = [interpolate_lagrange(x_points, y_points, x) for x in x_generated]
    return x_generated, y_generated



