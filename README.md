# About Project

This is a simple task management api for CRUD todo.

## Backend Stack
- Django
- DRF (Djangorestframework)
- Openapi + drf-spectacular (api documentation)


## Running Tests Locally

To ensure a clean environment (especially if `DJANGO_SETTINGS_MODULE` is globally set), run:

**On Unix/macOS:**
```bash
source scripts/unset_env.sh
```

**On Windows (Powershell)**
```sh
.\scripts\unset_env.ps1
```

After that, you can safely run pytest 
```bash
pytest
```