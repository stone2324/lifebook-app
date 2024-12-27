import streamlit as st
from app.data import data

HEIGHT= 400

def render_lifebook_page():
    content = data

    # First split by major sections (####)
    sections = content.split("####")
    
    # Get title from first section
    title = sections[0].strip()

    # Create a nested dictionary for tabs and their categories
    tab_dict = {}
    for section in sections[1:]:  # Skip the first section (title)
        if not section.strip():
            continue
            
        # Split first line for tab/category names
        section_lines = section.split("\n", 1)
        if len(section_lines) == 2:
            header, content = section_lines
            section_parts = header.strip().split(",")
            
            if len(section_parts) == 2:
                tab_name = section_parts[0].strip()
                category_name = section_parts[1].strip()

                # Split content into subsections based on *
                subsections = content.split("*")
                
                # Create dictionary of subsections
                subsection_dict = {}
                for subsection in subsections[1:]:  # Skip first empty split
                    if not subsection.strip():
                        continue
                        
                    # Split first line for subsection title
                    sub_lines = subsection.split("\n", 1)
                    if len(sub_lines) == 2:
                        sub_title = sub_lines[0].strip()
                        sub_content = sub_lines[1]  # Keep original formatting
                        subsection_dict[sub_title] = sub_content

                # Create tab if it doesn't exist
                if tab_name not in tab_dict:
                    tab_dict[tab_name] = {}

                # Add category and content to tab
                tab_dict[tab_name][category_name] = subsection_dict

    # Create tabs
    tabs = st.tabs(list(tab_dict.keys()))

    # For each tab, create radio buttons for categories
    for idx, (tab_name, categories) in enumerate(tab_dict.items()):
        with tabs[idx]:
            # Only create columns if there's more than one category
            if len(categories) > 1:
                col1, col2 = st.columns([25, 75])
                with col1:
                    with st.container(border=True, height=HEIGHT):
                        category = st.radio(
                            label=f"Select {tab_name} Category",
                            options=list(categories.keys()),
                            label_visibility="collapsed",
                        )
                
                # Display content in the second column
                with col2:
                    with st.container(border=True, height=HEIGHT):
                        subsections = categories[category]
                        if isinstance(subsections, dict) and len(subsections) > 0:
                            # Only create tabs if there's more than one subsection
                            if len(subsections) > 1:
                                subtabs = st.tabs(list(subsections.keys()))
                                for subtab_idx, (subtitle, subcontent) in enumerate(subsections.items()):
                                    with subtabs[subtab_idx]:
                                        # Format content logic here...
                                        lines = subcontent.splitlines()
                                        # Add subtitle as header
                                        formatted_content = f"#### {subtitle}\n\n"
                                        for i, line in enumerate(lines):
                                            stripped_line = line.strip()
                                            if stripped_line:
                                                formatted_content += stripped_line
                                                if i < len(lines) - 1:
                                                    next_line = lines[i + 1].strip()
                                                    if not next_line:
                                                        formatted_content += "  \n   \n"
                                                    else:
                                                        formatted_content += "  \n"
                                        
                                        st.markdown(formatted_content)
                            else:
                                # If only one subsection, display it directly
                                subtitle = list(subsections.keys())[0]
                                subcontent = list(subsections.values())[0]
                                lines = subcontent.splitlines()
                                # Add subtitle as header
                                formatted_content = f"#### {subtitle}\n\n"
                                for i, line in enumerate(lines):
                                    stripped_line = line.strip()
                                    if stripped_line:
                                        formatted_content += stripped_line
                                        if i < len(lines) - 1:
                                            next_line = lines[i + 1].strip()
                                            if not next_line:
                                                formatted_content += "  \n   \n"
                                            else:
                                                formatted_content += "  \n"
                                
                                st.markdown(formatted_content)
            else:
                # If only one category, display content directly without columns
                category = list(categories.keys())[0]
                with st.container(border=True, height=HEIGHT):
                    subsections = categories[category]
                    if isinstance(subsections, dict) and len(subsections) > 0:
                        # Only create tabs if there's more than one subsection
                        if len(subsections) > 1:
                            subtabs = st.tabs(list(subsections.keys()))
                            for subtab_idx, (subtitle, subcontent) in enumerate(subsections.items()):
                                with subtabs[subtab_idx]:
                                    # Format content logic here...
                                    lines = subcontent.splitlines()
                                    # Add subtitle as header
                                    formatted_content = f"#### {subtitle}\n\n"
                                    for i, line in enumerate(lines):
                                        stripped_line = line.strip()
                                        if stripped_line:
                                            formatted_content += stripped_line
                                            if i < len(lines) - 1:
                                                next_line = lines[i + 1].strip()
                                                if not next_line:
                                                    formatted_content += "  \n   \n"
                                                else:
                                                    formatted_content += "  \n"
                                    
                                    st.markdown(formatted_content)
                        else:
                            # If only one subsection, display it directly
                            subtitle = list(subsections.keys())[0]
                            subcontent = list(subsections.values())[0]
                            lines = subcontent.splitlines()
                            # Add subtitle as header
                            formatted_content = f"#### {subtitle}\n\n"
                            for i, line in enumerate(lines):
                                stripped_line = line.strip()
                                if stripped_line:
                                    formatted_content += stripped_line
                                    if i < len(lines) - 1:
                                        next_line = lines[i + 1].strip()
                                        if not next_line:
                                            formatted_content += "  \n   \n"
                                        else:
                                            formatted_content += "  \n"
                            
                            st.markdown(formatted_content)
