from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.entry_attribute_value import EntryAttributeValue


T = TypeVar("T", bound="GetApiV4ObjectsObjectIdAllUsersAttributesResponse200")


@attr.s(auto_attribs=True)
class GetApiV4ObjectsObjectIdAllUsersAttributesResponse200:
    """ """

    additional_properties: dict[str, "EntryAttributeValue"] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.entry_attribute_value import EntryAttributeValue

        d = src_dict.copy()
        get_api_v4_objects_object_id_all_users_attributes_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = EntryAttributeValue.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_api_v4_objects_object_id_all_users_attributes_response_200.additional_properties = additional_properties
        return get_api_v4_objects_object_id_all_users_attributes_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "EntryAttributeValue":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "EntryAttributeValue") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
