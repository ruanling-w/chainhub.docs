import os
import json

def generate_navigation(root_dir):
    docs_dir = os.path.join(root_dir, "chainhub.docs")
    
    # Define tab mappings
    tabs = {
        "Overview": {
            "folders": [
                "Overview", 
                "Help Center", 
                "Python configuration methods", 
                "Node.js configuration method", 
                "PHP configuration method",
                "Chat",
                "Chat (Responses)",
                "GPTs related",
                "Rerank Reordering Model"
            ],
            "groups": {}
        },
        "Video": {
            "folders": ["Video Model", "Kling platform", "Suno Music"],
            "groups": {}
        },
        "Image": {
            "folders": ["Painting Model", "Fal-ai aggregation platform", "Replicate aggregation platform"],
            "groups": {}
        },
        "Exam": {
            "folders": [],
            "groups": {"Exam API": []}
        }
    }

    # Files at the root of chainhub.docs (like index.md) go to Overview -> Introduction
    root_files = []
    for f in os.listdir(docs_dir):
        if f.endswith(".md"):
            root_files.append(f"chainhub.docs/{f[:-3]}")
    
    if root_files:
        tabs["Overview"]["groups"]["Introduction"] = root_files

    # Walk through folders
    for tab_name, config in tabs.items():
        for folder in config["folders"]:
            folder_path = os.path.join(docs_dir, folder)
            if not os.path.exists(folder_path):
                continue
            
            for root, dirs, files in os.walk(folder_path):
                md_files = [f for f in files if f.endswith(".md")]
                if not md_files:
                    continue
                
                # Create group name from subfolder structure
                rel_path = os.path.relpath(root, docs_dir)
                group_name = rel_path.replace("\\", " > ")
                
                pages = []
                for f in sorted(md_files):
                    # Mintlify paths use forward slashes and no .md extension
                    full_rel_path = os.path.relpath(os.path.join(root, f), root_dir).replace("\\", "/")
                    pages.append(full_rel_path[:-3])
                
                if tab_name == "Exam" or "exam" in group_name.lower():
                    tabs["Exam"]["groups"].setdefault("Exam Resources", []).extend(pages)
                else:
                    tabs[tab_name]["groups"][group_name] = pages

    # Build final result
    nav_tabs = []
    for tab_name, config in tabs.items():
        tab_groups = []
        for group_name, pages in config["groups"].items():
            if pages:
                tab_groups.append({
                    "group": group_name,
                    "pages": pages
                })
        
        if tab_groups:
            nav_tabs.append({
                "tab": tab_name,
                "groups": tab_groups
            })

    return nav_tabs

if __name__ == "__main__":
    base_dir = r"c:\Setup\code\chainhub-docs"
    navigation = generate_navigation(base_dir)
    
    # Load original doc.json to keep other settings
    with open(os.path.join(base_dir, "doc.json"), "r", encoding="utf-8") as f:
        config = json.load(f)
    
    config["navigation"]["tabs"] = navigation
    
    with open(os.path.join(base_dir, "doc.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    
    print("Successfully mapped 300+ files into doc.json")
