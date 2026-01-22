"""Utility functions for MCP Midjourney server."""

from typing import Any


def format_imagine_result(data: dict[str, Any]) -> str:
    """Format imagine result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if not data.get("success", False):
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [
        f"Task ID: {data.get('task_id', 'N/A')}",
        f"Image ID: {data.get('image_id', 'N/A')}",
        "",
        f"Image URL: {data.get('image_url', 'N/A')}",
        f"Image Size: {data.get('image_width', 'N/A')}x{data.get('image_height', 'N/A')}",
        "",
        f"Raw Image URL: {data.get('raw_image_url', 'N/A')}",
        f"Raw Image Size: {data.get('raw_image_width', 'N/A')}x{data.get('raw_image_height', 'N/A')}",
        "",
        f"Progress: {data.get('progress', 'N/A')}%",
        "",
    ]

    # Add sub images if available
    sub_images = data.get("sub_image_urls", [])
    if sub_images:
        lines.append("Sub Images:")
        for i, url in enumerate(sub_images, 1):
            lines.append(f"  {i}. {url}")
        lines.append("")

    # Add available actions
    actions = data.get("actions", [])
    if actions:
        lines.append("Available Actions:")
        lines.append(f"  {', '.join(actions)}")
        lines.append("")

    return "\n".join(lines)


def format_describe_result(data: dict[str, Any]) -> str:
    """Format describe result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    descriptions = data.get("descriptions", [])
    if not descriptions:
        return "No descriptions returned."

    lines = ["Image Descriptions:", ""]
    for i, desc in enumerate(descriptions, 1):
        lines.extend([f"--- Option {i} ---", desc, ""])

    return "\n".join(lines)


def format_video_result(data: dict[str, Any]) -> str:
    """Format video generation result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if not data.get("success", False):
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [
        f"Task ID: {data.get('task_id', 'N/A')}",
        f"Video ID: {data.get('video_id', 'N/A')}",
        "",
        f"Cover Image: {data.get('image_url', 'N/A')}",
        f"Cover Size: {data.get('image_width', 'N/A')}x{data.get('image_height', 'N/A')}",
        "",
        f"Progress: {data.get('progress', 'N/A')}%",
        "",
    ]

    # Add video URLs
    video_urls = data.get("video_urls", [])
    if video_urls:
        lines.append("Video URLs:")
        for i, url in enumerate(video_urls, 1):
            lines.append(f"  {i}. {url}")
        lines.append("")

    return "\n".join(lines)


def format_translate_result(data: dict[str, Any]) -> str:
    """Format translate result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    content = data.get("content", "")
    if not content:
        return "No translation returned."

    return f"Translated Content:\n\n{content}"


def format_task_result(data: dict[str, Any]) -> str:
    """Format task query result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    request_info = data.get("request", {})
    response_info = data.get("response", {})

    lines = [
        f"Task ID: {data.get('id', 'N/A')}",
        f"Type: {data.get('type', 'N/A')}",
        f"Created At: {data.get('created_at', 'N/A')}",
        f"Finished At: {data.get('finished_at', 'N/A')}",
        "",
        "Request:",
        f"  Action: {request_info.get('action', 'N/A')}",
        f"  Prompt: {request_info.get('prompt', 'N/A')}",
        f"  Mode: {request_info.get('mode', 'N/A')}",
        "",
    ]

    if response_info.get("success"):
        lines.append("Response: Success")
        lines.append("")

        if "image_url" in response_info:
            lines.extend([
                f"Image ID: {response_info.get('image_id', 'N/A')}",
                f"Image URL: {response_info.get('image_url', 'N/A')}",
                f"Image Size: {response_info.get('image_width', 'N/A')}x{response_info.get('image_height', 'N/A')}",
                "",
            ])

            actions = response_info.get("actions", [])
            if actions:
                lines.append(f"Available Actions: {', '.join(actions)}")
                lines.append("")

        elif "descriptions" in response_info:
            descriptions = response_info.get("descriptions", [])
            lines.append("Descriptions:")
            for i, desc in enumerate(descriptions, 1):
                lines.append(f"  {i}. {desc[:100]}...")
            lines.append("")

    else:
        lines.append(f"Response: {response_info}")

    return "\n".join(lines)


def format_edit_result(data: dict[str, Any]) -> str:
    """Format edit result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if not data.get("success", False):
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [
        f"Task ID: {data.get('task_id', 'N/A')}",
        f"Image ID: {data.get('image_id', 'N/A')}",
        "",
        f"Image URL: {data.get('image_url', 'N/A')}",
        f"Image Size: {data.get('image_width', 'N/A')}x{data.get('image_height', 'N/A')}",
        "",
        f"Raw Image URL: {data.get('raw_image_url', 'N/A')}",
        f"Raw Image Size: {data.get('raw_image_width', 'N/A')}x{data.get('raw_image_height', 'N/A')}",
        "",
        f"Progress: {data.get('progress', 'N/A')}%",
        "",
    ]

    # Add sub images if available
    sub_images = data.get("sub_image_urls", [])
    if sub_images:
        lines.append("Sub Images:")
        for i, url in enumerate(sub_images, 1):
            lines.append(f"  {i}. {url}")
        lines.append("")

    return "\n".join(lines)
