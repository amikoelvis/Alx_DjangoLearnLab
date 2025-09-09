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

# Security Best Practices in LibraryProject

## Configured Security Settings

- DEBUG = False (production only)
- ALLOWED_HOSTS restricts domains
- X_FRAME_OPTIONS = "DENY" prevents clickjacking
- SECURE_BROWSER_XSS_FILTER = True enables browser XSS filter
- SECURE_CONTENT_TYPE_NOSNIFF = True prevents MIME-sniffing
- CSRF_COOKIE_SECURE & SESSION_COOKIE_SECURE enforce HTTPS
- HSTS enabled for strict HTTPS usage
- CSP (Content Security Policy) restricts sources for scripts and styles

## CSRF Protection

- All forms include `{% csrf_token %}` to prevent CSRF attacks.

## Safe Data Handling

- Views use Django ORM (no raw SQL).
- Forms (`BookForm`) validate and sanitize user input.

## Content Security Policy

- Configured via django-csp middleware.
- Restricts scripts/styles to trusted sources.

## Testing

- Manually tested with different user roles.
- Verified CSRF token presence in forms.
- Attempted XSS injection in inputs (blocked).
- Attempted SQL injection in search fields (ORM safe).
