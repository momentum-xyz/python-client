from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_http_error import ApiHTTPError
from ...models.dto_object_sub_options import DtoObjectSubOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    client: Client,
    effective: Unset | None | bool = UNSET,
    sub_option_key: str,
) -> dict[str, Any]:
    url = f"{client.base_url}/api/v4/objects/{object_id}/options/sub"

    headers: dict[str, str] = client.get_headers()
    cookies: dict[str, Any] = client.get_cookies()

    params: dict[str, Any] = {}
    params["effective"] = effective

    params["subOptionKey"] = sub_option_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> ApiHTTPError | DtoObjectSubOptions | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = DtoObjectSubOptions.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiHTTPError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiHTTPError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiHTTPError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiHTTPError | DtoObjectSubOptions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: Client,
    effective: Unset | None | bool = UNSET,
    sub_option_key: str,
) -> Response[ApiHTTPError | DtoObjectSubOptions]:
    """Get object sub options

     Returns a object sub options based on query

    Args:
        object_id (str):
        effective (Union[Unset, None, bool]):
        sub_option_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiHTTPError, DtoObjectSubOptions]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        client=client,
        effective=effective,
        sub_option_key=sub_option_key,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: str,
    *,
    client: Client,
    effective: Unset | None | bool = UNSET,
    sub_option_key: str,
) -> ApiHTTPError | DtoObjectSubOptions | None:
    """Get object sub options

     Returns a object sub options based on query

    Args:
        object_id (str):
        effective (Union[Unset, None, bool]):
        sub_option_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiHTTPError, DtoObjectSubOptions]
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        effective=effective,
        sub_option_key=sub_option_key,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: Client,
    effective: Unset | None | bool = UNSET,
    sub_option_key: str,
) -> Response[ApiHTTPError | DtoObjectSubOptions]:
    """Get object sub options

     Returns a object sub options based on query

    Args:
        object_id (str):
        effective (Union[Unset, None, bool]):
        sub_option_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiHTTPError, DtoObjectSubOptions]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        client=client,
        effective=effective,
        sub_option_key=sub_option_key,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: Client,
    effective: Unset | None | bool = UNSET,
    sub_option_key: str,
) -> ApiHTTPError | DtoObjectSubOptions | None:
    """Get object sub options

     Returns a object sub options based on query

    Args:
        object_id (str):
        effective (Union[Unset, None, bool]):
        sub_option_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiHTTPError, DtoObjectSubOptions]
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            effective=effective,
            sub_option_key=sub_option_key,
        )
    ).parsed
