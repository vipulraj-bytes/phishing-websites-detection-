import importlib
pkgs = [
    ("fastapi", "fastapi"),
    ("uvicorn", "uvicorn"),
    ("pydantic", "pydantic"),
    ("sklearn", "scikit-learn"),
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("shap", "shap"),
    ("xgboost", "xgboost"),
    ("whois", "python-whois"),
    ("requests", "requests"),
    ("joblib", "joblib"),
    ("multipart", "python-multipart"),
]
for mod, pkg in pkgs:
    try:
        m = importlib.import_module(mod)
        print(f"OK   {pkg:<22} {getattr(m, '__version__', 'n/a')}")
    except Exception as e:
        print(f"FAIL {pkg:<22} {e}")
