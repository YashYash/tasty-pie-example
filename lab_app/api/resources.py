from django.conf import settings
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.bundle import Bundle
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, CharField, ToOneField
from tastypie.resources import ModelResource, Resource
from lab_app.api import fields
from lab_app.api.authorization import UserObjectsOnlyAuthorization
from lab_app.models import Media





class MediaResource(ModelResource):
    class Meta:
        queryset = Media.objects.all()
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()


class UserResource(ModelResource):
    media = ToOneField(MediaResource, 'media', full=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = UserObjectsOnlyAuthorization()
        authentication = BasicAuthentication()


######################
# Non-Model Resource #
######################

class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)