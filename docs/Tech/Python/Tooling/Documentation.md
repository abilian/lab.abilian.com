To document Python projects, we tend to prefer Markdown to reStructuredText (ReST is more powerful, but less common).

## Tools

### Sphinx

- A robust documentation generator traditionally associated with reST but also supports Markdown with plugins like **MyST-Parser**.
- Excellent for generating static documentation in HTML, PDF, or other formats.
- Integrates well with autodoc modules to extract Python docstrings for API documentation.
- Recommended for larger projects needing cross-references, indices, and advanced formatting.

### Portray

- A minimalist tool for generating project documentation with little configuration.
- Uses Markdown as the primary format and integrates seamlessly with Python projects.
- Auto-generates API documentation based on code and docstrings.
- Suitable for developers seeking a lightweight, quick-to-deploy solution.

### MkDocs

- A Markdown-focused static site generator designed for simplicity and ease of use.
- Features include fast builds, live previews, and minimal setup.
- Ideal for creating beautiful project documentation from Markdown files.

### MkDocs-Material

- A widely used theme/plugin for MkDocs that enhances the design and interactivity of the generated site.
- Provides features like search, responsive design, and rich UI components.
- Highly customizable with built-in support for dark mode, versioning, and navigation.

## Documenting the Python API

### Short Summary

Documenting a Python API involves generating reference material directly from the codebase. This ensures documentation is consistent with the actual implementation and minimizes maintenance overhead. Tools like **Sphinx autodoc**, **pdoc**, and **Doxygen** parse docstrings in Python modules, methods, and functions to create structured and searchable documentation.

**Steps**:

1. **Write Clear Docstrings**: Follow a standard docstring format (e.g., Google, NumPy, or reST).
2. **Automate Documentation**: Use tools like Sphinx with autodoc or pdoc to convert docstrings into HTML or Markdown.
3. **Include Examples**: Add usage examples, edge cases, and sample inputs/outputs to the documentation.

More details: [[Documenting a Python API]].

## Documenting a REST API

Swagger is an industry-standard tool for documenting RESTful APIs. It adheres to the **OpenAPI Specification**, enabling both human-readable and machine-readable documentation. It includes tools like **Swagger UI** for interactive API documentation.

**Key Benefits**:

- **Interactive Documentation**: Users can try out API endpoints directly in the browser.
- **Standardized Format**: OpenAPI Specification ensures compatibility across platforms and tools.
- **Integration with Frameworks**: Most Python web frameworks (or their extensions) support OpenAPI generation.

**Framework-Specific Solutions**:

1. **Django REST Framework (DRF)**:

    - Supports OpenAPI/Swagger documentation using extensions like **drf-yasg** or **django-rest-framework-simplejwt**.
    - Configuration involves specifying serializers, views, and endpoints.
2. **FastAPI**:

    - Provides automatic OpenAPI generation out of the box.
    - Swagger UI and ReDoc are integrated and require minimal configuration.
    - Developers can enrich the API schema with metadata directly from Python type annotations.
3. **Flask**:

    - Extensions like **Flask-RESTPlus** and **Flask-Swagger** provide OpenAPI support.
    - Schemas and endpoint descriptions are declared alongside route definitions.

**Example Configuration for DRF**:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API endpoints for the project.",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

**Recommendations**:

- Use **Swagger UI** or **ReDoc** for interactive documentation.
- Ensure that OpenAPI schemas are versioned and updated with code changes.
- Include examples and authentication details in the API spec for better usability.
