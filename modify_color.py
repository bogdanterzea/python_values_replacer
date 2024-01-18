import sys

def modify_colors(file_path, colors_to_change):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            for color_name, new_color in colors_to_change.items():
                if line.strip().startswith(f"{color_name}:"):
                    line = f"        {color_name}: \"{new_color}\"\n"
            file.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) % 2 != 1:
        print("Usage: python modify_color.py <color_name> <new_color> [<color_name> <new_color> ...]")
        sys.exit(1)

    file_path = 'files_details/ColorFile.bs'
    colors_to_change = {sys.argv[i]: sys.argv[i + 1] for i in range(1, len(sys.argv), 2)}
    modify_colors(file_path, colors_to_change)
