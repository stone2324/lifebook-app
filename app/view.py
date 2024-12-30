import streamlit as st
from streamlit_extras import stylable_container

from notes.a_prologue import prologue_data
from notes.b_the_truth import truth_data
from notes.c_habits import habits_data
from notes.d_personal_skills import personal_skills_data
from notes.e_interpersonal_skills import interpersonal_skills_data
from notes.f_techical_skills import technical_skills_data

HEIGHT = 480
SUBHEADER_SIZE = "####"

def format_content(subcontent, subtitle):
    """Format the content with proper line breaks and headers."""
    lines = subcontent.splitlines()
    formatted_content = f"{SUBHEADER_SIZE} {subtitle}\n\n"
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if not stripped_line:
            continue
            
        formatted_content += stripped_line
        if i < len(lines) - 1:
            next_line = lines[i + 1].strip()
            formatted_content += "  \n   \n" if not next_line else "  \n"
    
    return formatted_content

def display_subsections(subsections):
    """Display subsections either as tabs or single content."""
    if len(subsections) <= 1:
        # Display single subsection
        subtitle, subcontent = next(iter(subsections.items()))
        with stylable_container.stylable_container(
            key="content_container",
            css_styles="{padding: 0px 10px;}"
        ):
            st.markdown(format_content(subcontent, subtitle))
        return

    # Display multiple subsections as tabs
    with stylable_container.stylable_container(
        key="tabs_container",
        css_styles="{padding: 0px 10px;}"
    ):
        subtabs = st.tabs(list(subsections.keys()))
        for subtab_idx, (subtitle, subcontent) in enumerate(subsections.items()):
            with subtabs[subtab_idx]:
                st.markdown(format_content(subcontent, subtitle))

def display_category_content(categories, category):
    """Display the content for a selected category."""
    with st.container(border=True, height=HEIGHT):
        with stylable_container.stylable_container(
            key=f"content_container_{category}",
            css_styles="{padding: 0px 10px;}"
        ):
            subsections = categories[category]
            if isinstance(subsections, dict) and subsections:
                display_subsections(subsections)

def parse_content(content):
    """Parse the content into a nested dictionary of tabs and categories."""
    tab_dict = {}
    sections = content.split("####")[1:]  # Skip the first empty section
    
    for section in sections:
        if not section.strip():
            continue
            
        section_lines = section.split("\n", 1)
        if len(section_lines) != 2:
            continue
            
        header, content = section_lines
        section_parts = header.strip().split("|")
        
        if len(section_parts) != 2:
            continue
            
        tab_name, category_name = map(str.strip, section_parts)
        subsections = content.split("*")
        
        # Process subsections
        subsection_dict = {}
        if len(subsections) <= 1:
            subsection_dict[category_name] = content.strip()
        else:
            for subsection in subsections[1:]:
                if not subsection.strip():
                    continue
                    
                sub_lines = subsection.split("\n", 1)
                if len(sub_lines) == 2:
                    sub_title, sub_content = sub_lines
                    subsection_dict[sub_title.strip()] = sub_content

        # Add to tab dictionary
        if tab_name not in tab_dict:
            tab_dict[tab_name] = {}
        tab_dict[tab_name][category_name] = subsection_dict
        
    return tab_dict

def render_lifebook_page():
    """Main function to render the lifebook page."""
    content = (
        prologue_data + truth_data + habits_data 
        + personal_skills_data + interpersonal_skills_data + technical_skills_data
    )
    
    tab_dict = parse_content(content)
    tabs = st.tabs(list(tab_dict.keys()))

    for idx, (tab_name, categories) in enumerate(tab_dict.items()):
        with tabs[idx]:
            if len(categories) <= 1:
                # Display single category without columns
                category = next(iter(categories.keys()))
                display_category_content(categories, category)
                continue

            # Display multiple categories with columns
            col_category, col_display = st.columns([20, 80])
            with col_category:
                with st.container(border=True, height=HEIGHT):
                    with stylable_container.stylable_container(
                        key="category_radio_container",
                        css_styles="{padding: 30px 10px;}"
                    ):
                        numbered_options = [f"{i+1:02d} - {cat}" for i, cat in enumerate(categories.keys())]
                        options_map = dict(zip(numbered_options, categories.keys()))
                        
                        numbered_category = st.radio(
                            label=f"Select {tab_name} Category",
                            options=numbered_options,
                            label_visibility="collapsed",
                        )
                        category = options_map[numbered_category]
            
            with col_display:
                display_category_content(categories, category)
