import os
import json

def build_nested_nav(file_path):
    encodings = ['utf-16le', 'utf-16', 'utf-8', 'latin-1']
    content = None
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                content = f.read()
            break
        except Exception:
            continue
    
    if not content:
        return None

    lines = content.splitlines()
    
    # Mapping of root folders to tabs
    tab_mapping = {
        "Chat": "Overview",
        "Chat (Responses)": "Overview",
        "Overview": "Overview",
        "Help Center": "Overview",
        "Python configuration methods": "Overview",
        "Node.js configuration method": "Overview",
        "PHP configuration method": "Overview",
        "Video Model": "Video",
        "Kling platform": "Video",
        "Suno Music": "Video",
        "Painting Model": "Image",
        "Fal-ai aggregation platform": "Image",
        "Replicate aggregation platform": "Image",
        "Rerank Reordering Model": "Overview",
        "GPTs related": "Overview"
    }

    # Tree structure: tab -> folder_tree
    tabs_tree = {
        "Overview": {},
        "Video": {},
        "Image": {},
        "Exam": {}
    }
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("@@") or line.startswith("+") or line.startswith("-"):
            continue
            
        parts = line.split('\t')
        if len(parts) < 3:
            parts = line.split()
            if len(parts) < 3: continue
            
        new_path = parts[2].strip()
        if new_path.endswith(".md"):
            new_path = new_path[:-3]
            
        path_parts = new_path.split("/")
        root_folder = path_parts[0]
        
        # Determine tab
        tab = tab_mapping.get(root_folder, "Overview")
        if "exam" in new_path.lower():
            tab = "Exam"
            
        # Traverse/Build tree
        current_node = tabs_tree[tab]
        for part in path_parts[:-1]:
            if part not in current_node:
                current_node[part] = {}
            current_node = current_node[part]
        
        # Add the page
        if "__pages__" not in current_node:
            current_node["__pages__"] = []
        current_node["__pages__"].append("chainhub.docs/" + new_path)

    # Function to convert nested dict to Mintlify groups
    def dict_to_nav(d):
        # We need to return a list that can contain strings OR dicts
        pages_list = []
        
        # 1. Collect and sort sub-folders (inner nodes)
        sub_folders = sorted([k for k in d.keys() if k != "__pages__"])
        
        # 2. Add direct pages (leaf nodes)
        if "__pages__" in d:
            for p in sorted(d["__pages__"]):
                pages_list.append(p)
        
        # 3. Add sub-groups
        for folder in sub_folders:
            sub_content = dict_to_nav(d[folder])
            if sub_content:
                pages_list.append({
                    "group": folder,
                    "pages": sub_content
                })
        
        return pages_list

    # Build final result
    final_tabs = []
    for tab_name in ["Overview", "Video", "Image", "Exam"]:
        tree = tabs_tree[tab_name]
        if not tree: continue
        
        tab_groups = []
        # For each top-level key in the tree, create a group
        for root_key in sorted(tree.keys()):
            if root_key == "__pages__":
                # Special case: files at the very top of a tab (rare if based on root folders)
                tab_groups.append({
                    "group": "General",
                    "pages": sorted(tree["__pages__"])
                })
                continue
                
            group_content = dict_to_nav(tree[root_key])
            if group_content:
                tab_groups.append({
                    "group": root_key,
                    "pages": group_content
                })
        
        if tab_groups:
            final_tabs.append({
                "tab": tab_name,
                "groups": tab_groups
            })
            
    return final_tabs

if __name__ == "__main__":
    renames_file = r"c:\Setup\code\chainhub-docs\renames.txt"
    doc_json_file = r"c:\Setup\code\chainhub-docs\doc.json"
    
    nested_nav = build_nested_nav(renames_file)
    if nested_nav:
        with open(doc_json_file, 'r', encoding='utf-8') as f:
            doc_config = json.load(f)
            
        doc_config["navigation"]["tabs"] = nested_nav
        
        with open(doc_json_file, 'w', encoding='utf-8') as f:
            json.dump(doc_config, f, indent=4, ensure_ascii=False)
            
        print("Updated doc.json with MULTI-LEVEL NESTED structure")
