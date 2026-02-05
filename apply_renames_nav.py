import sys
import os
import json

def parse_renames(file_path):
    # Try different encodings
    encodings = ['utf-16le', 'utf-16', 'utf-8', 'latin-1']
    content = None
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            print(f"Read success with {enc}")
            break
        except Exception:
            continue
    
    if not content:
        print("Failed to read file with known encodings")
        return None

    lines = content.splitlines()
    navigation = {
        "Overview": {},
        "Video": {},
        "Image": {},
        "Exam": {}
    }
    
    current_tab = "Overview" # Default
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check for tab headers
        if line.startswith("#"):
            header = line[1:].strip().lower()
            if "overview" in header: current_tab = "Overview"
            elif "video" in header: current_tab = "Video"
            elif "image" in header: current_tab = "Image"
            elif "exam" in header: current_tab = "Exam"
            continue
            
        parts = line.split('\t')
        if len(parts) < 3:
            # Try spaces if tabs are missing
            parts = line.split()
            if len(parts) < 3: continue
            
        # Column 3 is the new path: "Folder/Sub/file.md"
        new_path = parts[2].strip()
        if new_path.endswith(".md"):
            new_path = new_path[:-3]
            
        # Split folder and file
        if "/" in new_path:
            folder_parts = new_path.split("/")
            group_name = " > ".join(folder_parts[:-1])
            page_path = "chainhub.docs/" + new_path
        else:
            group_name = "Introduction"
            page_path = "chainhub.docs/" + new_path
            
        if group_name not in navigation[current_tab]:
            navigation[current_tab][group_name] = []
        
        navigation[current_tab][group_name].append(page_path)
    
    # Format into Mintlify structure
    nav_tabs = []
    for tab_name in ["Overview", "Video", "Image", "Exam"]:
        groups_dict = navigation[tab_name]
        if not groups_dict: continue
        
        tab_groups = []
        for group_name, pages in groups_dict.items():
            tab_groups.append({
                "group": group_name,
                "pages": sorted(pages)
            })
        
        nav_tabs.append({
            "tab": tab_name,
            "groups": tab_groups
        })
        
    return nav_tabs

if __name__ == "__main__":
    renames_file = r"c:\Setup\code\chainhub-docs\renames.txt"
    doc_json_file = r"c:\Setup\code\chainhub-docs\doc.json"
    
    nav_structure = parse_renames(renames_file)
    if nav_structure:
        with open(doc_json_file, 'r', encoding='utf-8') as f:
            doc_config = json.load(f)
            
        doc_config["navigation"]["tabs"] = nav_structure
        
        with open(doc_json_file, 'w', encoding='utf-8') as f:
            json.dump(doc_config, f, indent=4, ensure_ascii=False)
            
        print("Updated doc.json with structure from renames.txt")
