import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_rag_diagram():
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 120)
    ax.axis('off')

    # Styles
    box_props = dict(boxstyle='round,pad=1', facecolor='white', edgecolor='#333333', linewidth=1.5)
    inner_box_props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#333333', linewidth=1)
    
    # --- SECTION: INGESTION ---
    ax.add_patch(patches.FancyBboxPatch((30, 85), 65, 30, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='#f9f9f9'))
    ax.text(32, 112, "Ingestion", fontsize=10, weight='bold', color='#333333')

    # Source Data
    ax.text(35, 96, "GlassDoor\nJob Datasets", ha='center', va='center', fontsize=9, bbox=inner_box_props)
    
    # Arrow
    ax.arrow(42, 96, 5, 0, head_width=1, head_length=1, fc='gray', ec='gray')

    # Chunks
    ax.add_patch(patches.FancyBboxPatch((50, 88), 25, 16, boxstyle="round,pad=0.2", linewidth=1, edgecolor='gray', facecolor='white'))
    ax.text(52, 102, "Chunks", fontsize=9)
    # Draw mini docs
    for i, x in enumerate([53, 60, 67]):
        for j, y in enumerate([90, 96]):
            ax.add_patch(patches.Rectangle((x, y), 4, 5, fill=False, edgecolor='gray'))
    
    # Arrow
    ax.arrow(77, 96, 5, 0, head_width=1, head_length=1, fc='gray', ec='gray')

    # Embedding Model (Ingestion)
    ax.text(88, 96, "Embedding\nModel", ha='center', va='center', fontsize=9, bbox=inner_box_props)


    # --- SECTION: USER ---
    ax.add_patch(patches.FancyBboxPatch((2, 55), 25, 25, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='#f9f9f9'))
    ax.text(5, 77, "User", fontsize=10, weight='bold', color='#333333')
    
    query_text = "Query: I'm a Python\ndeveloper, I want to be\na Data Science developer.\nWhat should be my\ncareer path?"
    ax.text(14.5, 66, query_text, ha='center', va='center', fontsize=9, wrap=True, bbox=dict(boxstyle='round,pad=1', facecolor='white', edgecolor='gray'))

    # Arrow from User to Retrieval
    ax.arrow(28, 66, 3, 0, head_width=1, head_length=1, fc='gray', ec='gray')


    # --- SECTION: RETRIEVAL ---
    ax.add_patch(patches.FancyBboxPatch((30, 45), 65, 35, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='#f9f9f9'))
    ax.text(32, 77, "Retrieval", fontsize=10, weight='bold', color='#333333')

    # Embedding Model (Retrieval)
    ax.text(40, 66, "Embedding\nModel", ha='center', va='center', fontsize=9, bbox=inner_box_props)
    
    # Arrow
    ax.arrow(46, 66, 5, 0, head_width=1, head_length=1, fc='gray', ec='gray')

    # Vector Database
    ax.add_patch(patches.FancyBboxPatch((54, 48), 20, 25, boxstyle="round,pad=0.2", linewidth=1, edgecolor='gray', facecolor='white'))
    ax.text(60, 71, "Vector Database", fontsize=9)
    ax.text(64, 65, "Dense Index", ha='center', va='center', fontsize=8, bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray'))
    ax.text(64, 56, "Sparse Index", ha='center', va='center', fontsize=8, bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='gray'))

    # Arrow
    ax.arrow(75, 60, 5, 0, head_width=1, head_length=1, fc='gray', ec='gray')

    # Rerank
    ax.text(85, 60, "Rerank", ha='center', va='center', fontsize=9, bbox=inner_box_props)

    # Connector line from Ingestion Embedding to Vector DB
    ax.plot([88, 88, 64, 64], [90, 83, 83, 75], color='gray', lw=1)
    ax.arrow(64, 76, 0, -1, head_width=1, head_length=1, fc='gray', ec='gray')


    # --- SECTION: GENERATION & AUGMENTATION ---
    # Generation Box
    ax.add_patch(patches.FancyBboxPatch((30, 25), 32, 15, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='#f9f9f9'))
    ax.text(32, 37, "Generation", fontsize=10, weight='bold')
    ax.text(46, 31, "LLM", ha='center', va='center', fontsize=10, bbox=inner_box_props)

    # Augmentation Box
    ax.add_patch(patches.FancyBboxPatch((65, 25), 30, 15, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='#f9f9f9'))
    ax.text(67, 37, "Augmentation", fontsize=10, weight='bold')
    ax.text(80, 31, "Query + Context", ha='center', va='center', fontsize=9)

    # Arrow from Rerank to Augmentation
    ax.plot([85, 85], [55, 35], color='gray', lw=1)
    
    # Arrow from Augmentation to Generation
    ax.arrow(72, 31, -20, 0, head_width=1, head_length=1, fc='gray', ec='gray')

    # --- SECTION: FINAL OUTPUT ---
    ax.add_patch(patches.FancyBboxPatch((30, 0), 65, 20, boxstyle="round,pad=0.5", linewidth=1, edgecolor='#333333', facecolor='white'))
    
    output_text = (
        "OUTPUT: Based on GlassDoor job datasets, here is a career path "
        "for a Python Dev pivoting to Data Science:\n\n"
        "1. Master Data Libraries (Pandas, NumPy)\n"
        "2. Learn SQL & Database Management\n"
        "3. Study Machine Learning (Scikit-Learn)\n\n"
        "This path leverages your existing coding skills to fast-track "
        "your transition into Data Science."
    )
    ax.text(32, 10, output_text, ha='left', va='center', fontsize=9, wrap=True)

    # Arrow from LLM to Output
    ax.arrow(46, 26, 0, -8, head_width=1, head_length=1, fc='gray', ec='gray')

    plt.tight_layout()
    plt.show()

draw_rag_diagram()