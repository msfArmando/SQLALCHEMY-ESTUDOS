import kagglehub

# Download latest version
path = kagglehub.dataset_download('luciodias/brazil-oil-production')

print('Path to dataset files:', path)
