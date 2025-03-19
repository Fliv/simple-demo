import os

def list_files_recursively(directory):
    """
    递归遍历目录及其子目录中的所有文件，并返回包含完整路径的文件列表。

    参数:
        directory (str): 要遍历的目录的路径。

    返回:
        list: 包含所有文件完整路径的列表。如果发生错误，则返回一个空列表。
    """
    file_list = []
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                file_list.append(full_path)
    except OSError as e:
        print(f"发生错误：{e}")  # 打印错误信息
        return [] # 显式返回空列表
    except Exception as e:
        print(f"发生未知错误：{e}")
        return []

    return file_list

if __name__ == "__main__":
    # 指定要遍历的目录。  你可以将 './your_directory' 替换为你想要遍历的实际目录。
    target_directory = './'
    files = list_files_recursively(target_directory)
    if files:
        print("找到以下文件：")
        for file_path in files:
            print(file_path)
    else:
        print(f"未找到任何文件或发生错误。请确保目录 '{target_directory}' 存在且可访问。")
