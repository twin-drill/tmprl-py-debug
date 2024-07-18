"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AccountAccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    role: builtins.str
    """The role on the account, should be one of [admin, developer, read]
    admin - gives full access the account, including users and namespaces
    developer - gives access to create namespaces on the account
    read - gives read only access to the account
    """
    def __init__(
        self,
        *,
        role: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["role", b"role"]
    ) -> None: ...

global___AccountAccess = AccountAccess

class NamespaceAccess(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERMISSION_FIELD_NUMBER: builtins.int
    permission: builtins.str
    """The permission to the namespace, should be one of [admin, write, read]
    admin - gives full access to the namespace, including assigning namespace access to other users
    write - gives write access to the namespace configuration and workflows within the namespace
    read - gives read only access to the namespace configuration and workflows within the namespace
    """
    def __init__(
        self,
        *,
        permission: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["permission", b"permission"]
    ) -> None: ...

global___NamespaceAccess = NamespaceAccess

class Access(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class NamespaceAccessesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___NamespaceAccess: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___NamespaceAccess | None = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...

    ACCOUNT_ACCESS_FIELD_NUMBER: builtins.int
    NAMESPACE_ACCESSES_FIELD_NUMBER: builtins.int
    @property
    def account_access(self) -> global___AccountAccess:
        """The account access"""
    @property
    def namespace_accesses(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        builtins.str, global___NamespaceAccess
    ]:
        """The map of namespace accesses
        The key is the namespace name and the value is the access to the namespace
        """
    def __init__(
        self,
        *,
        account_access: global___AccountAccess | None = ...,
        namespace_accesses: collections.abc.Mapping[
            builtins.str, global___NamespaceAccess
        ]
        | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["account_access", b"account_access"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "account_access",
            b"account_access",
            "namespace_accesses",
            b"namespace_accesses",
        ],
    ) -> None: ...

global___Access = Access

class UserSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EMAIL_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    email: builtins.str
    """The email address associated to the user"""
    @property
    def access(self) -> global___Access:
        """The access to assigned to the user"""
    def __init__(
        self,
        *,
        email: builtins.str = ...,
        access: global___Access | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["access", b"access"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["access", b"access", "email", b"email"],
    ) -> None: ...

global___UserSpec = UserSpec

class Invitation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATED_TIME_FIELD_NUMBER: builtins.int
    EXPIRED_TIME_FIELD_NUMBER: builtins.int
    @property
    def created_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the user was created"""
    @property
    def expired_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the invitation expires or has expired"""
    def __init__(
        self,
        *,
        created_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        expired_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "created_time", b"created_time", "expired_time", b"expired_time"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "created_time", b"created_time", "expired_time", b"expired_time"
        ],
    ) -> None: ...

global___Invitation = Invitation

class User(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    RESOURCE_VERSION_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ASYNC_OPERATION_ID_FIELD_NUMBER: builtins.int
    INVITATION_FIELD_NUMBER: builtins.int
    CREATED_TIME_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_TIME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """The id of the user"""
    resource_version: builtins.str
    """The current version of the user specification
    The next update operation will have to include this version
    """
    @property
    def spec(self) -> global___UserSpec:
        """The user specification"""
    state: builtins.str
    """The current state of the user"""
    async_operation_id: builtins.str
    """The id of the async operation that is creating/updating/deleting the user, if any"""
    @property
    def invitation(self) -> global___Invitation:
        """The details of the open invitation sent to the user, if any"""
    @property
    def created_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the user was created"""
    @property
    def last_modified_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the user was last modified
        Will not be set if the user has never been modified
        """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        resource_version: builtins.str = ...,
        spec: global___UserSpec | None = ...,
        state: builtins.str = ...,
        async_operation_id: builtins.str = ...,
        invitation: global___Invitation | None = ...,
        created_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "created_time",
            b"created_time",
            "invitation",
            b"invitation",
            "last_modified_time",
            b"last_modified_time",
            "spec",
            b"spec",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "async_operation_id",
            b"async_operation_id",
            "created_time",
            b"created_time",
            "id",
            b"id",
            "invitation",
            b"invitation",
            "last_modified_time",
            b"last_modified_time",
            "resource_version",
            b"resource_version",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> None: ...

global___User = User

class UserGroupSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the group as defined in the customer's IdP (e.g. Google group name in Google Workspace)
    The name is immutable. Once set, it cannot be changed
    """
    @property
    def access(self) -> global___Access:
        """The access assigned to the group"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        access: global___Access | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["access", b"access"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["access", b"access", "name", b"name"],
    ) -> None: ...

global___UserGroupSpec = UserGroupSpec

class UserGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    RESOURCE_VERSION_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ASYNC_OPERATION_ID_FIELD_NUMBER: builtins.int
    CREATED_TIME_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_TIME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """The id of the group"""
    resource_version: builtins.str
    """The current version of the group specification
    The next update operation will have to include this version
    """
    @property
    def spec(self) -> global___UserGroupSpec:
        """The group specification"""
    state: builtins.str
    """The current state of the group"""
    async_operation_id: builtins.str
    """The id of the async operation that is creating/updating/deleting the group, if any"""
    @property
    def created_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the group was created"""
    @property
    def last_modified_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the group was last modified
        Will not be set if the group has never been modified
        """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        resource_version: builtins.str = ...,
        spec: global___UserGroupSpec | None = ...,
        state: builtins.str = ...,
        async_operation_id: builtins.str = ...,
        created_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "created_time",
            b"created_time",
            "last_modified_time",
            b"last_modified_time",
            "spec",
            b"spec",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "async_operation_id",
            b"async_operation_id",
            "created_time",
            b"created_time",
            "id",
            b"id",
            "last_modified_time",
            b"last_modified_time",
            "resource_version",
            b"resource_version",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> None: ...

global___UserGroup = UserGroup

class ServiceAccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    RESOURCE_VERSION_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ASYNC_OPERATION_ID_FIELD_NUMBER: builtins.int
    CREATED_TIME_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_TIME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """The id of the service account."""
    resource_version: builtins.str
    """The current version of the service account specification.
    The next update operation will have to include this version.
    """
    @property
    def spec(self) -> global___ServiceAccountSpec:
        """The service account specification."""
    state: builtins.str
    """The current state of the service account.
    Possible values: activating, activationfailed, active, updating, updatefailed, deleting, deletefailed, deleted, suspending, suspendfailed, suspended.
    For any failed state, reach out to Temporal Cloud support for remediation.
    """
    async_operation_id: builtins.str
    """The id of the async operation that is creating/updating/deleting the service account, if any."""
    @property
    def created_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the service account was created."""
    @property
    def last_modified_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the service account was last modified
        Will not be set if the service account has never been modified.
        """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        resource_version: builtins.str = ...,
        spec: global___ServiceAccountSpec | None = ...,
        state: builtins.str = ...,
        async_operation_id: builtins.str = ...,
        created_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "created_time",
            b"created_time",
            "last_modified_time",
            b"last_modified_time",
            "spec",
            b"spec",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "async_operation_id",
            b"async_operation_id",
            "created_time",
            b"created_time",
            "id",
            b"id",
            "last_modified_time",
            b"last_modified_time",
            "resource_version",
            b"resource_version",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> None: ...

global___ServiceAccount = ServiceAccount

class ServiceAccountSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name associated with the service account.
    The name is mutable, but must be unique across all your active service accounts.
    """
    @property
    def access(self) -> global___Access:
        """The access assigned to the service account.
        The access is mutable.
        """
    description: builtins.str
    """The description associated with the service account - optional.
    The description is mutable.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        access: global___Access | None = ...,
        description: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["access", b"access"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "access", b"access", "description", b"description", "name", b"name"
        ],
    ) -> None: ...

global___ServiceAccountSpec = ServiceAccountSpec

class ApiKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    RESOURCE_VERSION_FIELD_NUMBER: builtins.int
    SPEC_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ASYNC_OPERATION_ID_FIELD_NUMBER: builtins.int
    CREATED_TIME_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_TIME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """The id of the API Key."""
    resource_version: builtins.str
    """The current version of the API key specification.
    The next update operation will have to include this version.
    """
    @property
    def spec(self) -> global___ApiKeySpec:
        """The API key specification."""
    state: builtins.str
    """The current state of the API key.
    Possible values: activating, activationfailed, active, updating, updatefailed, deleting, deletefailed, deleted, suspending, suspendfailed, suspended.
    For any failed state, reach out to Temporal Cloud support for remediation.
    """
    async_operation_id: builtins.str
    """The id of the async operation that is creating/updating/deleting the API key, if any."""
    @property
    def created_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the API key was created."""
    @property
    def last_modified_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time when the API key was last modified.
        Will not be set if the API key has never been modified.
        """
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        resource_version: builtins.str = ...,
        spec: global___ApiKeySpec | None = ...,
        state: builtins.str = ...,
        async_operation_id: builtins.str = ...,
        created_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "created_time",
            b"created_time",
            "last_modified_time",
            b"last_modified_time",
            "spec",
            b"spec",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "async_operation_id",
            b"async_operation_id",
            "created_time",
            b"created_time",
            "id",
            b"id",
            "last_modified_time",
            b"last_modified_time",
            "resource_version",
            b"resource_version",
            "spec",
            b"spec",
            "state",
            b"state",
        ],
    ) -> None: ...

global___ApiKey = ApiKey

class ApiKeySpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OWNER_ID_FIELD_NUMBER: builtins.int
    OWNER_TYPE_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    EXPIRY_TIME_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    owner_id: builtins.str
    """The id of the owner to create the API key for.
    The owner id is immutable. Once set during creation, it cannot be changed.
    The owner id is the id of the user when the owner type is 'user'.
    The owner id is the id of the service account when the owner type is 'service-account'.
    """
    owner_type: builtins.str
    """The type of the owner to create the API key for.
    The owner type is immutable. Once set during creation, it cannot be changed.
    Possible values: user, service-account.
    """
    display_name: builtins.str
    """The display name of the API key."""
    description: builtins.str
    """The description of the API key."""
    @property
    def expiry_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The expiry time of the API key."""
    disabled: builtins.bool
    """True if the API key is disabled."""
    def __init__(
        self,
        *,
        owner_id: builtins.str = ...,
        owner_type: builtins.str = ...,
        display_name: builtins.str = ...,
        description: builtins.str = ...,
        expiry_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        disabled: builtins.bool = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["expiry_time", b"expiry_time"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "description",
            b"description",
            "disabled",
            b"disabled",
            "display_name",
            b"display_name",
            "expiry_time",
            b"expiry_time",
            "owner_id",
            b"owner_id",
            "owner_type",
            b"owner_type",
        ],
    ) -> None: ...

global___ApiKeySpec = ApiKeySpec