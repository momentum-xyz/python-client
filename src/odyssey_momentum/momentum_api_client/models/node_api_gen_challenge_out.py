from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeApiGenChallengeOut")


@attr.s(auto_attribs=True)
class NodeApiGenChallengeOut:
    """
    Attributes:
        challenge (Union[Unset, str]):
    """

    challenge: Unset | str = UNSET
    additional_properties: dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        challenge = self.challenge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge is not UNSET:
            field_dict["challenge"] = challenge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        challenge = d.pop("challenge", UNSET)

        node_api_gen_challenge_out = cls(
            challenge=challenge,
        )

        node_api_gen_challenge_out.additional_properties = d
        return node_api_gen_challenge_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
