from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.utils.text import slugify


def get_unique_slug(model_instance: object, slugable_field_name: object, slug_field_name: object) -> object:
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    slug = slugify(getattr(model_instance, slugable_field_name))
    unique_slug = slug
    extension = 1
    ModelClass = model_instance.__class__

    while ModelClass._default_manager.filter(
            **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1

    return unique_slug


def handler_class_on_validate(form, valid):
    """The function handles the class of the field when form validated

    Arguments:
        form {[Form]} -- [instance of form]
        valid {[boolean]} -- [True of False]
    """
    fields_error = {field for field in form.errors}
    form_fields = {field for field in form.fields}

    for field_name in form.errors:
        if 'class' in form.fields[field_name].widget.attrs:
            form.fields[field_name].widget.attrs['class'] += ' is-invalid'
        else:
            form.fields[field_name].widget.attrs['class'] = 'is-invalid'

    for field_name in form_fields - fields_error:
        if 'class' in form.fields[field_name].widget.attrs:
            form.fields[field_name].widget.attrs['class'] += ' is-valid'
        else:
            form.fields[field_name].widget.attrs['class'] = 'is-valid'


def login_has_type_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='dang-nhap'):
    '''
    Decorator for views that checks that the logged in user is a user_type,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_active,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
