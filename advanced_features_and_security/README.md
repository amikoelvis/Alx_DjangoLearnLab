# Permissions and Groups Setup

## Custom Permissions

Defined in `Book` model (`models.py`):

- can_view
- can_create
- can_edit
- can_delete

## Groups

- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Usage in Views

Views use `@permission_required` decorator, e.g.:

```python
@permission_required("bookshelf.can_edit", raise_exception=True)
```
