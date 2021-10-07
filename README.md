# analyze-sit

Datasets used in the Matatika SITs.

## development

pip ignores package_data, during development we need to 

```console
    python3 setup.py sdist
```

update the pip_url in your discovery.yml

```
    pip_url: [full path]/analyze-sit/dist/files-matatika-sit-datasets-0.1.0.tar.gz
```