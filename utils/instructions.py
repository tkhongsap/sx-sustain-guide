from textwrap import dedent

parsing_instruction = dedent("""
    The document provided is a PDF file. Please extract detailed information and organize it in a comprehensive and coherent manner, focusing on key concepts, methodologies, and practical applications.

    Exclude any styles, CSS, or formatting details. Only extract meaningful content such as text, descriptions, diagrams, tables, and summaries.

    For diagrams, flow charts, infographics, images, long tables, and illustrations:
      - Extract textual information, including labels, captions, notes, and annotations.
      - For flow charts, represent the flow of processes and decisions using bullet points, markdown tables, or flowchart syntax (e.g., Mermaid or PlantUML).
      - For diagrams and infographics, break them into simpler components, ensuring that relationships and connections are clear.
      - For images, provide a summary or interpretation, focusing on key elements relevant to understanding the content.
      - Use markdown to format descriptions and represent structured data (e.g., charts) in tables or lists.
      - Indicate the location of visuals with a placeholder (e.g., [Infographic: Title]) and briefly describe their purpose or relevance.

    For long tables:
      - Extract and represent all table data in markdown format.

    For flow charts:
      - Represent each step or decision using bullet points or a numbered list.

    For illustrations:
      - Describe key components and their relationships.

    Highlight important terms and their definitions.
    Summarize each major section of the document with as much detail as necessary while ensuring clarity and coherence.
""")


from textwrap import dedent

parsing_instruction_summary = dedent("""
        The document provided is a PDF file. Please extract key summaries and essential highlights, organizing the information in a clear and concise manner. Focus on core concepts, methodologies, and significant practical applications.

        For **summarizing**:
        - **Core concepts**: Focus on primary ideas, theories, and models mentioned.
        - **Methodologies**: Summarize the general approach and significant steps.
        - **Applications**: Extract key practical uses or implementations without going into granular detail.

        For **key terms**:
        - Highlight **important definitions** and **key terms**, but do not extract full explanations. Use concise descriptions to ensure the concept is understood quickly.
        - Ensure major frameworks, approaches, or systems are clearly summarized in one or two sentences.

        For **tables** and **charts**:
        - Extract only the main **trends**, **patterns**, or **key figures**.
        - Represent data highlights in a simplified markdown format, avoiding unnecessary detail.

        For **diagrams**, **flow charts**, and **infographics**:
        - Summarize the general flow or key relationships, ensuring high-level understanding.
        - Only extract key points and insights that are critical for understanding the content.

        For **methodologies and processes**:
        - Provide a brief overview of the main steps, using bullet points or lists where appropriate.

        For **sections of the document**:
        - Provide a brief **summary** of each major section, highlighting the most significant takeaways or points.
        - Ensure summaries are **concise** but **informative**, capturing the essence of each section in one or two paragraphs.

        For **illustrations**:
        - Provide a high-level description of the image, focusing on **key elements** relevant to the text.
        
        Where applicable, organize content using **markdown** for better readability:
        - Use headings (##) for section titles.
        - Bullet points for lists of key highlights.
        - Tables for summarizing key figures or comparisons.
    """)