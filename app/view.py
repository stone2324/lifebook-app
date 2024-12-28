import streamlit as st

from data.prologue import prologue_data
from data.the_truth import truth_data
from data.skills import skills_data

HEIGHT= 400

def render_lifebook_page():
    content = prologue_data + truth_data + skills_data

    # First split by major sections (####)
    sections = content.split("####")
    
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
                
                # If there are no * markers, use the category name as the subtitle
                if len(subsections) <= 1:
                    subsection_dict[category_name] = content.strip()
                else:
                    # Process subsections as before
                    for subsection in subsections[1:]:
                        if not subsection.strip():
                            continue
                            
                        sub_lines = subsection.split("\n", 1)
                        if len(sub_lines) == 2:
                            sub_title = sub_lines[0].strip()
                            sub_content = sub_lines[1]
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
                col_category, col_display = st.columns([25, 75])
                with col_category:
                    with st.container(border=True, height=HEIGHT):
                        # Create numbered options for the radio buttons
                        numbered_options = [f"{i+1:02d} - {cat}" for i, cat in enumerate(categories.keys())]
                        # Create a mapping from numbered options back to original categories
                        options_map = {numbered: orig for numbered, orig in zip(numbered_options, categories.keys())}
                        
                        numbered_category = st.radio(
                            label=f"Select {tab_name} Category",
                            options=numbered_options,
                            label_visibility="collapsed",
                        )
                        # Convert back to original category name for lookup
                        category = options_map[numbered_category]
                
                # Display content in the second column
                with col_display:
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
