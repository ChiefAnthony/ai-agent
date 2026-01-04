import os

from google.genai import types

from config import MAX_CHARS


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir_abs = os.path.abspath(os.path.join(working_dir_abs, directory))

    if os.path.commonpath([working_dir_abs, target_dir_abs]) != working_dir_abs:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir_abs):
        return f'Error: "{directory}" is not a directory'

    try:
        results = []
        for item in os.listdir(target_dir_abs):
            item_path = os.path.join(target_dir_abs, item)

            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            results.append(f"- {item}: size={size} bytes, is_dir={is_dir}")

        return "\n".join(results)

    except Exception as e:
        return f"Error: {str(e)}"


def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_dir_abs, file_path))

    if os.path.commonpath([working_dir_abs, target_abs]) != working_dir_abs:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_abs, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            # Peek to see if there is more data
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return content
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


# class FileManager:
#     def __init__(self, working_directory):
#         self.root = os.path.abspath(working_directory)

#     def _is_safe_path(self, path):
#         """heck if a path is inside the permitted directory."""
#         target_abs = os.path.abspath(os.path.join(self.root, path))
#         return os.path.commonpath([self.root, target_abs]) == self.root, target_abs

#     def get_files_info(self, directory="."):
#         is_safe, target_dir = self._is_safe_path(directory)

#         if not is_safe:
#             return f'Error: "{directory}" is outside the permitted directory'

#         if not os.path.isdir(target_dir):
#             return f'Error: "{directory}" is not a directory'

#         try:
#             results = []
#             for item in os.listdir(target_dir):
#                 item_path = os.path.join(target_dir, item)
#                 size = os.path.getsize(item_path)
#                 is_dir = os.path.isdir(item_path)
#                 results.append(f"- {item}: size={size} bytes, is_dir={is_dir}")
#             return "\n".join(results)
#         except Exception as e:
#             return f"Error: {str(e)}"

#     def get_file_content(self, file_path):
#         is_safe, target_file = self._is_safe_path(file_path)

#         if not is_safe:
#             return f'Error: "{file_path}" is outside the permitted directory'

#         if not os.path.isfile(target_file):
#             return f'Error: File not found: "{file_path}"'

#         try:
#             with open(target_file, "r") as f:
#                 content = f.read(MAX_CHARS)
#                 if f.read(1):
#                     content += (
#                         f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
#                     )
#                 return content
#         except Exception as e:
#             return f"Error: {str(e)}"
