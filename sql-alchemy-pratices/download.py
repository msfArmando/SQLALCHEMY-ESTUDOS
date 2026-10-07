from kagglehub import kagglehub  # type: ignore[import-untyped]

# Download latest version
path = kagglehub.dataset_download(
    'akrambelha/synthetic-banking-dataset-csv-sql-sqlite'
)

print('Path to dataset files:', path)
