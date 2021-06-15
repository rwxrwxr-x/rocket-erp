from django.db.models.fields.related import ForeignKey


def get_fk_by_instance(instance, postfix='_id'):
    """Get foreign key name of instance."""
    fields = instance._meta.fields
    for x in fields:
        if isinstance(x, ForeignKey):
            return x.name + postfix


def get_model(instance):
    """Get model by instance."""
    return instance._meta.model
