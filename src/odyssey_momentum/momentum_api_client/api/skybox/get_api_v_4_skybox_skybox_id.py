from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_http_error import ApiHTTPError
from ...types import Response


def _get_kwargs(
    skybox_id: str,
    *,
    client: Client,
) -> dict[str, Any]:
    url = f"{client.base_url}/api/v4/skybox/{skybox_id}"

    headers: dict[str, str] = client.get_headers()
    cookies: dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Any | ApiHTTPError | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiHTTPError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiHTTPError.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any | ApiHTTPError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    skybox_id: str,
    *,
    client: Client,
) -> Response[Any | ApiHTTPError]:
    """Get skybox image by ID

     Return Get skybox image by ID

    Args:
        skybox_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiHTTPError]]
    """

    kwargs = _get_kwargs(
        skybox_id=skybox_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    skybox_id: str,
    *,
    client: Client,
) -> Any | ApiHTTPError | None:
    """Get skybox image by ID

     Return Get skybox image by ID

    Args:
        skybox_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiHTTPError]
    """

    return sync_detailed(
        skybox_id=skybox_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    skybox_id: str,
    *,
    client: Client,
) -> Response[Any | ApiHTTPError]:
    """Get skybox image by ID

     Return Get skybox image by ID

    Args:
        skybox_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiHTTPError]]
    """

    kwargs = _get_kwargs(
        skybox_id=skybox_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    skybox_id: str,
    *,
    client: Client,
) -> Any | ApiHTTPError | None:
    """Get skybox image by ID

     Return Get skybox image by ID

    Args:
        skybox_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiHTTPError]
    """

    return (
        await asyncio_detailed(
            skybox_id=skybox_id,
            client=client,
        )
    ).parsed