import matplotlib.pyplot as plt
import ruptures as rpt


n_samples, dim, sigma = 1000, 3, 4

# generate signal
n_bkps, sigma = 4, 4
signal, bkps = rpt.pw_constant(n_samples, dim, n_bkps, noise_std=sigma)

# detection
algo = rpt.Pelt(model="rbf").fit(signal)
result = algo.predict(pen=10)

# display
rpt.display(signal, bkps, result)
plt.show()